"""Storage module for CipherSmith."""

import json
import os
from .encryption import Encryptor

class PasswordStorage:
    """Manages secure storage of passwords and related data."""

    def __init__(self, storage_file, key_file):
        """Initialize storage with file paths.
        
        Args:
            storage_file (str): Path to password storage file
            key_file (str): Path to encryption key file
        """
        self.storage_file = storage_file
        self.key_file = key_file
        
        # Initialize encryption
        if os.path.exists(key_file):
            self.encryptor = Encryptor(Encryptor.load_key(key_file))
        else:
            self.encryptor = Encryptor()
            self.encryptor.save_key(key_file)
        
        # Initialize storage
        self.passwords = {}
        if os.path.exists(storage_file):
            self.load_database()
        else:
            self.save_database()

    def add_password(self, service, username, password, url="", notes=""):
        """Add a new password entry.
        
        Args:
            service (str): Service name
            username (str): Username
            password (str): Password
            url (str, optional): Service URL
            notes (str, optional): Additional notes
        """
        self.passwords[service] = {
            "username": username,
            "password": password,
            "url": url,
            "notes": notes,
            "history": [password]
        }
        self.save_database()

    def get_password(self, service):
        """Get password entry for a service.
        
        Args:
            service (str): Service name
        
        Returns:
            dict: Password entry
        
        Raises:
            KeyError: If service not found
        """
        return self.passwords[service]

    def update_password(self, service, **kwargs):
        """Update password entry.
        
        Args:
            service (str): Service name
            **kwargs: Fields to update
        
        Raises:
            KeyError: If service not found
        """
        if service not in self.passwords:
            raise KeyError(f"Service '{service}' not found")
        
        entry = self.passwords[service]
        for key, value in kwargs.items():
            if key == 'password':
                entry['history'].append(value)
            entry[key] = value
        
        self.save_database()

    def delete_password(self, service):
        """Delete password entry.
        
        Args:
            service (str): Service name
        
        Raises:
            KeyError: If service not found
        """
        del self.passwords[service]
        self.save_database()

    def list_services(self):
        """List all services.
        
        Returns:
            list: List of service names
        """
        return list(self.passwords.keys())

    def search_passwords(self, **kwargs):
        """Search password entries.
        
        Args:
            **kwargs: Search criteria
        
        Returns:
            list: Matching entries
        """
        results = []
        for service, entry in self.passwords.items():
            if all(entry.get(k) == v for k, v in kwargs.items()):
                results.append({"service": service, **entry})
        return results

    def get_password_history(self, service):
        """Get password history for a service.
        
        Args:
            service (str): Service name
        
        Returns:
            list: Password history
        
        Raises:
            KeyError: If service not found
        """
        return self.passwords[service]["history"]

    def save_database(self):
        """Save password database to file."""
        data = json.dumps(self.passwords)
        encrypted_data = self.encryptor.encrypt(data)
        with open(self.storage_file, 'wb') as f:
            f.write(encrypted_data)

    def load_database(self):
        """Load password database from file."""
        try:
            with open(self.storage_file, 'rb') as f:
                encrypted_data = f.read()
            decrypted_data = self.encryptor.decrypt(encrypted_data)
            self.passwords = json.loads(decrypted_data)
        except Exception as e:
            # Initialize empty database if loading fails
            self.passwords = {}
            self.save_database()

    def export_database(self, filename):
        """Export database to file.
        
        Args:
            filename (str): Export file path
        """
        with open(filename, 'w') as f:
            json.dump(self.passwords, f, indent=4)

    def import_database(self, filename):
        """Import database from file.
        
        Args:
            filename (str): Import file path
        """
        with open(filename, 'r') as f:
            self.passwords = json.load(f)
        self.save_database()
