import sqlite3

# 1. Establish connection
# This will automatically create 'bass_tracker.db' in current folder if it doesn't exist
conn = sqlite3.connect('bass_tracker.db')

# 2. Create a cursor object
# The cursor is what is used to actually send SQL commands to the database/
cursor = conn.cursor()

# 3. Create the Techniques table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Techniques(
    technique_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT
    )
''')

# 4. Save (commit) the changes
conn.commit()
print("Techniques table created successfully!")