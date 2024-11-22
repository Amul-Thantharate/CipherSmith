import click
from datetime import datetime
from ..database import PasswordDatabase

@click.command()
@click.option('--limit', '-l', type=int, help='Limit the number of entries to show')
@click.option('--tag', '-t', help='Filter entries by tag')
def history(limit: int, tag: str):
    """Show password generation history."""
    db = PasswordDatabase()
    try:
        history_entries = db.get_password_history(limit=limit, tag=tag)
        if not history_entries:
            click.echo("No history entries found.")
            return

        for entry in history_entries:
            created_at = datetime.fromisoformat(entry['created_at']).strftime('%Y-%m-%d %H:%M:%S')
            config = entry.get('config', '{}')
            description = entry.get('description', '')
            tags = entry.get('tags', '[]')
            
            click.echo(f"\n{created_at} - Length: {entry['length']}")
            if description:
                click.echo(f"Description: {description}")
            if tags != '[]':
                click.echo(f"Tags: {tags}")
            click.echo(f"Config: {config}")
            click.echo("-" * 50)
    except Exception as e:
        click.echo(f"Error retrieving password history: {str(e)}", err=True)
    finally:
        db.close()
