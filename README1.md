Trivia Game CLI

Overview
This is a command-line interface (CLI) Trivia Game built as part of the Phase 3 project. Users can interact with the game to answer questions across multiple categories, add new questions, or delete existing ones. The project is implemented using Python and SQLite with an Object-Relational Mapping (ORM) to manage the database.

Features
Play a trivia game with multiple categories and random questions.
Add new trivia questions to the database.
Delete existing trivia questions from the database.
Tracks and displays user scores during gameplay.
User-friendly interface with clear instructions and input validation.

Files and Functionality
lib/cli.py
This is the main entry point for the application. It provides the user interface and manages the interaction between the user and the database.

Key Functions:
main(): Displays the main menu and processes user choices.
view_categories(): Lists all available categories.
play_question(): Manages the trivia gameplay, including showing questions, tracking scores, and handling user input.
add_question(): Allows users to add a new question to the database.
delete_question(): Allows users to delete a question from the database by selecting from a list.

lib/models/category.py
This file defines the Category model, representing the categories in the database.

Key Methods:
create_table(): Creates the categories table in the database if it doesn’t already exist.
save(): Saves a new category to the database.
all(): Fetches all categories from the database.
find_by_id(id): Finds a category by its ID.
delete(): Deletes a category from the database.
Properties:
name: A property to get or set the category name with validation.
lib/models/question.py
This file defines the Question model, representing the trivia questions in the database.

Key Methods:
create_table(): Creates the questions table in the database.
save(): Saves a new question to the database.
all(): Fetches all questions from the database.
find_by_id(id): Finds a question by its ID.
find_random_by_category(category_id, exclude_ids=set()): Fetches a random question from a specific category, excluding already asked questions.
delete(): Deletes a question from the database.
generate_choices(): Generates multiple-choice answers for a question.
Properties:
question_text: A property to get or set the question text with validation.
correct_answer: A property to get or set the correct answer with validation.
Database
The database (trivia.db) is managed using SQLite and contains two tables:

categories: Stores category information with columns id and name.
questions: Stores question information with columns id, question_text, correct_answer, and category_id.
Setup and Installation
Clone the repository.
Install required dependencies using the Pipfile.
bash
Copy code
pipenv install
Activate the virtual environment:
bash
Copy code
pipenv shell
Run the CLI:
bash
Copy code
PYTHONPATH=lib python lib/cli.py

Usage
Main Menu Options:
View Categories: Lists all categories.
Play a Question: Lets the user choose a category and play a trivia game.
Exit Game: Exits the application.
Add a Question: Allows users to add a new trivia question.
Delete a Question: Allows users to delete an existing trivia question.

Future Enhancements
Add functionality to edit existing questions and categories.
Add a leaderboard to track user scores over multiple sessions.
Implement timed questions for added challenge.
