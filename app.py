from flask import Flask, jsonify, request
from scraper import fetch_album_data
from database import session, Album, Rating

app = Flask(__name__)

@app.route("/")
def home():
    return "Album Score Ranker API is running!"

@app.route("/albums", methods=["GET"])
def get_albums():
    albums = fetch_album_data(api_mode=False)
    return jsonify(albums)

@app.route("/rank", methods=["POST"])
def rank_album():
    data = request.json
    if not data or "album" not in data or "rating" not in data:
        return jsonify({"error": "Provide 'album' and 'rating' in JSON body"}), 400

    album_title = data["album"]
    rating_value = float(data["rating"])

    # Save rating to DB
    new_rating = Rating(album_title=album_title, rating=rating_value)
    session.add(new_rating)
    session.commit()

    return jsonify({"message": f"Received rating of {rating_value} for '{album_title}'!"})

@app.route("/rankings", methods=["GET"])
def get_rankings():
    # Aggregate ratings by album
    results = session.query(
        Rating.album_title,
        Rating.rating
    ).all()

    ranking_dict = {}
    for title, rating in results:
        if title not in ranking_dict:
            ranking_dict[title] = []
        ranking_dict[title].append(rating)

    rankings = [
        {
            "album": title,
            "average_rating": sum(ratings)/len(ratings),
            "num_ratings": len(ratings)
        }
        for title, ratings in ranking_dict.items()
    ]

    # Sort by average_rating descending
    rankings.sort(key=lambda x: x["average_rating"], reverse=True)
    return jsonify(rankings)

if __name__ == "__main__":
    app.run(debug=True)

