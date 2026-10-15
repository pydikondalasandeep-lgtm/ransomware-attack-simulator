from flask import Flask, render_template

app = Flask(__name__)


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# TEAM
# =========================================================

@app.route("/team")
def team():
    return render_template("team.html")


# =========================================================
# INCIDENT INTRODUCTION
# =========================================================

@app.route("/incident")
def incident():
    return render_template("incident.html")


# =========================================================
# STAGE 01 — PHISHING
# =========================================================

@app.route("/phishing")
def phishing():
    return render_template("phishing.html")


# =========================================================
# STAGE 02 — INITIAL ACCESS
# =========================================================

@app.route("/initial-access")
def initial_access():
    return render_template("initial-access.html")


# =========================================================
# STAGE 03 — EXECUTION
# =========================================================

@app.route("/execution")
def execution():
    return render_template("execution.html")


# =========================================================
# STAGES 04 + 05 — PERSISTENCE + DISCOVERY
# =========================================================

@app.route("/persistence-discovery")
def persistence_discovery():
    return render_template("persistence-discovery.html")


# =========================================================
# STAGE 06 — IMPACT + RANSOMWARE
# =========================================================

@app.route("/impact")
def impact():
    return render_template("impact.html")


# =========================================================
# STAGE 07 — INCIDENT RESPONSE
# =========================================================

@app.route("/response")
def response():
    return render_template("response.html")


# =========================================================
# START SERVER
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)