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
from .password_strength import check_password_strength, PasswordStrengthAnalyzer

init(autoreset=True)
app = typer.Typer(
    help="Advanced Password Generator with validation and enhanced options."
)
console = Console()
db = PasswordDatabase()

def validate_password_length(numbers, lowercase, uppercase, special_chars, total_length):
    """Validate the provided password length parameters."""
    total_length = total_length.value if hasattr(total_length, "value") else total_length
    numbers = numbers.value if hasattr(numbers, "value") else numbers
    lowercase = lowercase.value if hasattr(lowercase, "value") else lowercase
    uppercase = uppercase.value if hasattr(uppercase, "value") else uppercase
    special_chars = special_chars.value if hasattr(special_chars, "value") else special_chars

    if total_length:
        return total_length >= 4
    return sum([numbers, lowercase, uppercase, special_chars]) >= 4

@app.callback()
def callback():
    """Secure Password Generator CLI - Generate strong passwords with customizable options."""
    pass

@app.command()
def generate(
    total_length: int = typer.Option(
        None,
        "-t",
        "--total-length",
        help="Total password length. Overrides individual counts.",
    ),
    exclude_similar: bool = typer.Option(
        False,
        "-e",
        "--exclude-similar",
        help="Exclude similar characters (e.g., 'O', '0', 'I', 'l').",
    ),
    amount: int = typer.Option(
        1, "-a", "--amount", help="Number of passwords to generate."
    ),
    numbers: int = typer.Option(
        0, "-n", "--numbers", help="Number of digits in the password."
    ),
    lowercase: int = typer.Option(
        0, "-l", "--lowercase", help="Number of lowercase characters."
    ),
    uppercase: int = typer.Option(
        0, "-u", "--uppercase", help="Number of uppercase characters."
    ),
    special_chars: int = typer.Option(
        0, "-s", "--special-chars", help="Number of special characters."
    ),
    no_specials: bool = typer.Option(
        False,
        "--no-specials",
        help="Exclude special characters when using --total-length.",
    ),
    output_file: Path = typer.Option(
        None,
        "-o",
        "--output-file",
        help="File to save the generated passwords.",
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
        help="Tags to categorize the password.",
    ),
    verbose: bool = typer.Option(
        False, "-v", "--verbose", help="Show detailed output."
    ),
    save_history: bool = typer.Option(
        True, "--no-history", help="Don't save to password history.", is_flag=True
    ),
    check_strength: bool = typer.Option(
        False, "-c", "--check-strength", help="Analyze password strength after generation."
    ),
):
    """Generate secure passwords with customizable rules and options."""
    try:
        if not any([total_length, numbers, lowercase, uppercase, special_chars]):
            total_length = 12  # Default length

        if not validate_password_length(numbers, lowercase, uppercase, special_chars, total_length):
            console.print("[red]Invalid configuration! Total length or sum of counts must be at least 4.")
            raise typer.Exit(code=1)

        base_digits = "23456789" if exclude_similar else string.digits
        base_lowercase = "abcdefghjkmnpqrstuvwxyz" if exclude_similar else string.ascii_lowercase
        base_uppercase = "ABCDEFGHJKLMNPQRSTUVWXYZ" if exclude_similar else string.ascii_uppercase
        base_specials = "!@#$%^&*()-_=+[]{}|;:,.<>?/~" if not no_specials else ""

        passwords = []
        analyzer = PasswordStrengthAnalyzer() if check_strength else None

        for _ in range(amount):
            if total_length:
                pool = base_digits + base_lowercase + base_uppercase
                if not no_specials:
                    pool += base_specials
                password = "".join(secrets.choice(pool) for _ in range(total_length))
            else:
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

            if check_strength:
                console.print(f"\n[bold]Password: [cyan]{password}")
                analyzer.analyze(password)

        if output_file:
            output_file.write_text("\n".join(passwords))
            if verbose:
                console.print(f"[green]Passwords saved to {output_file}")
        else:
            if not check_strength:
                for password in passwords:
                    console.print(f"[cyan]{password}")

        if verbose:
            console.print("[green]Password generation completed successfully!")

        return passwords

    except Exception as e:
        console.print(f"[red]Error generating passwords: {str(e)}")
        raise typer.Exit(code=1)

