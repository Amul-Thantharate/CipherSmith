import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from ciphersmith.cli import CLI
from ciphersmith.storage import PasswordStorage

class TestCLI(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = PasswordStorage("test_passwords.json", "test_key.key")
        self.cli = CLI(self.storage)
        
        # Test data
        self.test_service = "testservice"
        self.test_entry = {
            "username": "testuser",
            "password": "TestPass123!",
            "url": "https://test.com",
            "notes": "Test account"
        }

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_password(self, mock_stdout):
        """Test adding password through CLI"""
        with patch('builtins.input', side_effect=[
            self.test_service,
            self.test_entry["username"],
            self.test_entry["password"],
            self.test_entry["url"],
            self.test_entry["notes"]
        ]):
            self.cli.add_password()
        
        # Verify password was added
        stored_entry = self.storage.get_password(self.test_service)
        self.assertEqual(stored_entry["username"], self.test_entry["username"])
        self.assertEqual(stored_entry["password"], self.test_entry["password"])

    @patch('sys.stdout', new_callable=StringIO)
    def test_get_password(self, mock_stdout):
        """Test retrieving password through CLI"""
        # Add test password
        self.storage.add_password(self.test_service, **self.test_entry)
        
        with patch('builtins.input', return_value=self.test_service):
            self.cli.get_password()
        
        output = mock_stdout.getvalue()
        self.assertIn(self.test_entry["username"], output)
        self.assertIn(self.test_entry["password"], output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_services(self, mock_stdout):
        """Test listing services through CLI"""
        # Add multiple test entries
        test_services = ["service1", "service2", "service3"]
        for service in test_services:
            self.storage.add_password(service, **self.test_entry)
        
        self.cli.list_services()
        
        output = mock_stdout.getvalue()
        for service in test_services:
            self.assertIn(service, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_password(self, mock_stdout):
        """Test updating password through CLI"""
        # Add initial password
        self.storage.add_password(self.test_service, **self.test_entry)
        
        new_password = "NewPass456@"
        with patch('builtins.input', side_effect=[self.test_service, new_password]):
            self.cli.update_password()
        
        # Verify password was updated
        updated_entry = self.storage.get_password(self.test_service)
        self.assertEqual(updated_entry["password"], new_password)

    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_password(self, mock_stdout):
        """Test deleting password through CLI"""
        # Add password to delete
        self.storage.add_password(self.test_service, **self.test_entry)
        
        with patch('builtins.input', side_effect=[self.test_service, 'y']):
            self.cli.delete_password()
        
        # Verify password was deleted
        with self.assertRaises(KeyError):
            self.storage.get_password(self.test_service)

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_password(self, mock_stdout):
        """Test password generation through CLI"""
        with patch('builtins.input', side_effect=['16', 'y', 'y', 'y']):
            self.cli.generate_password()
        
        output = mock_stdout.getvalue()
        generated_password = output.strip().split('\n')[-1]
        self.assertEqual(len(generated_password), 16)
        self.assertTrue(any(c.isupper() for c in generated_password))
        self.assertTrue(any(c.islower() for c in generated_password))
        self.assertTrue(any(c.isdigit() for c in generated_password))

    @patch('sys.stdout', new_callable=StringIO)
    def test_search_passwords(self, mock_stdout):
        """Test searching passwords through CLI"""
        # Add test entries
        self.storage.add_password("gmail", username="test@gmail.com", password="pass1")
        self.storage.add_password("yahoo", username="test@yahoo.com", password="pass2")
        
        with patch('builtins.input', return_value="gmail"):
            self.cli.search_passwords()
        
        output = mock_stdout.getvalue()
        self.assertIn("gmail", output)
        self.assertIn("test@gmail.com", output)
        self.assertNotIn("yahoo", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_export_import(self, mock_stdout):
        """Test database export/import through CLI"""
        # Add test data
        self.storage.add_password(self.test_service, **self.test_entry)
        
        export_file = "cli_export_test.json"
        with patch('builtins.input', return_value=export_file):
            self.cli.export_database()
        
        # Clear storage
        self.storage = PasswordStorage("new_test_passwords.json", "new_test_key.key")
        self.cli = CLI(self.storage)
        
        # Import database
        with patch('builtins.input', return_value=export_file):
            self.cli.import_database()
        
        # Verify imported data
        imported_entry = self.storage.get_password(self.test_service)
        self.assertEqual(imported_entry["username"], self.test_entry["username"])
        self.assertEqual(imported_entry["password"], self.test_entry["password"])

if __name__ == '__main__':
    unittest.main()
