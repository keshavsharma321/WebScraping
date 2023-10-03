from flask import Flask, jsonify , request
import requests

app = Flask(__name__)

link = "https://raw.githubusercontent.com/keshavsharma321/WebScraping/main/db.json"

@app.route('/', methods=['GET'])
def displayData():
    if request.method == 'GET':  
        response = requests.get(link)
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": "Failed to fetch data from the URL"}), 500

if __name__ == '__main__':
    app.run(debug=True)
