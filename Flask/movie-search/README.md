# Flask Movie Search

A simple local movie search application built with **Python** and **Flask**, using movie data retrieved from **The Movie Database (TMDB) API**.

This project is part of my personal learning journey, focusing on REST APIs, JSON data handling, and web development with Flask.

## Features

- Fetch movie information from TMDB.
- Filter movies released in 2026.
- Include movies with a TMDB rating greater than 7 and at least 100 votes.
- Store movie data locally in `movies.json`.
- Search movies by title through a browser interface.
- Display matching movie titles, ratings, and vote counts.
- Perform case-insensitive and partial-title searches.
- Search the local JSON file without making additional API requests.

## Technologies Used

- Python
- Flask
- Requests
- python-dotenv
- TMDB API
- JSON
- HTML and CSS

## Project Structure

```text
flask-movie-search/
├── app.py
├── fetch_movies.py
├── movies.json
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mahdie-dolatabadi/learning-hub.git
cd learning-hub/flask-movie-search
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the TMDB API

Create a `.env` file in the project directory and add your TMDB API key:

```env
TMDB_API_KEY=your_api_key_here
```

You can obtain an API key from [TMDB](https://www.themoviedb.org/settings/api).

### 4. Fetch movie data

```bash
python fetch_movies.py
```

This script retrieves qualifying movies from TMDB and saves the results to `movies.json`.

### 5. Run the Flask application

```bash
python app.py
```

Open your browser and navigate to:

http://127.0.0.1:5000

## How It Works

The project consists of two main components.

**Movie Data Collection (`fetch_movies.py`)**

The script sends requests to the TMDB Discover Movie API, retrieves matching movie records across available result pages, and stores them in a local JSON file.

Filtering criteria:

| Parameter | Value |
|---|---|
| Release date | January 1 – November 20, 2026 |
| TMDB rating | Greater than 7 |
| Minimum votes | 100 |
| Sorting | Rating, descending |

**Local Movie Search (`app.py`)**

The Flask application reads `movies.json` and provides a browser-based search interface.

Users can enter a full or partial movie title. If matching records exist, the application displays their titles, ratings, and vote counts. Otherwise, it displays a movie-not-found message.

Searches are performed locally without contacting TMDB.

## Example

Search query:

```text
Avatar
```

If matching movies are stored in `movies.json`, their information will appear in the results section.

## Limitations

- Only movies are supported; TV series are not included.
- The dataset covers a specific period of 2026.
- Search results are limited to movies already stored locally.
- The dataset does not update automatically.
- TMDB API pagination limits may affect very large result sets.
- The Flask application is intended for local development, not production deployment.

## Future Improvements

- Add TV series support.
- Introduce search filters by genre and rating.
- Display movie posters.
- Add automatic dataset updates.
- Improve the user interface.

## Data Source

Movie information is provided by [The Movie Database (TMDB)](https://www.themoviedb.org/).

This product uses the TMDB API but is not endorsed or certified by TMDB.

## Purpose

This project was created for educational purposes to practice API integration, JSON file handling, and Flask-based web development.