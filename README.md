# Album Score Ranker 🎵

**Album Score Ranker** is a Python Flask app that aggregates user ratings to rank music albums, using REST APIs, SQL, and Raspberry Pi for data automation.

## Features

- ✅ Aggregate 2,000+ user ratings to rank albums with real-time updates.
- ✅ Optional live album data fetching via Spotify API or other music APIs.
- ✅ Automated album data scraping using Raspberry Pi cron jobs.
- ✅ SQLite database design with SQLAlchemy ORM for efficient data handling.
- ✅ RESTful API endpoints to get albums and submit ratings.
- ✅ Flask backend with JSON responses for easy integration.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API status check |
| `/albums` | GET | Returns album list (mock or live via API) |
| `/rank` | POST | Submit album rating (JSON body: `{"album": "...", "rating": ...}`) |

## Tech Stack

- **Python 3**
- **Flask** for backend API
- **SQLAlchemy ORM** for database interactions
- **SQLite** database
- **Requests** for API calls
- **Raspberry Pi** for scheduled scraping
- **REST API design**

## Installation & Run

```bash
# Clone repo
git clone https://github.com/RininAbraham1/Album-Score-Ranker.git
cd Album-Score-Ranker

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py

# Visit in browser
http://127.0.0.1:5000/albums
