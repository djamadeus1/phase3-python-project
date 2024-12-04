import sqlite3
import random  
import os
from .category import Category  

# Define the database path
DB_PATH = os.path.join("lib", "trivia.db") 

# Initialize the database connection
CONN = sqlite3.connect(DB_PATH)
CURSOR = CONN.cursor()

class Question:
    def __init__(self, question_text, correct_answer, category_id, id=None):
        self.id = id
        self._question_text = question_text
        self._correct_answer = correct_answer
        self.category_id = category_id

    @property
    def question_text(self):
        """Getter for question text."""
        return self._question_text

    @question_text.setter
    def question_text(self, value):
        """Setter for question text with validation."""
        if not value.strip() or len(value) < 5:
            raise ValueError("Question text must be at least 5 characters long.")
        self._question_text = value

    @property
    def correct_answer(self):
        """Getter for correct answer."""
        return self._correct_answer

    @correct_answer.setter
    def correct_answer(self, value):
        """Setter for correct answer with validation."""
        if not value.strip():
            raise ValueError("Correct answer cannot be empty.")
        self._correct_answer = value

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
            CURSOR.execute(
                """
                INSERT INTO questions (question_text, correct_answer, category_id)
                VALUES (?, ?, ?);
                """,
                (self._question_text, self._correct_answer, self.category_id),
            )
            CONN.commit()
            self.id = CURSOR.lastrowid
        except Exception as e:
            print(f"Error saving question: {e}")

    @classmethod
    def all(cls):
        """Fetch all questions from the database."""
        try:
            CURSOR.execute("SELECT * FROM questions;")
            rows = CURSOR.fetchall()
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

    @classmethod
    def find_random_by_category(cls, category_id, exclude_ids=set()):
        """Fetch a random question from a specific category, excluding already asked questions."""
        try:
            placeholders = ', '.join('?' for _ in exclude_ids)
            query = f"""
                SELECT * FROM questions
                WHERE category_id = ? {f"AND id NOT IN ({placeholders})" if exclude_ids else ""}
                ORDER BY RANDOM()
                LIMIT 1;
            """
            params = (category_id, *exclude_ids) if exclude_ids else (category_id,)
            CURSOR.execute(query, params)
            row = CURSOR.fetchone()
            if row:
                return cls(
                    id=row[0],
                    question_text=row[1],
                    correct_answer=row[2],
                    category_id=row[3]
                )
        except Exception as e:
            print(f"Error finding random question by category: {e}")
        return None

    def delete(self):
        """Delete the current question from the database."""
        try:
            CURSOR.execute("DELETE FROM questions WHERE id = ?;", (self.id,))
            CONN.commit()
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
        random.shuffle(all_choices)

        # Return choices with letters
        choices_with_letters = {letter: choice for letter, choice in zip("ABCD", all_choices)}
        return choices_with_letters

    def get_plausible_wrong_answers(self):
        """Generate plausible wrong answers based on the correct answer."""
        if "miles" in self.correct_answer:
            return [
                "100 miles", "1,000 miles", "10,000 miles"
            ]
        elif self.correct_answer.isdigit():
            correct_value = int(self.correct_answer)
            return [str(correct_value + random.randint(-10, 10)) for _ in range(3)]
        elif "million" in self.correct_answer:
            return ["1 million", "10 million", "100 million"]
        else:
            return ["Choice 1", "Choice 2", "Choice 3"]
