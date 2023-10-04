from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

json_url = "https://raw.githubusercontent.com/keshavsharma321/WebScraping/main/db.json"

def get_data():
    response = requests.get(json_url)
    data = response.json()
    return data

@app.route("/", methods=["GET"])
def display_json_data():
    data = get_data()
    return jsonify(data)

@app.route("/entity", methods=["GET"])
def get_entity_by_id():
    data = get_data()
    
    option = request.args.get("option")
    id = request.args.get("id")
    
    if not option or not id:
        return jsonify({"error": "Missing option or id in query parameters"}), 400
    
    if option not in ["User", "Post", "Comments"]:
        return jsonify({"error": "Invalid option"}), 400
    
    entities = data.get(option, [])
    
    for entity in entities:
        if entity["id"] == int(id):
            return jsonify(entity)
    
    return jsonify({"error": f"{option} with id {id} not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
