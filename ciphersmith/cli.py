"""Command-line interface for CipherSmith."""

import os
import sys
from pathlib import Path

from .password_generator import PasswordGenerator
from .storage import PasswordStorage

class CLI:
    """Command-line interface for CipherSmith."""

    def __init__(self, storage):
        """Initialize CLI with storage.
        
        Args:
            storage (PasswordStorage): Password storage instance
        """
        self.storage = storage
        self.generator = PasswordGenerator()

    def add_password(self):
        """Add a new password entry."""
        service = input("Enter service name: ")
        username = input("Enter username: ")
        password = input("Enter password (or press enter to generate): ")
        url = input("Enter URL (optional): ")
        notes = input("Enter notes (optional): ")

        if not password:
            password = self.generator.generate()
            print(f"Generated password: {password}")

        self.storage.add_password(service, username, password, url, notes)
        print(f"Password for {service} has been saved.")

    def get_password(self):
        """Retrieve a password entry."""
        service = input("Enter service name: ")
        try:
            entry = self.storage.get_password(service)
            print("\nPassword Entry:")
            print(f"Service: {service}")
            print(f"Username: {entry['username']}")
            print(f"Password: {entry['password']}")
            if entry['url']:
                print(f"URL: {entry['url']}")
            if entry['notes']:
                print(f"Notes: {entry['notes']}")
        except KeyError:
            print(f"No password found for service: {service}")

    def update_password(self):
        """Update a password entry."""
        service = input("Enter service name: ")
        try:
            new_password = input("Enter new password (or press enter to generate): ")
            if not new_password:
                new_password = self.generator.generate()
                print(f"Generated password: {new_password}")
            
            self.storage.update_password(service, password=new_password)
            print(f"Password for {service} has been updated.")
        except KeyError:
            print(f"No password found for service: {service}")

    def delete_password(self):
        """Delete a password entry."""
        service = input("Enter service name: ")
        try:
            confirm = input(f"Are you sure you want to delete password for {service}? (y/n): ")
            if confirm.lower() == 'y':
                self.storage.delete_password(service)
                print(f"Password for {service} has been deleted.")
        except KeyError:
            print(f"No password found for service: {service}")

    def list_services(self):
        """List all services."""
        services = self.storage.list_services()
        if services:
            print("\nStored Services:")
            for service in services:
                print(f"- {service}")
        else:
            print("No passwords stored.")

    def generate_password(self):
        """Generate a new password."""
        length = int(input("Enter password length (default 12): ") or "12")
        include_letters = input("Include letters? (y/n, default y): ").lower() != 'n'
        include_numbers = input("Include numbers? (y/n, default y): ").lower() != 'n'
        include_special = input("Include special characters? (y/n, default y): ").lower() != 'n'

        password = self.generator.generate(
            length=length,
            letters=include_letters,
            numbers=include_numbers,
            special_chars=include_special
        )
        print(f"\nGenerated password: {password}")

    def search_passwords(self):
        """Search password entries."""
        query = input("Enter search term: ")
        results = self.storage.search_passwords(username=query)
        results.extend(self.storage.search_passwords(service=query))

        if results:
            print("\nSearch Results:")
            for entry in results:
                print(f"\nService: {entry['service']}")
                print(f"Username: {entry['username']}")
                print(f"Password: {entry['password']}")
                if entry['url']:
                    print(f"URL: {entry['url']}")
        else:
            print("No matching entries found.")

    def export_database(self):
        """Export password database."""
        filename = input("Enter export file name: ")
        self.storage.export_database(filename)
        print(f"Database exported to {filename}")

    def import_database(self):
        """Import password database."""
        filename = input("Enter import file name: ")
        try:
            self.storage.import_database(filename)
            print("Database imported successfully.")
        except Exception as e:
            print(f"Error importing database: {e}")

    def run(self):
        """Run the CLI interface."""
        commands = {
            '1': ('Add Password', self.add_password),
            '2': ('Get Password', self.get_password),
            '3': ('Update Password', self.update_password),
            '4': ('Delete Password', self.delete_password),
            '5': ('List Services', self.list_services),
            '6': ('Generate Password', self.generate_password),
            '7': ('Search Passwords', self.search_passwords),
            '8': ('Export Database', self.export_database),
            '9': ('Import Database', self.import_database),
            '0': ('Exit', None)
        }

        while True:
            print("\nCipherSmith Password Manager")
            print("=" * 30)
            for key, (name, _) in commands.items():
                print(f"{key}. {name}")

            choice = input("\nEnter your choice: ")
            if choice == '0':
                break
            elif choice in commands:
                try:
                    commands[choice][1]()
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Invalid choice. Please try again.")

def main():
    """Main entry point for CipherSmith CLI."""
    # Create default storage directory if it doesn't exist
    storage_dir = Path.home() / '.ciphersmith'
    storage_dir.mkdir(exist_ok=True)
    
    # Initialize storage with default database and key paths
    db_path = storage_dir / 'passwords.db'
    key_path = storage_dir / 'master.key'
    storage = PasswordStorage(str(db_path), str(key_path))
    
    # Run CLI
    cli = CLI(storage)
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\nExiting CipherSmith...")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
