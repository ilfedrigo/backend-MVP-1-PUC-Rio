import sqlite3

def connect_db():
    return sqlite3.connect('database.db')

def initialize_db():
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            comment TEXT
        )
        """)
        connection.commit()

if __name__ == '__main__':
    initialize_db()
