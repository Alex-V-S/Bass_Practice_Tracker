from flask import Flask, jsonify

app = Flask(__name__)

# The first API endpoint
@app.route('/api/status', methods=['GET'])
# The root endpoint (The front door)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Bass Practice Tracker!"
def get_status():
    return jsonify({
        "status": "success",
        "message": "Bass Practice Tracker API is running!"
    })

if __name__ == '__main__':
    app.run(debug=True)