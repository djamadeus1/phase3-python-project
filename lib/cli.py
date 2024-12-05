import sys
sys.path.append("lib") 
from models.category import Category
from models.question import Question


def main():
    while True:
        print("\n--- Trivia Game ---")
        print("1. View Categories")
        print("2. Play a Question")
        print("3. Exit Game")
        print("4. Add a Question")
        print("5. Delete a Question")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_categories()
        elif choice == "2":
            play_question()
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            add_question()
        elif choice == "5":
            delete_question()
        else:
            print("Invalid choice. Please try again.")


def view_categories():
    """Display all categories."""
    print("\nCategories:")
    categories = Category.all()
    for category in categories:
        print(f"{category.id}. {category.name}")


def play_question():
    """Play a trivia question."""
    correct_count = 0
    wrong_count = 0

    try:
        # Select a category
        category_id = input("\nEnter the category ID to play: ").strip()
        if not category_id.isdigit():
            print("Invalid category ID. Please enter a number.")
            return

        category_id = int(category_id)
        asked_questions = set()

        while True:
            # Fetch a random question from the category, excluding already asked ones
            question = Question.find_random_by_category(category_id, exclude_ids=asked_questions)

            if not question:
                # Reset asked_questions to loop through the questions again
                print("You've answered all questions in this category. Starting over...")
                asked_questions.clear()
                continue

            asked_questions.add(question.id)

            # Generate multiple-choice options
            choices = question.generate_choices()

            # Display the question and choices
            print(f"\nQuestion: {question.question_text}")
            for letter, choice in choices.items():
                print(f"{letter}) {choice}")

            # Add a blank line for better readability
            print()

            # Ask the user for their answer
            user_answer = input("Choose answer (A/B/C/D)\nor type 'exit' to go back to quit: ").strip().upper()

            if user_answer.lower() == "exit":
                print("Exiting category. Returning to main menu.")
                break

            # Validate the answer
            try:
                correct_letter = next(
                    letter for letter, choice in choices.items() if choice.strip() == question.correct_answer.strip()
                )
            except StopIteration:
                print("An error occurred: The correct answer is not in the choices. Please check the question data.")
                return

            if user_answer == correct_letter:
                print(f"\nCorrect! {correct_letter}: {question.correct_answer.strip()}")
                correct_count += 1
            else:
                print(f"\nWrong! The correct answer is: {correct_letter}) {question.correct_answer.strip()}")
                wrong_count += 1

            # Show the current score
            print(f"Current Score: {correct_count} Correct, {wrong_count} Wrong")
            print()  # Add a blank line for better readability

    except ValueError:
        print("Invalid category ID. Please enter a number.")



def add_question():
    """Add a new question to the database."""
    print("\n--- Add a Question ---")
    category_id = input("Enter the category ID for the question: ")
    question_text = input("Enter the question text: ")
    correct_answer = input("Enter the correct answer: ")

    try:
        new_question = Question(
            question_text=question_text,
            correct_answer=correct_answer,
            category_id=int(category_id),
        )
        new_question.save()
        print(f"Question added successfully: {question_text}")
    except Exception as e:
        print(f"Error adding question: {e}")


def delete_question():
    """Display all questions and prompt the user to delete one."""
    try:
        # Fetch all questions
        questions = Question.all()
        if not questions:
            print("\nNo questions available to delete.")
            return

        # Display questions with IDs and categories
        print("\nAvailable Questions:")
        for question in questions:
            category = Category.find_by_id(question.category_id)
            category_name = category.name if category else "Unknown"
            print(f"{question.id}. {question.question_text} (Category: {category_name})")

        # Prompt the user to select a question by ID
        question_id = input("\nEnter the ID of the question you want to delete (or type 'exit' to go back): ").strip()

        if question_id.lower() == 'exit':
            print("Returning to the main menu.")
            return

        try:
            question_id = int(question_id)
            question = Question.find_by_id(question_id)

            if not question:
                print(f"Question with ID {question_id} not found.")
                return

            # Confirm deletion
            confirm = input(f"Are you sure you want to delete this question: '{question.question_text}'? (yes/no): ").strip().lower()
            if confirm == 'yes':
                question.delete()
                print(f"Question with ID {question_id} deleted successfully.")
            else:
                print("Deletion canceled.")
        except ValueError:
            print("Invalid input. Please enter a valid question ID.")
    except Exception as e:
        print(f"An error occurred while deleting the question: {e}")


if __name__ == "__main__":
    main()
