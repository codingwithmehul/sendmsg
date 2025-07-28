from flask import Flask, request, render_template
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# Load email credentials from environment variables
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form.get("email", "No email provided")
    message = request.form["message"]

    send_email(name, email, message)
    return "<h1>Message Sent Successfully!</h1><a href='/'>Go back</a>"

def send_email(name, email, message):
    msg = EmailMessage()
    msg["Subject"] = f"New Message from {name}"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg.set_content(f"From: {name}\nEmail: {email}\n\nMessage:\n{message}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
