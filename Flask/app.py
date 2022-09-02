from pickle import TRUE
from flask import Flask, redirect, request, url_for, render_template
from flask_wtf import Form
from wtforms import BooleanField, SubmitField


class MyForm(Form):
    var = BooleanField()

    submit = SubmitField()


app = Flask(__name__)


flag = TRUE


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/form.html")
def form():
    return render_template("form.html")


"""
@app.route('/string',methods=['GET','POST'])
def get_input():
    form = MyForm()
    if form.valid

"""
app.run()
