import sqlite3

# Connect to the database
CONN = sqlite3.connect("trivia.db")
CURSOR = CONN.cursor()

# Update query to clean up the `correct_answer` column
def clean_answers():
    """Remove the pre-existing letter from the correct_answer column."""
    try:
        CURSOR.execute("""
            UPDATE questions
            SET correct_answer = TRIM(SUBSTR(correct_answer, INSTR(correct_answer, ')') + 2))
        """)
        CONN.commit()
        print("Answers cleaned successfully.")
    except Exception as e:
        print(f"Error cleaning answers: {e}")
    finally:
        CONN.close()

# Run the cleanup
if __name__ == "__main__":
    clean_answers()
