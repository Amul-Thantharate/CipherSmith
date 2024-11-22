import unittest
import os
from ciphersmith.encryption import Encryptor
from cryptography.fernet import Fernet

class TestEncryption(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.key = Fernet.generate_key()
        self.encryptor = Encryptor(self.key)
        self.test_data = "sensitive_password123"

    def test_encryption_decryption(self):
        """Test basic encryption and decryption"""
        # Encrypt data
        encrypted_data = self.encryptor.encrypt(self.test_data)
        self.assertNotEqual(encrypted_data, self.test_data)

        # Decrypt data
        decrypted_data = self.encryptor.decrypt(encrypted_data)
        self.assertEqual(decrypted_data, self.test_data)

    def test_multiple_encryptions(self):
        """Test that multiple encryptions of the same data produce different results"""
        encrypted1 = self.encryptor.encrypt(self.test_data)
        encrypted2 = self.encryptor.encrypt(self.test_data)
        self.assertNotEqual(encrypted1, encrypted2)

    def test_key_persistence(self):
        """Test encryption key storage and retrieval"""
        # Save key to file
        key_file = "test_key.key"
        self.encryptor.save_key(key_file)
        
        # Check key file exists
        self.assertTrue(os.path.exists(key_file))
        
        # Load key and create new encryptor
        loaded_key = Encryptor.load_key(key_file)
        new_encryptor = Encryptor(loaded_key)
        
        # Test encryption/decryption with loaded key
        encrypted = self.encryptor.encrypt(self.test_data)
        decrypted = new_encryptor.decrypt(encrypted)
        self.assertEqual(decrypted, self.test_data)
        
        # Clean up
        os.remove(key_file)

    def test_invalid_key(self):
        """Test encryption with invalid key"""
        invalid_key = Fernet.generate_key()
        invalid_encryptor = Encryptor(invalid_key)
        
        # Encrypt with original key
        encrypted = self.encryptor.encrypt(self.test_data)
        
        # Try to decrypt with different key
        with self.assertRaises(Exception):
            invalid_encryptor.decrypt(encrypted)

    def test_empty_string(self):
        """Test encryption of empty string"""
        empty_string = ""
        encrypted = self.encryptor.encrypt(empty_string)
        decrypted = self.encryptor.decrypt(encrypted)
        self.assertEqual(decrypted, empty_string)

    def test_special_characters(self):
        """Test encryption with special characters"""
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        encrypted = self.encryptor.encrypt(special_chars)
        decrypted = self.encryptor.decrypt(encrypted)
        self.assertEqual(decrypted, special_chars)

    def test_large_data(self):
        """Test encryption of large data"""
        large_data = "x" * 1000000  # 1MB of data
        encrypted = self.encryptor.encrypt(large_data)
        decrypted = self.encryptor.decrypt(encrypted)
        self.assertEqual(decrypted, large_data)

if __name__ == '__main__':
    unittest.main()
