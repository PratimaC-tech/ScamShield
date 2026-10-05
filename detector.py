import re
from urllib.parse import urlparse

RULES = [
    {
        "key": "payment",
        "title": "Payment request",
        "weight": 30,
        "keywords": [
            "registration fee", "registration fees", "processing fee",
            "training fee", "security deposit", "pay to join",
            "pay before joining", "joining fee", "application fee",
            "refundable fee", "deposit money", "pay rs", "pay ₹",
            "payment required", "send money", "transfer money"
        ],
        "explanation": "Legitimate recruitment normally should not require a candidate to pay money simply to obtain a job or internship."
    },
    {
        "key": "urgency",
        "title": "Urgency or pressure",
        "weight": 20,
        "keywords": [
            "act now", "urgent", "immediately", "limited time",
            "today only", "within 24 hours", "last chance",
            "respond immediately", "offer expires", "do not delay"
        ],
        "explanation": "Strong pressure to act quickly can reduce the time available for independent verification."
    },
    {
        "key": "sensitive_data",
        "title": "Sensitive information request",
        "weight": 25,
        "keywords": [
            "aadhaar", "aadhar", "pan card", "pan number",
            "bank account", "bank details", "credit card",
            "debit card", "cvv", "otp", "password",
            "upi pin", "net banking", "login credentials"
        ],
        "explanation": "Sensitive financial or identity information should not be shared with an unverified recruiter or website."
    },
    {
        "key": "suspicious_link",
        "title": "Suspicious URL signal",
        "weight": 20,
        "keywords": [],
        "explanation": "The submitted link contains patterns that deserve additional verification before you continue."
    },
    {
        "key": "guaranteed_job",
        "title": "Unrealistic guarantee",
        "weight": 15,
        "keywords": [
            "guaranteed job", "100% job", "guaranteed placement",
            "guaranteed internship", "no interview", "easy money",
            "earn huge", "guaranteed income"
        ],
        "explanation": "Promises of guaranteed jobs, placements, or unusually easy income can be a warning sign."
    },
    {
        "key": "unprofessional",
        "title": "Unprofessional recruitment language",
        "weight": 10,
        "keywords": [
            "whatsapp only", "telegram only", "contact on whatsapp",
            "send otp", "send your password"
        ],
        "explanation": "Unusual communication requirements or requests for credentials should be independently verified."
    }
]

def normalize(text):
    return re.sub(r"\s+", " ", text.lower()).strip()

def url_signals(url):
    if not url:
        return []

    findings = []
    parsed = urlparse(url if "://" in url else "https://" + url)
    host = parsed.netloc.lower()

    if not host:
        return findings

    suspicious_terms = [
        "bit.ly", "tinyurl", "t.ly", "cutt.ly", "is.gd",
        "free", "verify", "claim", "secure-login"
    ]

    if any(term in host for term in suspicious_terms):
        findings.append("The domain or URL pattern deserves independent verification.")

    if "@" in url:
        findings.append("The URL contains an @ symbol, which can be misleading in a link.")

    if len(url) > 120:
        findings.append("The URL is unusually long and should be checked carefully.")

    # Raw IP address rather than a normal domain
    if re.fullmatch(r"https?://\d{1,3}(?:\.\d{1,3}){3}.*", url.strip().lower()):
        findings.append("The link uses an IP address instead of a normal organization domain.")

    return findings

def analyze_offer(message, url):
    text = normalize(message)
    signals = []
    score = 0

    for rule in RULES:
        if rule["key"] == "suspicious_link":
            continue

        matched = [kw for kw in rule["keywords"] if kw in text]
        if matched:
            signals.append({
                "key": rule["key"],
                "title": rule["title"],
                "explanation": rule["explanation"],
                "matches": matched[:4],
                "severity": "high" if rule["weight"] >= 25 else "medium"
            })
            score += rule["weight"]

    url_findings = url_signals(url)
    if url_findings:
        signals.append({
            "key": "suspicious_link",
            "title": "Suspicious URL signal",
            "explanation": "The submitted URL has one or more patterns that should be independently checked before opening or submitting information.",
            "matches": url_findings,
            "severity": "medium"
        })
        score += 20

    score = min(score, 100)

    if score >= 60:
        level = "HIGH"
        recommendation = "Pause before proceeding. Do not send money or sensitive information until the employer and offer are independently verified."
    elif score >= 30:
        level = "MEDIUM"
        recommendation = "Proceed carefully. Verify the company, recruiter, domain and offer details before sharing information."
    else:
        level = "LOW"
        recommendation = "No major warning pattern was detected by the current rule set, but independently verify the opportunity before proceeding."

    checklist = [
        "Find the company's official website independently rather than relying only on the supplied link.",
        "Check whether the recruiter and job opening can be verified through an official company channel.",
        "Do not pay registration, processing, training or security fees without strong independent verification.",
        "Never share OTPs, passwords, UPI PINs or banking credentials with a recruiter.",
        "Check the email/domain, job description and contact details for inconsistencies.",
        "If uncertain, ask a trusted person or your college placement/career office to review the offer."
    ]

    return {
        "risk_score": score,
        "risk_level": level,
        "signals": signals,
        "signal_count": len(signals),
        "recommendation": recommendation,
        "checklist": checklist,
        "disclaimer": "Risk assessment, not a guarantee. ScamShield cannot confirm with certainty that an offer is genuine or fraudulent."
    }
