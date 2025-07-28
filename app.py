
from flask import Flask, request, render_template_string
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

html_template = open("templates/index.html").read()

@app.route("/", methods=["GET"])
def home():
    return render_template_string(html_template)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    message = request.form["message"]
    send_email(name, message)
    return "<h1>Message Sent Successfully!</h1><a href='/'>Go back</a>"

def send_email(name, message):
    email_address = "youremail@example.com"  # Change to your email
    email_password = "yourpassword"          # Use app password if using Gmail with 2FA

    msg = EmailMessage()
    msg["Subject"] = f"New Message from {name}"
    msg["From"] = email_address
    msg["To"] = email_address
    msg.set_content(f"Message from {name}:{message}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)
