from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from collections import Counter

from database import *
from model import *
from utils import *

app = Flask(__name__)
app.secret_key = "secret"

init_db()


# -------------------- HOME --------------------
@app.route("/")
def index():
    return redirect("/login")


# -------------------- REGISTER --------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        insert_user(name, email, password)
        return redirect("/login")

    return render_template("register.html")


# -------------------- LOGIN --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = get_user(email)
        print("User from DB:", user)

        if user and check_password_hash(user[3], password):
            session["user_id"] = user[0]
            print("Login successful")
            return redirect("/dashboard")

        print("Invalid login")

    return render_template("login.html")


# -------------------- DASHBOARD --------------------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    data = get_all_complaints()

    total = len(data)
    pending = len([d for d in data if d[7] == "Pending"])
    resolved = len([d for d in data if d[7] == "Resolved"])

    # Category chart
    category_counter = Counter([d[3] for d in data])

    # Sentiment chart
    sentiment_counter = Counter([d[4] for d in data])

    # Monthly trend
    month_counter = Counter([str(d[8])[:7] for d in data])

    return render_template(
        "dashboard.html",
        total=total,
        pending=pending,
        resolved=resolved,
        category_labels=list(category_counter.keys()),
        category_counts=list(category_counter.values()),
        sentiment_labels=list(sentiment_counter.keys()),
        sentiment_counts=list(sentiment_counter.values()),
        month_labels=list(month_counter.keys()),
        month_counts=list(month_counter.values())
    )


# -------------------- SUBMIT COMPLAINT --------------------
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        text = request.form["complaint"]

        category = predict_category(text)
        sentiment = analyze_sentiment(text)
        keywords = extract_keywords(text)
        priority = detect_priority(sentiment)

        insert_complaint((
            session["user_id"],
            text,
            category,
            sentiment,
            keywords,
            priority,
            datetime.now(),
        ))

        return redirect("/complaints")

    return render_template("submit_complaint.html")


# -------------------- VIEW COMPLAINTS --------------------
@app.route("/complaints")
def complaints():
    if "user_id" not in session:
        return redirect("/login")

    data = get_all_complaints()
    return render_template("complaints.html", data=data)



# -------------------- RESOLVE COMPLAINT --------------------

@app.route("/resolve/<int:complaint_id>", methods=["POST"])
def resolve_complaint(complaint_id):

    if "user_id" not in session:
        return redirect("/login")

    print("Resolve route HIT:", complaint_id)

    try:
        update_status(complaint_id, "Resolved")
        print("Status updated successfully")

    except Exception as e:
        print("Error updating status:", e)

    return redirect(url_for("complaints"))
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="127.0.0.1", port=5000, debug=True)