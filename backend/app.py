from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "backend running", "message": "Red Queen Emulator Flask backend UP"})

@app.route('/api/demo', methods=['GET'])
def demo_api():
    return jsonify({"demo": True, "msg": "This is a demo API endpoint from Flask backend"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)