# ScamShield 🛡️

### Internship \& Job Offer Risk Assessment Assistant

## Project Overview

ScamShield is a web-based student cyber-safety prototype that helps students identify warning signs in suspicious job and internship offers.

Users can enter an offer message and optionally provide a URL. ScamShield analyzes the information using an explainable Python rule-based detection engine and provides a risk score, detected warning signals, explanations, and verification guidance.

**Workflow:**  
**DETECT → EXPLAIN → VERIFY → EDUCATE**

> ScamShield provides a risk assessment, not a guarantee.

\---

## Features Implemented

* 🔍 Job and internship offer analysis
* 💰 Payment and fee request detection
* ⏰ Urgency and pressure detection
* 🔐 Sensitive information request detection
* 🔗 Basic suspicious URL detection
* ⚠️ Risk score and LOW / MEDIUM / HIGH classification
* 💡 Explanation of detected warning signals
* ✅ Interactive 6-step verification checklist
* 📊 Verification progress tracking
* 🛡️ Student safety guidance
* 💾 SQLite analysis record storage

\---

## Tech Stack

|Component|Technology|
|-|-|
|Frontend|HTML, CSS, JavaScript|
|Backend|Python, Flask|
|Detection|Python Rule-Based Engine|
|Database|SQLite|

\---

## Installation \& Run

### Requirements

* Python 3.x
* pip

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

\---

## Demo Credentials

**Email:** `student@gmail.com`

**Password:** `std@123`

> These credentials are provided only for prototype demonstration.

\---

## Screenshots

### Home / Login

!\[Home](screenshots/home.png)

### Analyze Offer

!\[Analyze](screenshots/analyze.png)

### Risk Report

!\[Risk Report](screenshots/report.png)

### Verification Checklist

!\[Verify](screenshots/verify.png)

\---

## Deployment

**GitHub Repository:**  
https://github.com/PratimaC-tech/ScamShield

\---

## Project Structure

```text
ScamShield/
├── app.py
├── detector.py
├── requirements.txt
├── README.md
├── templates/
└── static/
```

\---

## Team

**Team Name:** SHE2 – Two Minds One Solution

**Team Leader:** Pratima Chaudhari

**Team Member:** Riya Chiddarwar

**Contact:** pratima.chaudhari\_comp25@pccoer.in

