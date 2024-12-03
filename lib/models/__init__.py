import sqlite3

# Centralize database connection
CONN = sqlite3.connect("lib/trivia.db")
CURSOR = CONN.cursor()
