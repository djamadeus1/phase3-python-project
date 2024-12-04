import sqlite3
import os

DB_PATH = os.path.join("lib", "trivia.db") 

CONN = sqlite3.connect(DB_PATH)
CURSOR = CONN.cursor()

class Category:
    def __init__(self, name, id=None):
        self.id = id
        self._name = name

    @property
    def name(self):
        """Getter for category name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for category name with validation."""
        if not value.strip():
            raise ValueError("Category name cannot be empty.")
        self._name = value

    @classmethod
    def create_table(cls):
        """Create the categories table in the database."""
        try:
            CURSOR.execute(
                """
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE
                );
                """
            )
        except Exception as e:
            print(f"Error creating table: {e}")

    def save(self):
        """Insert the current instance into the database."""
        try:
            CURSOR.execute(
                """
                INSERT INTO categories (name)
                VALUES (?);
                """,
                (self._name,),
            )
            CONN.commit()
            self.id = CURSOR.lastrowid
        except Exception as e:
            print(f"Error saving category: {e}")

    @classmethod
    def all(cls):
        """Fetch all categories from the database."""
        try:
            CURSOR.execute("SELECT * FROM categories;")
            rows = CURSOR.fetchall()
            return [cls(id=row[0], name=row[1]) for row in rows]
        except Exception as e:
            print(f"Error fetching all categories: {e}")
            return []

    @classmethod
    def find_by_id(cls, id):
        """Find a category by its ID."""
        try:
            CURSOR.execute("SELECT * FROM categories WHERE id = ?;", (id,))
            row = CURSOR.fetchone()
            if row:
                return cls(id=row[0], name=row[1])
        except Exception as e:
            print(f"Error finding category by ID: {e}")
        return None

    def delete(self):
        """Delete the current instance from the database."""
        try:
            CURSOR.execute(
                "DELETE FROM categories WHERE id = ?;", (self.id,)
            )
            CONN.commit()
        except Exception as e:
            print(f"Error deleting category: {e}")
