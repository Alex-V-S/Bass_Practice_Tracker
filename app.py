from flask import Flask, jsonify, render_template, request
import sqlite3

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

# Route to the database
@app.route('/api/techniques', methods=['POST'])
def add_technique():
    # 1. Grab the JSON data sent from the browser
    data = request.get_json()
    name = data.get('name')
    category = data.get('category')

    # 2. Open the database and insert the new row
    conn = get_db_connection()
    conn.execute('INSERT INTO Techniques (name, category) VALUES (?, ?)', (name, category))
    conn.commit()
    conn.close()

    # 3. Return a success response
    return jsonify({"status": "success", "message": "Technique added!"}), 201

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