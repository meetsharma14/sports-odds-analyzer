from flask import Flask
import requests
from analyzer import find_best_odds

app = Flask(__name__)

API_KEY = "your api key"

@app.route("/")

def home():

    url = f"https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?apiKey={API_KEY}&regions=uk&markets=h2h"

    response = requests.get(url)
    data = response.json()

    output = ""

    for match in data:

        output += f"<h2>{match['home_team']} vs {match['away_team']}</h2>"

        best = find_best_odds(match)

        for team, odds in best.items():
            output += f"{team} : {odds}<br>"

        output += "<hr>"

    return output


if __name__ == "__main__":
    app.run(debug=False)
