from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "Album Score Ranker API is running!"

@app.route("/albums", methods=["GET"])
def get_albums():
    # Example: pretend to fetch albums
    albums = [
        {"title": "Random Access Memories", "artist": "Daft Punk", "score": 9.5},
        {"title": "To Pimp a Butterfly", "artist": "Kendrick Lamar", "score": 9.7},
        {"title": "Blonde", "artist": "Frank Ocean", "score": 9.4}
    ]
    return jsonify(albums)

@app.route("/rank", methods=["POST"])
def rank_album():
    data = request.json
    return jsonify({"message": f"Received rating for {data['album']}!"})

if __name__ == "__main__":
    app.run(debug=True)
