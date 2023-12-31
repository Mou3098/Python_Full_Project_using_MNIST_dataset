
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
conn.commit()

def add_user(name, age):
    # Add data
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()

def retrieve_users():
    # Retrieve data
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_user_age(name, new_age):
    # Update data
    cursor.execute('UPDATE users SET age=? WHERE name=?', (new_age, name))
    conn.commit()

def delete_user(name):
    # Delete data
    cursor.execute('DELETE FROM users WHERE name=?', (name,))
    conn.commit()

# Example Usage:
add_user('John Doe', 25)
add_user('Jane Smith', 30)

print("Before Update:")
retrieve_users()

update_user_age('John Doe', 30)

print("\nAfter Update:")
retrieve_users()

delete_user('Jane Smith')

print("\nAfter Deletion:")
retrieve_users()

# Close the connection
conn.close()
