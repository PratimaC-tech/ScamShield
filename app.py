from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from detector import analyze_offer
import sqlite3
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'scamshield-round2-demo-key'

# Demo credentials for the Round 2 prototype.
DEMO_EMAIL = 'student@gmail.com'
DEMO_PASSWORD = 'std@123'
DB_PATH = Path("data/scamshield.db")

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            risk_level TEXT NOT NULL,
            risk_score INTEGER NOT NULL,
            message_length INTEGER NOT NULL,
            url TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login is presented directly on the home page.
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        if email == DEMO_EMAIL and password == DEMO_PASSWORD:
            session['logged_in'] = True
            session['user_email'] = email
            # Successful home-page login goes directly to Analyze.
            return redirect(url_for('analyze_page'))

        # Keep the user on the home page if the credentials are incorrect.
        flash('Invalid demo credentials. Please use the credentials shown below.')
        return redirect(url_for('home'))

    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/analyze")
def analyze_page():
    return render_template("analyze.html")

@app.route("/report")
def report_page():
    return render_template("report.html")

@app.route("/verify")
def verify_page():
    return render_template("verify.html")

@app.route("/safety")
def safety_page():
    return render_template("safety.html")

@app.post("/api/analyze")
def api_analyze():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    url = str(data.get("url", "")).strip()

    if not message and not url:
        return jsonify({"error": "Please enter an offer message or job URL."}), 400

    result = analyze_offer(message, url)

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO analyses (created_at, risk_level, risk_score, message_length, url) VALUES (?, ?, ?, ?, ?)",
        (datetime.now().isoformat(timespec="seconds"),
         result["risk_level"], result["risk_score"], len(message), url)
    )
    conn.commit()
    conn.close()

    return jsonify(result)

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "ScamShield"})

init_db()

if __name__ == "__main__":
    app.run(debug=True)
