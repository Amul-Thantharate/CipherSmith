"""Password generation module for CipherSmith."""

import random
import string
import re

class PasswordGenerator:
    """Generates secure passwords with customizable options."""

    def __init__(self):
        self.uppercase_letters = string.ascii_uppercase
        self.lowercase_letters = string.ascii_lowercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def generate(self, length=12, letters=True, numbers=True, special_chars=True):
        """Generate a password with specified options.
        
        Args:
            length (int): Length of the password
            letters (bool): Include letters
            numbers (bool): Include numbers
            special_chars (bool): Include special characters
        
        Returns:
            str: Generated password
        """
        if not any([letters, numbers, special_chars]):
            raise ValueError("At least one character type must be selected")

        # Create character pool based on options
        char_pool = ""
        if letters:
            char_pool += self.uppercase_letters + self.lowercase_letters
        if numbers:
            char_pool += self.digits
        if special_chars:
            char_pool += self.special_chars

        # Generate password
        password = [random.choice(char_pool) for _ in range(length)]

        # Ensure at least one character of each selected type
        if letters:
            password[0] = random.choice(self.uppercase_letters)
            password[1] = random.choice(self.lowercase_letters)
        if numbers:
            password[2 if letters else 0] = random.choice(self.digits)
        if special_chars:
            password[3 if letters else (1 if numbers else 0)] = random.choice(self.special_chars)

        # Shuffle the password
        random.shuffle(password)
        return ''.join(password)

    def check_strength(self, password):
        """Check the strength of a password.
        
        Args:
            password (str): Password to check
        
        Returns:
            float: Strength score between 0 and 1
        """
        score = 0
        checks = [
            (r'[A-Z]', 0.2),  # Uppercase letters
            (r'[a-z]', 0.2),  # Lowercase letters
            (r'\d', 0.2),     # Numbers
            (r'[^A-Za-z0-9]', 0.2),  # Special characters
            (r'.{8,}', 0.1),  # Length >= 8
            (r'.{12,}', 0.1)  # Length >= 12
        ]

        for pattern, weight in checks:
            if re.search(pattern, password):
                score += weight

        return score
