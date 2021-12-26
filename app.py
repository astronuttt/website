from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, to everyone!</p>"


@app.route("/about")
def about():
    return "<p>This is about page</p>"