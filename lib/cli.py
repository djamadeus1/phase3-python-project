import sys
sys.path.append(".")
from models.category import Category
from models.question import Question


def main():
    while True:
        print("\n--- Trivia Game ---")
        print("1. View Categories")
        print("2. Play a Question")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_categories()
        elif choice == "2":
            play_question()
        elif choice == "3":
            print("Goodbye!")
            break
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
    try:
        # Select a category
        category_id = input("\nEnter the category ID to play: ")
        question = Question.find_by_category(int(category_id))

        if not question:
            print("No questions available in this category.")
            return

        # Generate multiple-choice options
        choices = question.generate_choices()

        # Display the question and choices
        print(f"\nQuestion: {question.question_text}")
        for letter, choice in choices.items():
            print(f"{letter}) {choice}")

        # Ask the user for their answer
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Validate the answer
        try:
            correct_letter = next(
                letter for letter, choice in choices.items() if choice.strip() == question.correct_answer.strip()
            )
        except StopIteration:
            print("An error occurred: The correct answer is not in the choices. Please check the question data.")
            return

        if user_answer == correct_letter:
            print(f"Correct! {correct_letter}: {question.correct_answer.strip()}")
        else:
            print(f"Wrong! The correct answer is: {correct_letter}) {question.correct_answer.strip()}")

    except ValueError:
        print("Invalid category ID. Please enter a number.")


if __name__ == "__main__":
    main()
