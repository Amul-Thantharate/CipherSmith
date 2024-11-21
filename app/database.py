import sqlite3
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional, Any, Union


class PasswordDatabase:
    def __init__(self, db_path: Optional[str] = None):
        """Initialize the database with the given path or default to user's home directory."""
        if db_path is None:
            home = Path.home()
            db_path = str(home / ".secure_passgen" / "passwords.db")
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)

        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        """Initialize the database schema."""
        cursor = self.conn.cursor()
        cursor.executescript(
            """
            CREATE TABLE IF NOT EXISTS password_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                length INTEGER NOT NULL,
                config TEXT,
                description TEXT,
                tags TEXT
            );
            
            CREATE INDEX IF NOT EXISTS idx_created_at ON password_history(created_at);
            CREATE INDEX IF NOT EXISTS idx_password_hash ON password_history(password_hash);
        """
        )
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        if hasattr(self, "conn"):
            self.conn.close()

    def add_password(
        self,
        password_hash: str,
        length: int,
        config: Dict[str, Any],
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> int:
        """Add a password entry to the database."""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO password_history 
            (password_hash, length, config, description, tags)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                password_hash,
                length,
                json.dumps(config),
                description,
                json.dumps(tags) if tags else None,
            ),
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_password_history(
        self,
        limit: Optional[int] = None,
        tag: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Get password history with optional limit and tag filter."""
        cursor = self.conn.cursor()
        query = "SELECT * FROM password_history"
        params = []

        if tag:
            query += " WHERE tags LIKE ?"
            params.append(f'%"{tag}"%')

        query += " ORDER BY created_at DESC"

        if limit:
            query += " LIMIT ?"
            params.append(limit)

        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]

    def get_all_tags(self) -> List[str]:
        """Get all unique tags used in the database."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT DISTINCT tags FROM password_history WHERE tags IS NOT NULL"
        )

        all_tags = set()
        for row in cursor.fetchall():
            tags = json.loads(row["tags"])
            all_tags.update(tags)

        return sorted(list(all_tags))

    def search_passwords(self, query: str) -> List[Dict[str, Any]]:
        """Search passwords by description or tags."""
        cursor = self.conn.cursor()
        # Make search case-insensitive and search in both description and tags
        cursor.execute(
            """
            SELECT * FROM password_history 
            WHERE LOWER(description) LIKE LOWER(?) 
               OR LOWER(tags) LIKE LOWER(?) 
               OR EXISTS (
                   SELECT 1 
                   FROM json_each(tags) 
                   WHERE LOWER(value) LIKE LOWER(?)
               )
            ORDER BY created_at DESC
            """,
            (f"%{query}%", f"%{query}%", f"%{query}%"),
        )
        return [dict(row) for row in cursor.fetchall()]

    def delete_password(self, entry_id: int) -> bool:
        """Delete a password entry by ID."""
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM password_history WHERE id = ?",
            (entry_id,),
        )
        self.conn.commit()
        return cursor.rowcount > 0

    def clear_history(self, days: Optional[int] = None):
        """Clear password history. If days is provided, only clear entries older than that."""
        cursor = self.conn.cursor()
        if days is not None:
            cutoff = datetime.now() - timedelta(days=days)
            cursor.execute(
                "DELETE FROM password_history WHERE created_at < ?",
                (cutoff.isoformat(),),
            )
        else:
            cursor.execute("DELETE FROM password_history")
        self.conn.commit()

    def get_stats(self) -> Dict[str, Any]:
        """Get password generation statistics."""
        cursor = self.conn.cursor()

        # Get basic stats
        cursor.execute(
            """
            SELECT 
                COUNT(*) as total,
                AVG(length) as avg_length
            FROM password_history
        """
        )
        basic_stats = dict(cursor.fetchone())

        # Get tag counts
        cursor.execute("SELECT tags FROM password_history WHERE tags IS NOT NULL")
        tag_counts = {}
        for row in cursor.fetchall():
            tags = json.loads(row["tags"])
            for tag in tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        # Get daily generation counts for the last week
        cursor.execute(
            """
            SELECT DATE(created_at) as day, COUNT(*) as count
            FROM password_history
            WHERE created_at >= DATE('now', '-7 days')
            GROUP BY DATE(created_at)
            ORDER BY day DESC
        """
        )
        daily_counts = {row["day"]: row["count"] for row in cursor.fetchall()}

        return {
            "total_passwords": basic_stats["total"],
            "avg_length": round(basic_stats["avg_length"], 1),
            "popular_tags": dict(
                sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:5]
            ),
            "daily_generation": daily_counts,
        }
