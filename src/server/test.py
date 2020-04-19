from flask import Flask, url_for, render_template, abort
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test/<username>")
def test(username):
    print(escape(username))
    return "User %s" % escape(username)


@app.route("/user/<int:id>")
def user(id):
    return "User's id is %s" % escape(id)


@app.route("/error")
def error():
    return abort(401)


@app.errorhandler(401)
def page_not_found(error):
    return {"key": "value"}, 401
