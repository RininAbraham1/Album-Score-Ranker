from flask import Flask, jsonify, request
from database import get_all_albums, add_rating

app = Flask(__name__)

@app.route("/")
def home():
    return "Album Score Ranker API is running!"

@app.route("/albums", methods=["GET"])
def albums():
    albums = get_all_albums()
    return jsonify(albums)

@app.route("/rank", methods=["POST"])
def rank_album():
    data = request.json
    album_title = data.get("album")
    rating = data.get("rating")
    success = add_rating(album_title, rating)
    if success:
        return jsonify({"message": f"Received rating for {album_title}!"})
    return jsonify({"error": "Album not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
