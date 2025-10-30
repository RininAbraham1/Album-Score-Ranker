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

