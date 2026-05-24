# Sports Odds Analyzer

Real-time sports betting odds analyzer built using Python and Flask.

This project fetches live football betting odds from The Odds API, compares bookmaker odds, and displays the best available odds for each team.

---

## Features

- Live sports odds fetching
- Best odds comparison
- Arbitrage detection logic
- Flask web application
- Deployable on Render
- Simple and clean project structure

---

## Tech Stack

- Python
- Flask
- Requests
- Gunicorn
- REST API

---

## Project Structure

```bash
sports-odds-analyzer/
│
├── app.py
├── analyzer.py
├── requirements.txt
├── render.yaml
└── README.md


## Installation

Clone the repository:

git clone https://github.com/your-username/sports-odds-analyzer.git

Move into project directory:

cd sports-odds-analyzer

Install dependencies:

pip install -r requirements.txt
Run Project
python app.py

Open in browser:

http://127.0.0.1:5000
Deployment

Deploy easily on Render.

Required files:

requirements.txt
render.yaml
API Used

The Odds API

https://the-odds-api.com/

Future Improvements
Real arbitrage calculator
Multiple sports support
Live auto-refresh
Database integration
Dashboard UI
CSV export
Author

Meet Sharma
