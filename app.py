from flask import Flask, jsonify, render_template
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# --- NEW: Database connection helper ---
def get_db_connection():
    # Connects to your specific database file
    conn = sqlite3.connect('bass_tracker.db')
    # This crucial line tells SQLite to return data as Python dictionaries 
    # instead of plain tuples, which makes it much easier to convert to JSON.
    conn.row_factory = sqlite3.Row
    return conn

# The root endpoint (The front door)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Your original status endpoint
@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "success",
        "message": "Bass Practice Tracker API is running!"
    })

# --- NEW: Your first real database endpoint! ---
@app.route('/api/techniques', methods=['GET'])
def get_techniques():
    # 1. Open the connection
    conn = get_db_connection()
    
    # 2. Run the SQL query to get everything from the Techniques table
    techniques = conn.execute('SELECT * FROM Techniques').fetchall()
    
    # 3. Always close the connection when you are done
    conn.close()
    
    # 4. Convert the SQL rows into a standard Python list so Flask can output it as JSON
    techniques_list = [dict(row) for row in techniques]
    
    return jsonify(techniques_list)

if __name__ == '__main__':
    app.run(debug=True)