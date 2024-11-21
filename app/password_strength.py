from dataclasses import dataclass
from typing import List, Dict
import re
from rich.console import Console
from rich.progress_bar import ProgressBar
from rich.panel import Panel
from rich.text import Text
import math
import zxcvbn

@dataclass
class StrengthAnalysis:
    score: int  # 0-4
    feedback: List[str]
    crack_time_seconds: float
    patterns_found: List[str]
    suggestions: List[str]

class PasswordStrengthAnalyzer:
    def __init__(self):
        self.console = Console()
        
    def analyze(self, password: str) -> StrengthAnalysis:
        """Analyze password strength using multiple criteria."""
        # Use zxcvbn for comprehensive analysis
        result = zxcvbn.zxcvbn(password)
        
        # Extract core metrics
        score = result['score']
        crack_time = result['crack_times_seconds']['offline_fast_hashing_1e10_per_second']
        
        # Analyze patterns
        patterns = self._analyze_patterns(password)
        
        # Generate feedback and suggestions
        feedback = self._generate_feedback(result, patterns)
        suggestions = self._generate_suggestions(result, patterns)
        
        return StrengthAnalysis(
            score=score,
            feedback=feedback,
            crack_time_seconds=crack_time,
            patterns_found=patterns,
            suggestions=suggestions
        )
    
    def _analyze_patterns(self, password: str) -> List[str]:
        """Identify common password patterns."""
        patterns = []
        
        # Only check for patterns if the password is not already very strong
        result = zxcvbn.zxcvbn(password)
        if result['score'] < 4:
            if re.search(r'(\w)\1{2,}', password):
                patterns.append("repeated_chars")
                
            if re.search(r'(123|abc|qwerty)', password.lower()):
                patterns.append("common_sequence")
                
            if re.search(r'[a-zA-Z]+\d+$', password):
                patterns.append("letters_followed_by_numbers")
                
            if len(set(password)) < len(password) * 0.7:
                patterns.append("low_character_variety")
        
        return patterns
    
    def _generate_feedback(self, zxcvbn_result: Dict, patterns: List[str]) -> List[str]:
        """Generate user-friendly feedback based on analysis."""
        feedback = []
        
        # Add zxcvbn feedback
        if zxcvbn_result['feedback']['warning']:
            feedback.append(zxcvbn_result['feedback']['warning'])
            
        # Add pattern-based feedback
        pattern_messages = {
            "repeated_chars": "Contains repeated characters",
            "common_sequence": "Uses a common character sequence",
            "letters_followed_by_numbers": "Follows a common pattern (letters then numbers)",
            "low_character_variety": "Uses too few unique characters"
        }
        
        for pattern in patterns:
            if pattern in pattern_messages:
                feedback.append(pattern_messages[pattern])
                
        return feedback
    
    def _generate_suggestions(self, zxcvbn_result: Dict, patterns: List[str]) -> List[str]:
        """Generate improvement suggestions based on analysis."""
        suggestions = []
        
        # Add zxcvbn suggestions
        suggestions.extend(zxcvbn_result['feedback']['suggestions'])
        
        # Add custom suggestions based on patterns
        if "repeated_chars" in patterns:
            suggestions.append("Avoid repeating characters")
            
        if "common_sequence" in patterns:
            suggestions.append("Avoid common sequences like '123' or 'abc'")
            
        if "letters_followed_by_numbers" in patterns:
            suggestions.append("Mix numbers throughout the password instead of adding them at the end")
            
        if "low_character_variety" in patterns:
            suggestions.append("Use a greater variety of characters")
            
        return suggestions
    
    def visualize_strength(self, analysis: StrengthAnalysis):
        """Display a rich visualization of password strength."""
        # Create progress bar
        strength_percentage = (analysis.score / 4) * 100
        bar_color = {
            0: "red",
            1: "red",
            2: "yellow",
            3: "green",
            4: "bright_green"
        }[analysis.score]
        
        strength_text = {
            0: "Very Weak",
            1: "Weak",
            2: "Medium",
            3: "Strong",
            4: "Very Strong"
        }[analysis.score]
        
        # Create main display
        self.console.print("\n[bold]Password Strength Analysis[/bold]\n")
        
        # Show strength bar
        self.console.print(f"Strength: {strength_text}")
        progress = ProgressBar(total=100, completed=strength_percentage, width=40)
        self.console.print(progress, style=bar_color)
        
        # Show crack time
        crack_time = self._format_crack_time(analysis.crack_time_seconds)
        self.console.print(f"\nEstimated crack time: {crack_time}")
        
        # Show feedback
        if analysis.feedback:
            self.console.print("\n[bold]Issues Found:[/bold]")
            for item in analysis.feedback:
                self.console.print(f"✗ {item}")
                
        # Show suggestions
        if analysis.suggestions:
            self.console.print("\n[bold]Suggestions:[/bold]")
            for suggestion in analysis.suggestions:
                self.console.print(f"• {suggestion}")
    
    def _format_crack_time(self, seconds: float) -> str:
        """Format crack time in a human-readable way."""
        if seconds < 60:
            return f"{seconds:.1f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.1f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.1f} hours"
        elif seconds < 2592000:
            return f"{seconds/86400:.1f} days"
        elif seconds < 31536000:
            return f"{seconds/2592000:.1f} months"
        else:
            return f"{seconds/31536000:.1f} years"

def check_password_strength(password: str):
    """Convenience function to analyze and visualize password strength."""
    analyzer = PasswordStrengthAnalyzer()
    analysis = analyzer.analyze(password)
    analyzer.visualize_strength(analysis)
    return analysis
