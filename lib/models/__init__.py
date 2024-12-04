import sqlite3
import os

# Construct the absolute path to `trivia.db` in the `lib` directory
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../trivia.db")

# Connect to the database
CONN = sqlite3.connect(DB_PATH)
CURSOR = CONN.cursor()
