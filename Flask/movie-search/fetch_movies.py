import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
URL = "https://api.themoviedb.org/3/discover/movie"

movies = []
page = 1

while True:
    params = {
        "api_key": API_KEY,
        "primary_release_date.gte": "2026-01-01",
        "primary_release_date.lte": "2026-11-20",
        "vote_average.gte": 7,
        "vote_count.gte": 100,
        "sort_by": "vote_average.desc",
        "page": page
    }

    response = requests.get(URL, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()

    movies.extend(data.get("results", []))

    total_pages = min(data["total_pages"], 500)
    print(f"Downloaded page {page}/{total_pages}")

    if page >= total_pages:
        break

    page += 1

movies = [m for m in movies if m["vote_average"] > 7]

with open("movies.json", "w", encoding="utf-8") as file:
    json.dump(movies, file, ensure_ascii=False, indent=2)

print(f"Saved {len(movies)} movies to movies.json")