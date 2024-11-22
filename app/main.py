import os
import secrets
import string
import typer
from rich.console import Console
from rich.table import Table
from datetime import datetime
from typing import List, Optional
from app.database import PasswordDatabase
from app.password_strength import PasswordStrengthAnalyzer
from colorama import Fore, Style, init
from pathlib import Path
import hashlib
import json

init(autoreset=True)
app = typer.Typer(
    help="Advanced Password Generator with validation and enhanced options."
)
console = Console()

# Initialize database lazily to allow mocking in tests
db = None

def get_db():
    global db
    if db is None:
        db = PasswordDatabase()
    return db

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
            console.print("[red]Invalid configuration! Total length or sum of counts must be at least 1.")
            raise typer.Exit(code=0)
        
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
                get_db().add_password(
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
        raise typer.Exit(code=0)

@app.command()
def check(
    password: str = typer.Argument(..., help="Password to analyze"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed analysis"),
):
    """Analyze password strength with detailed feedback."""
    try:
        analyzer = PasswordStrengthAnalyzer()
        analysis = analyzer.analyze(password)
        
        # Display basic strength info
        console.print(f"\n[bold]Password Strength Analysis:[/bold]")
        console.print(f"Score: {analysis.score}/4")
        console.print(f"Crack Time: {analysis.crack_time_seconds:.2f} seconds")
        console.print(f"Feedback: {', '.join(analysis.feedback)}")
        
        if verbose:
            console.print("\n[bold]Additional Details:[/bold]")
            console.print(f"Length: {len(password)}")
            console.print(f"Patterns Found: {', '.join(analysis.patterns_found) if analysis.patterns_found else 'None'}")
            console.print(f"Suggestions: {', '.join(analysis.suggestions) if analysis.suggestions else 'None'}")
    
    except Exception as e:
        console.print(f"[red]Error analyzing password: {str(e)}")
        raise typer.Exit(code=0)

@app.command()
def history(
    limit: int = typer.Option(10, "-n", "--limit", help="Number of entries to show"),
    tag: str = typer.Option(None, "-t", "--tag", help="Filter by tag"),
):
    """View password generation history."""
    try:
        entries = get_db().get_password_history(limit=limit, tag=tag)
        table = Table(title="Password Generation History")
        table.add_column("ID", justify="right", style="cyan")
        table.add_column("Date", style="magenta")
        table.add_column("Length", justify="right", style="green")
        table.add_column("Description", style="blue")
        table.add_column("Tags", style="yellow")
        
        if entries:
            for entry in entries:
                created_at = datetime.fromisoformat(entry['created_at'])
                tags = json.loads(entry['tags']) if entry['tags'] else []
                table.add_row(
                    str(entry['id']),
                    created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    str(entry['length']),
                    entry['description'] or "",
                    ", ".join(tags) if tags else "",
                )
        console.print(table)
        return

    except Exception as e:
        console.print(f"[red]Error retrieving password history: {str(e)}")
        raise typer.Exit(code=1)

@app.command()
def stats():
    """Show password generation statistics."""
    try:
        stats = get_db().get_stats()
        table = Table(title="Password Generation Statistics")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")

        table.add_row("Total Passwords Generated", str(stats["total_passwords"]))
        table.add_row("Average Password Length", f"{stats['avg_length']:.1f}")
        table.add_row("Most Common Length", str(stats["most_common_length"]))
        table.add_row(
            "Last Generated",
            stats["last_generated"].strftime("%Y-%m-%d %H:%M:%S") if stats["last_generated"] else "Never"
        )

        console.print(table)
        return

    except Exception as e:
        console.print(f"[red]Error retrieving statistics: {str(e)}")
        raise typer.Exit(code=0)

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

        count = get_db().clear_history(days=days)
        console.print(f"[green]Cleared {count} entries from history.")

    except typer.Abort:
        console.print("[yellow]Operation cancelled.")
    except Exception as e:
        console.print(f"[red]Error clearing history: {str(e)}")
        raise typer.Exit(code=0)

@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
    limit: int = typer.Option(10, "-n", "--limit", help="Number of entries to show"),
):
    """Search password history by description or tags."""
    try:
        entries = get_db().search_passwords(query, limit=limit)
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
        raise typer.Exit(code=0)

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
        entry = get_db().get_password(entry_id)
        if not entry:
            console.print(f"[yellow]No entry found with ID {entry_id}")
            raise typer.Exit(code=0)

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

        get_db().delete_password(entry_id)
        console.print(f"[green]Successfully deleted entry {entry_id}")

    except typer.Abort:
        console.print("[yellow]Operation cancelled.")
    except Exception as e:
        console.print(f"[red]Error deleting entry: {str(e)}")
        raise typer.Exit(code=0)

def validate_password_length(numbers=0, lowercase=0, uppercase=0, special_chars=0, total_length=None):
    """Validate the provided password length parameters."""
    # Convert any typer.models.OptionInfo to their values
    total_length = total_length.value if hasattr(total_length, "value") else total_length
    numbers = numbers.value if hasattr(numbers, "value") else numbers
    lowercase = lowercase.value if hasattr(lowercase, "value") else lowercase
    uppercase = uppercase.value if hasattr(uppercase, "value") else uppercase
    special_chars = special_chars.value if hasattr(special_chars, "value") else special_chars

    if total_length is not None:
        if total_length < 1:  
            console.print("[red]Password length must be at least 1 character.")
            return False  
        return True
    
    component_sum = numbers + lowercase + uppercase + special_chars
    if component_sum < 1:  
        console.print("[red]Total length must be at least 1 character.")
        return False  
    
    return True

if __name__ == "__main__":
    app()
