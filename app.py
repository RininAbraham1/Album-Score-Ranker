from flask import Flask, jsonify, request
from scraper import fetch_album_data  # import our scraper module

app = Flask(__name__)

@app.route("/")
def home():
    return "Album Score Ranker API is running!"

@app.route("/albums", methods=["GET"])
def get_albums():
    # Pass api_mode=True if you want to fetch from real API (requires token setup)
    albums = fetch_album_data(api_mode=False)
    return jsonify(albums)

@app.route("/rank", methods=["POST"])
def rank_album():
    data = request.json
    if not data or "album" not in data or "rating" not in data:
        return jsonify({"error": "Provide 'album' and 'rating' in JSON body"}), 400
    
    # Here you could integrate SQLAlchemy to store ratings in a DB
    # For now, we just return a confirmation
    return jsonify({"message": f"Received rating of {data['rating']} for {data['album']}!"})

if __name__ == "__main__":
    app.run(debug=True)