@app.command()
def check(
    password: str = typer.Argument(..., help="Password to analyze"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed analysis"),
):
    """Analyze password strength with detailed feedback."""
    try:
        analysis = check_password_strength(password)
        if verbose:
            console.print("\n[bold]Additional Details:[/bold]")
            console.print(f"Patterns found: {', '.join(analysis.patterns_found) if analysis.patterns_found else 'None'}")
    except Exception as e:
        console.print(f"[red]Error analyzing password: {str(e)}")
        raise typer.Exit(code=1)

@app.command()
def history(
    limit: int = typer.Option(10, "-n", "--limit", help="Number of entries to show"),
    tag: str = typer.Option(None, "-t", "--tag", help="Filter by tag"),
):
    """View password generation history."""
    try:
        entries = db.get_history(limit=limit, tag=tag)
        if not entries:
            console.print("[yellow]No password history found.")
            return

        table = Table(title="Password Generation History")
        table.add_column("ID", justify="right", style="cyan")
        table.add_column("Date", style="magenta")
        table.add_column("Length", justify="right", style="green")
        table.add_column("Description", style="blue")
        table.add_column("Tags", style="yellow")

        for entry in entries:
            table.add_row(
                str(entry.id),
                entry.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                str(entry.length),
                entry.description or "",
                ", ".join(entry.tags) if entry.tags else "",
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error retrieving history: {str(e)}")
        raise typer.Exit(code=1)

@app.command()
def stats():
    """Show password generation statistics."""
    try:
        stats = db.get_stats()
        table = Table(title="Password Generation Statistics")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", justify="right", style="green")

        table.add_row("Total Passwords Generated", str(stats["total_passwords"]))
        table.add_row("Average Length", f"{stats['avg_length']:.1f}")
        table.add_row("Most Common Length", str(stats["most_common_length"]))
        table.add_row(
            "Most Recent Generation",
            stats["last_generated"].strftime("%Y-%m-%d %H:%M:%S")
            if stats["last_generated"]
            else "Never",
        )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error retrieving statistics: {str(e)}")
        raise typer.Exit(code=1)

@app.command()
def clear(
    days: int = typer.Option(
        None,
        "-d",
        "--days",
        help="Clear entries older than specified days.",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Skip confirmation prompt.",
    ),
):
    """Clear password generation history."""
    try:
        if not force:
            msg = "all password history" if days is None else f"password history older than {days} days"
            if not typer.confirm(f"Are you sure you want to clear {msg}?"):
                raise typer.Abort()

        count = db.clear_history(days=days)
        console.print(f"[green]Cleared {count} entries from history.")

    except typer.Abort:
        console.print("[yellow]Operation cancelled.")
    except Exception as e:
        console.print(f"[red]Error clearing history: {str(e)}")
        raise typer.Exit(code=1)

@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
    limit: int = typer.Option(10, "-n", "--limit", help="Number of entries to show"),
):
    """Search password history by description or tags."""
    try:
        entries = db.search_passwords(query, limit=limit)
        if not entries:
            console.print("[yellow]No matching entries found.")
            return

        table = Table(title=f"Search Results for '{query}'")
        table.add_column("ID", justify="right", style="cyan")
        table.add_column("Date", style="magenta")
        table.add_column("Length", justify="right", style="green")
        table.add_column("Description", style="blue")
        table.add_column("Tags", style="yellow")

        for entry in entries:
            table.add_row(
                str(entry.id),
                entry.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                str(entry.length),
                entry.description or "",
                ", ".join(entry.tags) if entry.tags else "",
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error searching passwords: {str(e)}")
        raise typer.Exit(code=1)

@app.command()
def delete(
    entry_id: int = typer.Argument(..., help="Entry ID to delete"),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Skip confirmation prompt.",
    ),
):
    """Delete a specific password entry."""
    try:
        entry = db.get_password(entry_id)
        if not entry:
            console.print(f"[yellow]No entry found with ID {entry_id}")
            raise typer.Exit(code=1)

        if not force:
            console.print("\nEntry details:")
            console.print(f"Date: {entry.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            console.print(f"Length: {entry.length}")
            if entry.description:
                console.print(f"Description: {entry.description}")
            if entry.tags:
                console.print(f"Tags: {', '.join(entry.tags)}")

            if not typer.confirm("\nAre you sure you want to delete this entry?"):
                raise typer.Abort()

        db.delete_password(entry_id)
        console.print(f"[green]Successfully deleted entry {entry_id}")

    except typer.Abort:
        console.print("[yellow]Operation cancelled.")
    except Exception as e:
        console.print(f"[red]Error deleting entry: {str(e)}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
