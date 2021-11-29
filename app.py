from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)


@app.route('/')
def cover():
    return render_template('cover.html')


# def home(/home):
#     return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
