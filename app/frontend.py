import os
from flask import Flask, render_template
from threading import Lock

app = Flask(
    __name__,
    template_folder=os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "templates"
    ),
)


questions = []
lock = Lock()


@app.route("/")
def index():
    with lock:
        return render_template("index.html", questions=questions)


def run_flask_server():
    app.run(host="0.0.0.0", port=5005, debug=True, use_reloader=False)


def add_question(question):
    with lock:
        questions.append(question)
