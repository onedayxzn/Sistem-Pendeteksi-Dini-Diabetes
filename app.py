from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/check/',  methods=['GET', 'POST'])
def check():

    # if request.method == "POST":

    return render_template('check.html')


if __name__ == '__main__':
    app.run(debug=True)
