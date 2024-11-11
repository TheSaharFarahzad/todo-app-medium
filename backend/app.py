from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    # Home route with a message and available API routes
    return "Welcome to the ToDo API! Available routes: /tasks"
