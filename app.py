from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "<h2>Flask Vercel v2</h2>"

    return app
