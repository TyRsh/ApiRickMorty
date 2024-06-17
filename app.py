from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

RICK_AND_MORTY_API_URL = "https://rickandmortyapi.com/api/character"

@app.route('/search', methods=['GET'])
def search_character():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400
    
    response = requests.get(RICK_AND_MORTY_API_URL, params={'name': name})
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Character not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
