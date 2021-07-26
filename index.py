from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h2>Flask Vercel</h2>"
