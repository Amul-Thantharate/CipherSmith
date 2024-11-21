import unittest
from app.password_strength import PasswordStrengthAnalyzer, StrengthAnalysis

class TestPasswordStrength(unittest.TestCase):
    def setUp(self):
        self.analyzer = PasswordStrengthAnalyzer()

    def test_weak_password(self):
        """Test analysis of a weak password."""
        analysis = self.analyzer.analyze("password123")
        self.assertLessEqual(analysis.score, 1)
        self.assertIn("letters_followed_by_numbers", analysis.patterns_found)
        self.assertTrue(any("common" in suggestion.lower() for suggestion in analysis.suggestions))

    def test_medium_password(self):
        """Test analysis of a medium-strength password."""
        analysis = self.analyzer.analyze("P@ssw0rd2023!")
        self.assertGreaterEqual(analysis.score, 2)
        self.assertLessEqual(analysis.score, 3)

    def test_strong_password(self):
        """Test analysis of a strong password."""
        analysis = self.analyzer.analyze("xK9#mP$vL2nX&qR5")
        self.assertGreaterEqual(analysis.score, 3)
        self.assertLess(len(analysis.patterns_found), 2)

    def test_repeated_chars_pattern(self):
        """Test detection of repeated characters."""
        analysis = self.analyzer.analyze("passssword123")
        self.assertIn("repeated_chars", analysis.patterns_found)
        self.assertTrue(any("repeat" in feedback.lower() for feedback in analysis.feedback))

    def test_common_sequence_pattern(self):
        """Test detection of common sequences."""
        analysis = self.analyzer.analyze("abcdef123456")
        self.assertIn("common_sequence", analysis.patterns_found)
        self.assertTrue(any("sequence" in feedback.lower() for feedback in analysis.feedback))

    def test_letters_followed_by_numbers(self):
        """Test detection of letters followed by numbers pattern."""
        analysis = self.analyzer.analyze("Password123")
        self.assertIn("letters_followed_by_numbers", analysis.patterns_found)

    def test_character_variety(self):
        """Test detection of low character variety."""
        analysis = self.analyzer.analyze("aaaaabbbbbcccc")
        self.assertIn("low_character_variety", analysis.patterns_found)

    def test_crack_time_formatting(self):
        """Test crack time formatting for different durations."""
        self.assertEqual(
            self.analyzer._format_crack_time(30),
            "30.0 seconds"
        )
        self.assertEqual(
            self.analyzer._format_crack_time(3600),
            "1.0 hours"
        )
        self.assertEqual(
            self.analyzer._format_crack_time(86400),
            "1.0 days"
        )

    def test_suggestions_generation(self):
        """Test that appropriate suggestions are generated."""
        analysis = self.analyzer.analyze("password123")
        self.assertTrue(len(analysis.suggestions) > 0)
        self.assertTrue(any("variety" in suggestion.lower() 
                          or "mix" in suggestion.lower() 
                          for suggestion in analysis.suggestions))

    def test_very_strong_password(self):
        """Test analysis of a very strong password."""
        analysis = self.analyzer.analyze("xK9#mP$vL2nX&qR5@jW8")
        self.assertEqual(analysis.score, 4)
        self.assertEqual(len(analysis.patterns_found), 0)

if __name__ == '__main__':
    unittest.main()
