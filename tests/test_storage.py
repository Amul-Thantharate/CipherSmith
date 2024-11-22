import unittest
import os
import json
from ciphersmith.storage import PasswordStorage
from ciphersmith.encryption import Encryptor

class TestPasswordStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage_file = "test_passwords.json"
        self.key_file = "test_key.key"
        self.storage = PasswordStorage(self.storage_file, self.key_file)
        
        # Test data
        self.test_entries = {
            "google": {
                "username": "test@example.com",
                "password": "TestPass123!",
                "url": "https://google.com",
                "notes": "Test account"
            },
            "github": {
                "username": "testuser",
                "password": "GitPass456@",
                "url": "https://github.com",
                "notes": "Work account"
            }
        }

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.storage_file):
            os.remove(self.storage_file)
        if os.path.exists(self.key_file):
            os.remove(self.key_file)

    def test_add_password(self):
        """Test adding a new password entry"""
        service = "test_service"
        entry = {
            "username": "testuser",
            "password": "password123",
            "url": "https://test.com",
            "notes": "Test notes"
        }
        
        self.storage.add_password(service, **entry)
        stored_entry = self.storage.get_password(service)
        self.assertEqual(stored_entry["username"], entry["username"])
        self.assertEqual(stored_entry["password"], entry["password"])

    def test_update_password(self):
        """Test updating an existing password entry"""
        service = "test_service"
        original_entry = {
            "username": "testuser",
            "password": "password123",
            "url": "https://test.com",
            "notes": "Test notes"
        }
        
        # Add original entry
        self.storage.add_password(service, **original_entry)
        
        # Update password
        new_password = "newpassword456"
        self.storage.update_password(service, password=new_password)
        
        # Verify update
        updated_entry = self.storage.get_password(service)
        self.assertEqual(updated_entry["password"], new_password)
        self.assertEqual(updated_entry["username"], original_entry["username"])

    def test_delete_password(self):
        """Test deleting a password entry"""
        service = "test_service"
        entry = {
            "username": "testuser",
            "password": "password123",
            "url": "https://test.com",
            "notes": "Test notes"
        }
        
        # Add and then delete entry
        self.storage.add_password(service, **entry)
        self.storage.delete_password(service)
        
        # Verify deletion
        with self.assertRaises(KeyError):
            self.storage.get_password(service)

    def test_list_services(self):
        """Test listing all services"""
        # Add multiple entries
        for service, entry in self.test_entries.items():
            self.storage.add_password(service, **entry)
        
        # Get list of services
        services = self.storage.list_services()
        self.assertEqual(set(services), set(self.test_entries.keys()))

    def test_search_passwords(self):
        """Test searching password entries"""
        # Add test entries
        for service, entry in self.test_entries.items():
            self.storage.add_password(service, **entry)
        
        # Search by username
        results = self.storage.search_passwords(username="test@example.com")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["service"], "google")

    def test_export_import(self):
        """Test exporting and importing password database"""
        # Add test entries
        for service, entry in self.test_entries.items():
            self.storage.add_password(service, **entry)
        
        # Export database
        export_file = "export_test.json"
        self.storage.export_database(export_file)
        
        # Create new storage instance and import
        new_storage = PasswordStorage("new_storage.json", "new_key.key")
        new_storage.import_database(export_file)
        
        # Verify imported data
        for service in self.test_entries:
            original = self.storage.get_password(service)
            imported = new_storage.get_password(service)
            self.assertEqual(original, imported)
        
        # Clean up
        os.remove(export_file)
        os.remove("new_storage.json")
        os.remove("new_key.key")

    def test_password_history(self):
        """Test password history tracking"""
        service = "test_service"
        passwords = ["pass1", "pass2", "pass3"]
        
        # Add and update password multiple times
        for password in passwords:
            self.storage.add_password(service, username="testuser", password=password)
        
        # Check history
        history = self.storage.get_password_history(service)
        self.assertEqual(len(history), len(passwords))
        self.assertEqual(history[-1], passwords[-1])

if __name__ == '__main__':
    unittest.main()
