from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


app.run()
