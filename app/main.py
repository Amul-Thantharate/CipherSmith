import typer
import secrets
import random
import string
from pathlib import Path
from colorama import Fore, Style, init
import hashlib
from typing import List, Optional
from .database import PasswordDatabase
from rich.console import Console
from rich.table import Table
from datetime import datetime
import json

init(autoreset=True)
app = typer.Typer(
    help="Advanced Password Generator with validation and enhanced options."
)
console = Console()
db = PasswordDatabase()


def validate_password_length(
    numbers, lowercase, uppercase, special_chars, total_length
):
    """Validate the provided password length parameters."""
    # Convert any OptionInfo objects to their values
    total_length = (
        total_length.value if hasattr(total_length, "value") else total_length
    )
    numbers = numbers.value if hasattr(numbers, "value") else numbers
    lowercase = lowercase.value if hasattr(lowercase, "value") else lowercase
    uppercase = uppercase.value if hasattr(uppercase, "value") else uppercase
    special_chars = (
        special_chars.value if hasattr(special_chars, "value") else special_chars
    )

    if total_length:
        return total_length >= 4
    return sum([numbers, lowercase, uppercase, special_chars]) >= 4


@app.callback()
def callback():
    """
    Secure Password Generator CLI - Generate strong passwords with customizable options.
    """
    pass


