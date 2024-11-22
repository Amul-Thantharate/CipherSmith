import unittest
from ciphersmith.password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PasswordGenerator()

    def test_generate_password_default(self):
        """Test password generation with default settings"""
        password = self.generator.generate()
        self.assertEqual(len(password), 12)  # Default length
        self.assertTrue(any(c.isupper() for c in password))  # Contains uppercase
        self.assertTrue(any(c.islower() for c in password))  # Contains lowercase
        self.assertTrue(any(c.isdigit() for c in password))  # Contains numbers
        self.assertTrue(any(not c.isalnum() for c in password))  # Contains special chars

    def test_generate_password_custom_length(self):
        """Test password generation with custom length"""
        length = 20
        password = self.generator.generate(length=length)
        self.assertEqual(len(password), length)

    def test_generate_password_no_special_chars(self):
        """Test password generation without special characters"""
        password = self.generator.generate(special_chars=False)
        self.assertTrue(all(c.isalnum() for c in password))

    def test_generate_password_only_numbers(self):
        """Test password generation with only numbers"""
        password = self.generator.generate(letters=False, special_chars=False)
        self.assertTrue(all(c.isdigit() for c in password))

    def test_generate_password_only_letters(self):
        """Test password generation with only letters"""
        password = self.generator.generate(numbers=False, special_chars=False)
        self.assertTrue(all(c.isalpha() for c in password))

    def test_generate_multiple_passwords(self):
        """Test generation of multiple unique passwords"""
        passwords = [self.generator.generate() for _ in range(100)]
        # Check all passwords are unique
        self.assertEqual(len(passwords), len(set(passwords)))

    def test_password_strength(self):
        """Test password strength calculation"""
        password = self.generator.generate()
        strength = self.generator.check_strength(password)
        self.assertGreaterEqual(strength, 0.7)  # Strong password threshold

if __name__ == '__main__':
    unittest.main()
