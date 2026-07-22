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

# 4. Create the Sessions table (Macro daily details)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    duraction_minutes INTEGER
)
''')

# 5. Create the Session_Logs table (The bridge table with your metrics)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Session_Logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER.
    technique_id INTEGER,
    target_bpm INTEGER,
    achieved_bpm INTEGER,
    fret_buzz_count INTEGER,
    muting_rating INTEGER,
    strict_alternation BOOLEAN,
    recall_time_sec INTEGER,
    completion_percentage INTEGER,
    FOREIGN KEY (session_id) REFERENCES Sessions (session_id),
    FOREIGN KEY (technique_id) REFERENCES Techniques (technique_id)
)
''')

# 6. Insert a test technique to verify it works
cursor.execute('''
INSERT INTO Techniques (name, category)
VALUES ('The Adults Are Talking - The Strokes', 'Repertoire')
''')

# 7. Save (commit) the changes
conn.commit()
conn.close()
print("Database, tables, and test data created successfully!")