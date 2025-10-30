# Album Score Ranker

A simple Flask API that ranks albums based on user ratings.

**Tech Stack:** Python, Flask, SQLite 

## Run Locally
```bash
pip install -r requirements.txt
python app.py
## Example Endpoints
- GET /albums → View sample album scores
- POST /rank → Submit a new album rating
{
  "album": "Random Access Memories",
  "rating": 10
}
