"""Encryption module for CipherSmith."""

from cryptography.fernet import Fernet
import base64

class Encryptor:
    """Handles encryption and decryption of sensitive data."""

    def __init__(self, key=None):
        """Initialize encryptor with a key.
        
        Args:
            key (bytes, optional): Encryption key. If None, generates a new key.
        """
        self.key = key if key else Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, data):
        """Encrypt data.
        
        Args:
            data (str): Data to encrypt
        
        Returns:
            bytes: Encrypted data
        """
        if not isinstance(data, str):
            raise ValueError("Data must be a string")
        return self.cipher_suite.encrypt(data.encode('utf-8'))

    def decrypt(self, encrypted_data):
        """Decrypt data.
        
        Args:
            encrypted_data (bytes): Data to decrypt
        
        Returns:
            str: Decrypted data
        """
        if not isinstance(encrypted_data, bytes):
            raise ValueError("Encrypted data must be bytes")
        try:
            decrypted = self.cipher_suite.decrypt(encrypted_data)
            return decrypted.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Failed to decrypt data: {str(e)}")

    def save_key(self, filename):
        """Save encryption key to file.
        
        Args:
            filename (str): Path to save the key
        """
        with open(filename, 'wb') as f:
            f.write(self.key)

    @staticmethod
    def load_key(filename):
        """Load encryption key from file.
        
        Args:
            filename (str): Path to key file
        
        Returns:
            bytes: Encryption key
        """
        with open(filename, 'rb') as f:
            return f.read()
