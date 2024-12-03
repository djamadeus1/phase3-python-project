import sqlite3
import random
import sys
sys.path.append("..")  # Add the parent directory to the Python path
from lib.models.category import Category


# Connect to the database
CONN = sqlite3.connect("trivia.db")
CURSOR = CONN.cursor()


class Question:
    def __init__(self, question_text, correct_answer, category_id, id=None):
        self.id = id
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.category_id = category_id

    @classmethod
    def create_table(cls):
        """Create the questions table in the database."""
        try:
            CURSOR.execute(
                """
                CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY,
                    question_text TEXT NOT NULL,
                    correct_answer TEXT NOT NULL,
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES categories(id)
                );
                """
            )
        except Exception as e:
            print(f"Error creating questions table: {e}")
    
    def save(self):
        """Insert the current instance into the database."""
        try:
            # Strip any existing prefixes (e.g., "A)") from the correct answer
            sanitized_correct_answer = self.correct_answer.split(") ", 1)[-1].strip()

            CURSOR.execute(
                """
                INSERT INTO questions (question_text, correct_answer, category_id)
                VALUES (?, ?, ?);
                """,
                (self.question_text, sanitized_correct_answer, self.category_id),
            )
            CONN.commit()  # Commit the changes
            self.id = CURSOR.lastrowid  # Get the auto-generated ID
        except Exception as e:
            print(f"Error saving question: {e}")


    @classmethod
    def all(cls):
        """Fetch all questions from the database."""
        try:
            CURSOR.execute("SELECT * FROM questions;")
            rows = CURSOR.fetchall()  # Use fetchall to get all rows
            return [
                cls(
                    id=row[0],
                    question_text=row[1],
                    correct_answer=row[2],
                    category_id=row[3]
                ) for row in rows
            ]
        except Exception as e:
            print(f"Error fetching all questions: {e}")
            return []

    @classmethod
    def find_by_category(cls, category_id):
        """Fetch one question from a specific category."""
        try:
            CURSOR.execute(
                "SELECT * FROM questions WHERE category_id = ? LIMIT 1;", (category_id,)
            )
            row = CURSOR.fetchone()
            if row:
                return cls(
                    id=row[0],
                    question_text=row[1],
                    correct_answer=row[2],
                    category_id=row[3]
                )
        except Exception as e:
            print(f"Error finding question by category: {e}")
        return None

    @classmethod
    def find_by_id(cls, id):
        """Find a question by its ID."""
        try:
            CURSOR.execute("SELECT * FROM questions WHERE id = ?;", (id,))
            row = CURSOR.fetchone()
            if row:
                return cls(
                    id=row[0],
                    question_text=row[1],
                    correct_answer=row[2],
                    category_id=row[3]
                )
        except Exception as e:
            print(f"Error finding question by ID: {e}")
        return None

    def delete(self):
        """Delete the current question from the database."""
        try:
            CURSOR.execute("DELETE FROM questions WHERE id = ?;", (self.id,))
            CONN.commit()  # Commit the deletion
            print(f"Question with ID {self.id} has been deleted.")
        except Exception as e:
            print(f"Error deleting question: {e}")

    def generate_choices(self):
        """Generate multiple-choice options including the correct answer."""
        sanitized_correct_answer = self.correct_answer.strip()

        # Generate plausible wrong answers
        incorrect_answers = self.get_plausible_wrong_answers()

        # Combine correct and incorrect answers
        all_choices = incorrect_answers + [sanitized_correct_answer]
        random.shuffle(all_choices)  # Shuffle to randomize positions

        # Return choices with letters
        choices_with_letters = {letter: choice for letter, choice in zip("ABCD", all_choices)}
        return choices_with_letters

    def get_plausible_wrong_answers(self):
        """Generate plausible wrong answers based on the correct answer."""
        if "miles" in self.correct_answer:
            return [
                "100 miles", "1,000 miles", "10,000 miles"
            ]
        elif self.correct_answer.isdigit():  # Numbers
            correct_value = int(self.correct_answer)
            return [str(correct_value + random.randint(-10, 10)) for _ in range(3)]
        elif "million" in self.correct_answer:
            return ["1 million", "10 million", "100 million"]
        else:
            return ["Choice 1", "Choice 2", "Choice 3"]