from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import requests

URL = "https://api.jikan.moe/v4"

app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/search-results", methods=['GET', 'POST'])
def search_results():
    params = {
        'q': request.form.get("searchInput"),
    }

    response = requests.get(url=f"{URL}/anime", params=params)
    response.raise_for_status()
    results = response.json()

    return render_template('results.html', results=results['data'])


@app.route("/details/<anime_id>", methods=['GET', 'POST'])
def details(anime_id):
    response = requests.get(url=f"{URL}/anime/{anime_id}/full")
    response.raise_for_status()
    result = response.json()
    return render_template('details.html', anime=result['data'])


if __name__ == "__main__":
    app.run(debug=True)