@app.command()
def generate(
    total_length: int = typer.Option(
        None,
        "-t",
        "--total-length",
        help="Total password length. Overrides individual counts and generates a fully random password.",
    ),
    exclude_similar: bool = typer.Option(
        False,
        "-e",
        "--exclude-similar",
        help="Exclude similar characters (e.g., 'O', '0', 'I', 'l') for better readability.",
    ),
    amount: int = typer.Option(
        1, "-a", "--amount", help="Number of passwords to generate."
    ),
    numbers: int = typer.Option(
        0, "-n", "--numbers", help="Number of digits in the password."
    ),
    lowercase: int = typer.Option(
        0, "-l", "--lowercase", help="Number of lowercase characters in the password."
    ),
    uppercase: int = typer.Option(
        0, "-u", "--uppercase", help="Number of uppercase characters in the password."
    ),
    special_chars: int = typer.Option(
        0, "-s", "--special-chars", help="Number of special characters in the password."
    ),
    no_specials: bool = typer.Option(
        False,
        "--no-specials",
        help="Exclude special characters from the random pool when using --total-length.",
    ),
    output_file: Path = typer.Option(
        None,
        "-o",
        "--output-file",
        help="File to save the generated passwords. If not provided, passwords are printed to stdout.",
    ),
    description: str = typer.Option(
        None,
        "-d",
        "--description",
        help="Description of what this password is for.",
    ),
    tags: List[str] = typer.Option(
        None,
        "--tag",
        help="Tags to categorize the password (can be used multiple times).",
    ),
    verbose: bool = typer.Option(
        False, "-v", "--verbose", help="Show detailed output for debugging."
    ),
    save_history: bool = typer.Option(
        True, "--no-history", help="Don't save to password history.", is_flag=True
    ),
):
    """Generate secure passwords with customizable rules and advanced options."""
    # Convert OptionInfo objects to their values if needed
    total_length = (
        total_length.value if hasattr(total_length, "value") else total_length
    )
    numbers = numbers.value if hasattr(numbers, "value") else numbers
    lowercase = lowercase.value if hasattr(lowercase, "value") else lowercase
    uppercase = uppercase.value if hasattr(uppercase, "value") else uppercase
    special_chars = (
        special_chars.value if hasattr(special_chars, "value") else special_chars
    )

    # Set default values if no specific parameters are provided
    if not any([total_length, numbers, lowercase, uppercase, special_chars]):
        total_length = 12  # Default password length

    # Custom character pools
    base_digits = "23456789" if exclude_similar else string.digits
    base_lowercase = (
        "abcdefghjkmnpqrstuvwxyz" if exclude_similar else string.ascii_lowercase
    )
    base_uppercase = (
        "ABCDEFGHJKLMNPQRSTUVWXYZ" if exclude_similar else string.ascii_uppercase
    )
    base_specials = "!@#$%^&*()-_=+[]{}|;:,.<>?/~" if not no_specials else ""

    if total_length:
        # For total_length mode, adjust the pool based on no_specials
        pool = base_digits + base_lowercase + base_uppercase
        if not no_specials:
            pool += base_specials

        if not pool:
            console.print(
                "[red]No valid characters available for generating passwords!"
            )
            raise typer.Exit(code=1)
    else:
        if not validate_password_length(
            numbers, lowercase, uppercase, special_chars, total_length
        ):
            console.print(
                "[red]Invalid configuration! Ensure total length or the sum of individual counts is at least 4."
            )
            raise typer.Exit(code=1)

    passwords = []
    try:
        for _ in range(amount):
            if total_length:
                # Generate fully random password using the specified total length
                password = "".join(secrets.choice(pool) for _ in range(total_length))
            else:
                # Build password using specified counts
                password_parts = (
                    [secrets.choice(base_digits) for _ in range(numbers)]
                    + [secrets.choice(base_lowercase) for _ in range(lowercase)]
                    + [secrets.choice(base_uppercase) for _ in range(uppercase)]
                    + [secrets.choice(base_specials) for _ in range(special_chars)]
                )
                random.shuffle(password_parts)
                password = "".join(password_parts)

            passwords.append(password)

            if save_history:
                # Save to database with hash
                password_hash = hashlib.sha256(password.encode()).hexdigest()
                config = {
                    "exclude_similar": exclude_similar,
                    "no_specials": no_specials,
                    "composition": {
                        "total_length": total_length,
                        "numbers": numbers,
                        "lowercase": lowercase,
                        "uppercase": uppercase,
                        "special_chars": special_chars,
                    },
                }
                db.add_password(
                    password_hash=password_hash,
                    length=len(password),
                    config=json.dumps(config),
                    description=description,
                    tags=tags,
                )

        # Output results
        if output_file:
            output_file.write_text("\n".join(passwords))
            if verbose:
                console.print(f"[green]Passwords saved to {output_file}")
        else:
            for password in passwords:
                console.print(f"[cyan]{password}")

        if verbose:
            console.print("[green]Password generation completed successfully!")

        return passwords

    except Exception as e:
        console.print(f"[red]Error generating passwords: {str(e)}")
        raise typer.Exit(code=1)


@app.command()
def history(
    limit: int = typer.Option(10, "-n", "--limit", help="Number of entries to show"),
    tag: str = typer.Option(None, "-t", "--tag", help="Filter by tag"),
):
    """View password generation history."""
    entries = db.get_password_history(limit=limit, tag=tag)

    if not entries:
        console.print("[yellow]No password history found.")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date")
    table.add_column("Length")
    table.add_column("Description")
    table.add_column("Tags")

    for entry in entries:
        created_at = datetime.fromisoformat(entry["created_at"]).strftime(
            "%Y-%m-%d %H:%M"
        )
        tags = ", ".join(json.loads(entry["tags"])) if entry["tags"] else ""
        table.add_row(
            created_at, str(entry["length"]), entry["description"] or "", tags
        )

    console.print(table)


@app.command()
def stats():
    """Show password generation statistics."""
    stats = db.get_stats()

    console.print("\n[bold cyan]Password Generation Statistics[/]\n")

    console.print(f"[bold]Total Passwords Generated:[/] {stats['total_passwords']}")
    console.print(f"[bold]Average Password Length:[/] {stats['avg_length']}")

    if stats["popular_tags"]:
        console.print("\n[bold]Most Used Tags:[/]")
        for tag, count in stats["popular_tags"].items():
            console.print(f"  {tag}: {count}")

    if stats["daily_generation"]:
        console.print("\n[bold]Recent Daily Generation:[/]")
        for day, count in stats["daily_generation"].items():
            console.print(f"  {day}: {count} passwords")


