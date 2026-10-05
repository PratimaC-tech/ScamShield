# ScamShield — AI-Assisted Internship & Job Offer Verification Assistant

ScamShield is a web-based student cyber-safety prototype for analyzing suspicious job and internship offers.

## Core workflow

**DETECT → EXPLAIN → VERIFY → EDUCATE**

The prototype accepts an offer message and an optional job/internship URL. A Python rule engine checks for warning signals such as:

- Payment requests
- Urgency / pressure
- Sensitive information requests
- Suspicious URL patterns
- Unrealistic job/income guarantees
- Unusual recruitment language

It then produces a risk level, explains detected signals, and provides a verification checklist.

> **Important:** ScamShield provides risk assessment and educational guidance. It is not a guarantee that an offer is genuine or fraudulent.

## Technology

- HTML
- CSS
- JavaScript
- Python
- Flask
- SQLite
- Rule-based text and URL analysis

## Project structure

```text
ScamShield-Prototype/
├── app.py
├── detector.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   ├── analyze.html
│   ├── report.html
│   ├── verify.html
│   └── safety.html
├── static/
│   ├── style.css
│   └── script.js
└── data/
    └── scamshield.db   (created automatically)
```

## Setup

### 1. Install Python

Install Python 3.10+.

### 2. Open the project folder in a terminal

```bash
cd ScamShield-Prototype
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```text
http://127.0.0.1:5000
```

## Prototype demo

Try this example:

```text
Congratulations! You are selected for a remote internship.
Pay a refundable registration fee of ₹1999 today to confirm your seat.
Send your Aadhaar and bank details immediately. Offer expires today.
```

Expected result: HIGH risk with multiple warning signals.

Try a safer example:

```text
You are invited to interview for the Software Intern position.
The interview will be conducted through the company's official careers process.
No payment is requested.
```

Expected result: LOW risk under the current rule set.

## Limitations

- The current detector is rule-based and is an MVP.
- It cannot guarantee that an offer is genuine or fraudulent.
- New scam wording may not be detected until rules are updated.
- URL checks are limited to basic patterns.
- False positives and false negatives are possible.
- Advanced AI explanation and advanced URL reputation checks can be added in future versions.

## Future scope

- Browser extension
- Mobile application
- Screenshot/PDF offer analysis
- Multilingual support
- Advanced URL and domain reputation analysis
- College placement integration
- More advanced AI-assisted explanations

## Team

Add the final team member names and details before publishing the repository.

### Round 2 Login
The prototype includes a simple demo login interface for presentation purposes.
- Demo email: `student@scamshield.com`
- Demo password: `scamshield123`
- After login, the user is taken to the Analyze Offer page.
- This is prototype authentication only; no real user passwords should be used.
