Album Score Ranker

Python | Flask | REST APIs | SQLAlchemy | Raspberry Pi | Spotify API

An interactive backend service that ranks music albums based on user ratings and integrates live album metadata from Spotify. Designed for real-time updates, scalable data collection, and structured database handling.

Table of Contents

Features

Technologies

Setup & Installation

API Endpoints

Database Schema

Example Workflow

Future Improvements

Features

Aggregates 2,000+ album ratings to generate dynamic rankings

Fetches album metadata using Spotify API

Provides RESTful endpoints for album retrieval and rating submission

SQLite database integration via SQLAlchemy ORM for efficient storage

Optional Raspberry Pi cron jobs for automated album scraping

Returns average ratings and ranking for albums

Modular structure: scraper.py for data fetching, database.py for persistent storage, app.py for API

Technologies

Python – Core backend language

Flask – RESTful API development

SQLite + SQLAlchemy – Database storage and ORM

Requests – API communication

Raspberry Pi (optional) – Automated cron jobs for album data scraping

Spotify Web API – Live album metadata

JSON – Data interchange format

Setup & Installation

Clone the repository:

git clone https://github.com/YourUsername/Album-Score-Ranker.git
cd Album-Score-Ranker


Create a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux


Install dependencies:

pip install -r requirements.txt


Set up the database (SQLite):

python database.py


Obtain Spotify API access token (optional for live data):

Sign up for a Spotify Developer account

Create a new app → get Client ID and Client Secret

Run get_token.py to generate your token

Set api_mode=True in scraper.py

Run the API server:

python app.py


Access endpoints:

Open your browser or Postman: http://127.0.0.1:5000/albums

API Endpoints
Endpoint	Method	Description
/	GET	API status check
/albums	GET	Retrieve album list (mock or Spotify)
/rank	POST	Submit album rating ({"album": "Name", "rating": 95})
/rankings	GET	Get albums ranked by average user rating
Database Schema

Album Table

Column	Type	Description
id	Integer	Unique album ID
title	String	Album title
artist	String	Album artist(s)

Rating Table

Column	Type	Description
id	Integer	Unique rating ID
album_title	String	Album name (foreign key)
rating	Float	User-submitted rating (0-100)
Example Workflow

Fetch album list from /albums

Submit a user rating to /rank

POST /rank
{
    "album": "To Pimp a Butterfly",
    "rating": 95
}


Retrieve updated album rankings from /rankings

[
    {
        "album": "To Pimp a Butterfly",
        "average_rating": 95,
        "num_ratings": 1
    }
]

Future Improvements

Integrate real-time frontend visualization of album rankings

Add user authentication and personalized rating history

Include multiple APIs (Apple Music, SoundCloud) for richer metadata

Deploy backend on cloud server for public access

Implement automated weekly scraping via Raspberry Pi cron jobs

Showcases:

Backend development with Python and Flask

API integration and token-based authentication

Database modeling and SQLAlchemy ORM

Automated data collection using Raspberry Pi

Practical experience in handling live and mock data
