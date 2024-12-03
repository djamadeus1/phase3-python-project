from models.category import Category
from models.question import Question



print("Starting tests...")

# Step 1: Create the table
print("Creating categories table...")
Category.create_table()
print("Table created successfully!")

# Step 2: Add a category
print("Adding a category...")
cat1 = Category(name="Science")
cat1.save()
print(f"Category saved with ID: {cat1.id}")

print("Fetching all categories...")
all_categories = Category.all()
for category in all_categories:
    print(f"ID: {category.id}, Name: {category.name}")

cat2 = Category(name="History")
cat2.save()
print(f"Category saved with ID: {cat2.id}")

print("Starting Question table test...")

# Step 1: Create the questions table
print("Creating questions table...")
Question.create_table()
print("Questions table created successfully!")


print("Testing the save method for Question...")

# Step 1: Create a new Question
question1 = Question(
    question_text="What is the capital of France?",
    correct_answer="Paris",
    category_id=1  # Assuming Category ID 1 exists in your database
)

# Step 2: Save the Question
question1.save()
print(f"Question saved with ID: {question1.id}")

print("Fetching all questions...")
all_questions = Question.all()
for question in all_questions:
    print(f"ID: {question.id}, Text: {question.question_text}, Answer: {question.correct_answer}, Category ID: {question.category_id}")

print("Finding a question by ID...")
question = Question.find_by_id(1)
if question:
    print(f"Found Question: ID {question.id}, Text: {question.question_text}, Answer: {question.correct_answer}, Category ID: {question.category_id}")
else:
    print("No question found with that ID.")

print("Fetching one question from a category...")
question = Question.find_by_category(1)  # Assuming Category ID 1 exists
if question:
    print(f"Question from Category ID 1: ID {question.id}, Text: {question.question_text}")
else:
    print("No question found in Category ID 1.")

print("Fetching all questions...")
all_questions = Question.all()
for question in all_questions:
    print(f"ID: {question.id}, Text: {question.question_text}, Answer: {question.correct_answer}, Category ID: {question.category_id}")


# Add Math category
math_category = Category(name="Math")
math_category.save()

print("Math category added.")

print("Fetching all categories...")
all_categories = Category.all()
for category in all_categories:
    print(f"ID: {category.id}, Name: {category.name}")


# Questions for Science
science_questions = [
    {"text": "If you're standing on flat ground, how far can you see in any direction?", "answer": "B) 3 miles", "category_id": 1},
    {"text": "How many Earths can fit inside the Sun?", "answer": "D) 1.3 million", "category_id": 1},
    {"text": "How far is the Sun from Earth?", "answer": "B) 93 million miles", "category_id": 1},
    {"text": "How far is the Moon from Earth?", "answer": "A) 238,855 miles", "category_id": 1},
    {"text": "What is the chemical symbol for water?", "answer": "B) H₂O", "category_id": 1},
    {"text": "What is the powerhouse of the cell?", "answer": "C) Mitochondrion", "category_id": 1},
    {"text": "Which planet is known as the Red Planet?", "answer": "B) Mars", "category_id": 1},
    {"text": "What is the boiling point of water at sea level in Celsius?", "answer": "B) 100°C", "category_id": 1},
    {"text": "Which element is the most abundant in the Earth's crust?", "answer": "B) Oxygen", "category_id": 1},
    {"text": "Who developed the theory of relativity?", "answer": "B) Albert Einstein", "category_id": 1},
]

# Questions for Math
math_questions = [
    {"text": "What is the value of π (pi) to two decimal places?", "answer": "B) 3.14", "category_id": 3},
    {"text": "What is 7 × 8?", "answer": "B) 56", "category_id": 3},
    {"text": "What is the square root of 64?", "answer": "C) 8", "category_id": 3},
    {"text": "What is 25% of 200?", "answer": "B) 50", "category_id": 3},
    {"text": "What is the value of 12²?", "answer": "B) 144", "category_id": 3},
    {"text": "If the perimeter of a square is 36, what is the length of one side?", "answer": "A) 6", "category_id": 3},
    {"text": "What is the area of a triangle with a base of 5 units and a height of 10 units?", "answer": "B) 30 square units", "category_id": 3},
    {"text": "What is the value of 3³?", "answer": "C) 27", "category_id": 3},
    {"text": "Which of the following is the solution to the equation 2x + 4 = 12?", "answer": "A) x = 3", "category_id": 3},
    {"text": "What is 15 ÷ 3?", "answer": "C) 5", "category_id": 3},
]

# Questions for History
history_questions = [
    {"text": "Who was the first president of the United States?", "answer": "C) George Washington", "category_id": 2},
    {"text": "In which year did World War I begin?", "answer": "B) 1914", "category_id": 2},
    {"text": "Who discovered America in 1492?", "answer": "B) Christopher Columbus", "category_id": 2},
    {"text": "What was the main cause of the American Civil War?", "answer": "A) Slavery", "category_id": 2},
    {"text": "Which ancient civilization built the pyramids of Giza?", "answer": "B) Egyptians", "category_id": 2},
    {"text": "What year did the Titanic sink?", "answer": "C) 1912", "category_id": 2},
    {"text": "Who was the famous queen of ancient Egypt?", "answer": "A) Cleopatra", "category_id": 2},
    {"text": "Which empire was ruled by Julius Caesar?", "answer": "A) Roman Empire", "category_id": 2},
    {"text": "Who was the leader of the Soviet Union during World War II?", "answer": "D) Joseph Stalin", "category_id": 2},
    {"text": "Which event began on July 20, 1969?", "answer": "B) The moon landing", "category_id": 2},
]

# Add questions to the database
for question_data in science_questions + math_questions + history_questions:
    question = Question(
        question_text=question_data["text"],
        correct_answer=question_data["answer"],
        category_id=question_data["category_id"]
    )
    question.save()

print("All questions added successfully.")

print("Fetching all questions...")
all_questions = Question.all()
for question in all_questions:
    print(f"ID: {question.id}, Text: {question.question_text}, Answer: {question.correct_answer}, Category ID: {question.category_id}")

print("Deleting default questions...")

# Replace with the IDs of the default questions
default_question_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for question_id in default_question_ids:
    question = Question.find_by_id(question_id)
    if question:
        question.delete()
        print(f"Deleted question with ID: {question_id}")

print("Default questions removed.")

