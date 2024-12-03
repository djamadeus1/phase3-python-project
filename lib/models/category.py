from models.__init__ import CURSOR,CONN

class Category:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

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
            # Check if the category already exists
            existing_category = Category.find_by_name(self.name)
            if existing_category:
                print(f"Category '{self.name}' already exists with ID: {existing_category.id}")
                return

            # If not, insert the new category
            CURSOR.execute(
                """
                INSERT INTO categories (name)
                VALUES (?);
                """,
                (self.name,),
            )
            CONN.commit()  # Commit the changes
            self.id = CURSOR.lastrowid  # Get the auto-generated ID
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
    def find_by_name(cls, name):
        """Find a category by its name."""
        try:
            CURSOR.execute(
                "SELECT * FROM categories WHERE name = ?;", (name,)
            )
            row = CURSOR.fetchone()
            if row:
                return cls(id=row[0], name=row[1])
        except Exception as e:
            print(f"Error finding category by name: {e}")
        return None

    def delete(self):
        """Delete the current instance from the database."""
        try:
            CURSOR.execute(
                "DELETE FROM categories WHERE id = ?;", (self.id,)
            )
            CONN.commit()  # Commit the deletion
        except Exception as e:
            print(f"Error deleting category: {e}")