@app.command()
def clear(
    days: int = typer.Option(
        None,
        "-d",
        "--days",
        help="Clear entries older than specified days. If not provided, clears all history.",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Skip confirmation prompt.",
    ),
):
    """Clear password generation history."""
    if not force:
        msg = (
            "all password history"
            if days is None
            else f"password history older than {days} days"
        )
        if not typer.confirm(f"Are you sure you want to clear {msg}?"):
            raise typer.Abort()

    db.clear_history(days)
    console.print("[green]Password history cleared successfully!")


@app.command()
def search(
    query: str = typer.Argument(
        ..., help="Search query to find passwords by description or tags"
    ),
    limit: int = typer.Option(10, "-n", "--limit", help="Number of entries to show"),
):
    """
    Search password history by description or tags.
    """
    try:
        results = db.search_passwords(query)
        if not results:
            console.print(f"[yellow]No passwords found matching '{query}'[/yellow]")
            return

        table = Table(title=f"Search Results for '{query}'")
        table.add_column("Date", style="cyan")
        table.add_column("Length", style="blue")
        table.add_column("Description", style="green")
        table.add_column("Tags", style="magenta")

        for entry in results[:limit]:
            created_at = datetime.fromisoformat(entry["created_at"]).strftime(
                "%Y-%m-%d %H:%M"
            )
            tags = json.loads(entry["tags"]) if entry["tags"] else []
            tags_str = ", ".join(tags) if tags else ""

            table.add_row(
                created_at, str(entry["length"]), entry["description"] or "", tags_str
            )

        console.print(table)
        if len(results) > limit:
            console.print(
                f"\n[yellow]Showing {limit} of {len(results)} results. Use --limit to see more.[/yellow]"
            )

    except Exception as e:
        console.print(f"[red]Error searching passwords: {str(e)}[/red]")


@app.command()
def delete(
    entry_id: int = typer.Argument(..., help="ID of the password entry to delete"),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Skip confirmation prompt.",
    ),
):
    """
    Delete a specific password entry by ID.
    """
    try:
        # First show the entry to be deleted
        cursor = db.conn.cursor()
        cursor.execute("SELECT * FROM password_history WHERE id = ?", (entry_id,))
        entry = cursor.fetchone()

        if not entry:
            console.print(f"[red]No password entry found with ID {entry_id}[/red]")
            raise typer.Exit(1)

        # Show entry details
        table = Table(title=f"Password Entry #{entry_id}")
        table.add_column("Date", style="cyan")
        table.add_column("Length", style="blue")
        table.add_column("Description", style="green")
        table.add_column("Tags", style="magenta")

        created_at = datetime.fromisoformat(entry["created_at"]).strftime(
            "%Y-%m-%d %H:%M"
        )
        tags = json.loads(entry["tags"]) if entry["tags"] else []
        tags_str = ", ".join(tags) if tags else ""

        table.add_row(
            created_at, str(entry["length"]), entry["description"] or "", tags_str
        )

        console.print(table)

        # Delete the entry if forced or confirmed
        if force or typer.confirm(
            "Are you sure you want to delete this password entry?", default=False
        ):
            if db.delete_password(entry_id):
                console.print(
                    f"[green]Successfully deleted password entry #{entry_id}[/green]"
                )
            else:
                console.print(f"[red]Failed to delete password entry #{entry_id}[/red]")
                raise typer.Exit(1)
        else:
            console.print("[yellow]Deletion cancelled[/yellow]")

    except Exception as e:
        console.print(f"[red]Error deleting password: {str(e)}[/red]")
        raise typer.Exit(1)


def main():
    app()


if __name__ == "__main__":
    main()
