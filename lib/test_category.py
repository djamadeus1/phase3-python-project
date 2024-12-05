from models.category import Category
from models.question import Question
from models.__init__ import CONN, CURSOR

def reset_trivia_database():
    """Reset the trivia database and repopulate it with correct data."""
    print("Resetting the trivia database...")
    
    CURSOR.execute("DROP TABLE IF EXISTS questions;")
    CURSOR.execute("DROP TABLE IF EXISTS categories;")
    
    Category.create_table()
    Question.create_table()
    
    print("Repopulating categories...")
    for category_name in ["Science", "History", "Math"]:
        new_category = Category(name=category_name)
        new_category.save()
    
    print("Repopulating questions...")
    update_questions_in_db()

    CONN.commit()
    print("Trivia database reset and repopulated.")

def update_questions_in_db():
    """Ensure the database contains the latest question data."""
    print("Checking for updates to questions...")

    science_questions = [
        {"text": "If you're standing on flat ground, how far can you see in any direction?", "answer": "3 miles", "category_id": 1},
        {"text": "How many Earths can fit inside the Sun?", "answer": "1.3 million", "category_id": 1},
        {"text": "How far is the Sun from Earth?", "answer": "93 million miles", "category_id": 1},
        {"text": "How far is the Moon from Earth?", "answer": "238,855 miles", "category_id": 1},
        {"text": "What is the chemical symbol for water?", "answer": "H₂O", "category_id": 1},
        {"text": "What is the powerhouse of the cell?", "answer": "Mitochondrion", "category_id": 1},
        {"text": "Which planet is known as the Red Planet?", "answer": "Mars", "category_id": 1},
        {"text": "What is the boiling point of water at sea level in Celsius?", "answer": "100°C", "category_id": 1},
        {"text": "Which element is the most abundant in the Earth's crust?", "answer": "Oxygen", "category_id": 1},
        {"text": "Who developed the theory of relativity?", "answer": "Albert Einstein", "category_id": 1},
    ]

    math_questions = [
        {"text": "What is the value of π (pi) to two decimal places?", "answer": "3.14", "category_id": 3},
        {"text": "What is 7 × 8?", "answer": "56", "category_id": 3},
        {"text": "What is the square root of 64?", "answer": "8", "category_id": 3},
        {"text": "What is 25% of 200?", "answer": "50", "category_id": 3},
        {"text": "What is the value of 12²?", "answer": "144", "category_id": 3},
        {"text": "If the perimeter of a square is 36, what is the length of one side?", "answer": "6", "category_id": 3},
        {"text": "What is the area of a triangle with a base of 5 units and a height of 10 units?", "answer": "30 square units", "category_id": 3},
        {"text": "What is the value of 3³?", "answer": "27", "category_id": 3},
        {"text": "Which of the following is the solution to the equation 2x + 4 = 12?", "answer": "x = 3", "category_id": 3},
        {"text": "What is 15 ÷ 3?", "answer": "5", "category_id": 3},
    ]

    history_questions = [
        {"text": "Who was the first president of the United States?", "answer": "George Washington", "category_id": 2},
        {"text": "In which year did World War I begin?", "answer": "1914", "category_id": 2},
        {"text": "Who discovered America in 1492?", "answer": "Christopher Columbus", "category_id": 2},
        {"text": "What was the main cause of the American Civil War?", "answer": "Slavery", "category_id": 2},
        {"text": "Which ancient civilization built the pyramids of Giza?", "answer": "Egyptians", "category_id": 2},
        {"text": "What year did the Titanic sink?", "answer": "1912", "category_id": 2},
        {"text": "Who was the famous queen of ancient Egypt?", "answer": "Cleopatra", "category_id": 2},
        {"text": "Which empire was ruled by Julius Caesar?", "answer": "Roman Empire", "category_id": 2},
        {"text": "Who was the leader of the Soviet Union during World War II?", "answer": "Joseph Stalin", "category_id": 2},
        {"text": "Which event began on July 20, 1969?", "answer": "The moon landing", "category_id": 2},
    ]

    all_questions = science_questions + math_questions + history_questions
    added_count = 0

    for question_data in all_questions:
        Question(
            question_text=question_data["text"],
            correct_answer=question_data["answer"],
            category_id=question_data["category_id"],
        ).save()
        added_count += 1

    print(f"Added {added_count} questions.")

if __name__ == "__main__":
    reset_trivia_database()

if __name__ == "__main__":
    reset_trivia_database()
