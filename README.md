# __Trivia Game CLI__

## Overview
This is a command-line interface (CLI) Trivia Game built as part of our Phase 3 project. Users can play the game by answering questions across multiple categories while the game keeps score. The user also has the ability to add and remove questions if they choose. 

The project is implemented using Python and SQLite with an Object-Relational Mapping (ORM) to manage the database.

## Features
- Play a trivia game with multiple categories and random questions.
- Add new trivia questions to the database.
- Delete existing trivia questions from the database.
- Tracks and displays user scores during gameplay.
- User-friendly interface with clear instructions and input validation.

## How to Start the Game:
Run this in the root directory:
- PYTHONPATH=lib python lib/cli.py

## Key Functions:
- Main: Displays the main menu and processes user choices.
- View Categories: Lists all available categories.
- Play Question: Manages the trivia gameplay, including showing questions, tracking scores, and handling user input.
- Add Question: Allows users to add a new question to the database.
- Delete Question: Allows users to delete a question from the database by selecting from a list.

## categories:
- Science
- Math
- History

## Usage
Main Menu Options:
- View Categories: Lists all categories.
- Play a Question: Lets the user choose a category and play the trivia game.
- Exit Game: Exits the application.
- Add a Question: Allows users to add a new trivia question.
- Delete a Question: Allows users to delete an existing trivia question.

## _Future Enhancements_
- Add additional questions and categories.
- Add a leaderboard to track user scores over multiple sessions.
- Implement timed questions for added challenge.

## The Developers:
- Ron Roberts
- Karina Mogha
- Casey Rayson