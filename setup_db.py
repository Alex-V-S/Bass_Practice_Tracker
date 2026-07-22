import sqlite3

# 1. Establish the connection
conn = sqlite3.connect('bass_tracker.db')
cursor = conn.cursor()

# 2. Create the Techniques table (Static library)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Techniques (
    technique_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT
)
''')

# 3. Create the Sessions table (Macro daily details)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    duration_minutes INTEGER
)
''')

# 4. Create the Session_Logs table (The bridge table with your metrics)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Session_Logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER,
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

# 5. Insert a test technique to verify it works
cursor.execute('''
INSERT INTO Techniques (name, category)
VALUES ('The Adults Are Talking - The Strokes', 'Repertoire')
''')

# 6. Save (commit) the changes and close
conn.commit()
conn.close()
print("Database, tables, and test data created successfully!")