from flask import Flask, request, render_template_string
import json
from pathlib import Path

app = Flask(__name__)

MOVIES_FILE = Path(__file__).parent / "movies.json"

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Movie Search</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: #f4f4f4;
            padding: 60px;
        }
        input {
            padding: 12px;
            width: 300px;
        }
        button {
            padding: 12px 20px;
            cursor: pointer;
        }
        .result {
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <h1>Movie Search</h1>

    <form method="GET">
        <input type="text" name="q"
               placeholder="Enter movie name"
               value="{{ query }}" required>
        <button type="submit">Search</button>
    </form>

    <div class="result">
        {% if searched %}
            {% if results %}
                <h2>Movie Found!</h2>
                {% for movie in results %}
                    <h3>{{ movie.title }}</h3>
                    <p>Rating: {{ movie.vote_average }}/10</p>
                    <p>Votes: {{ movie.vote_count }}</p>
                {% endfor %}
            {% else %}
                <h2>Movie not found in database.</h2>
            {% endif %}
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/")
def search_movie():
    query = request.args.get("q", "").strip()
    results = []

    if query:
        with open(MOVIES_FILE, "r", encoding="utf-8") as file:
            movies = json.load(file)

        results = [
            movie for movie in movies
            if query.casefold() in movie.get("title", "").casefold()
        ]

    return render_template_string(
        HTML,
        query=query,
        results=results,
        searched=bool(query)
    )


if __name__ == "__main__":
    app.run(debug=True)