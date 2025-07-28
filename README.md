
# Ask Anyone Website

This is a simple web application where users can write a name and message, and it gets sent to your email.

## Setup

1. Update your email and password in `app.py` for `send_email()` function.
2. Use an app password if using Gmail with 2FA.
3. To run locally:

```bash
pip install -r requirements.txt
python app.py
```

## Deploy on Render

- Push this project to GitHub.
- Create a new Web Service on [Render](https://render.com/).
- Connect your GitHub repo.
- Use the following settings:
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `python app.py`
