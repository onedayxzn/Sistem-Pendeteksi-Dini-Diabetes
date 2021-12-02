import joblib
import numpy as np
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/check/')
def check():
    return render_template('check.html')


@app.route('/results/', methods=['GET', 'POST'])
def results():

    if request.method == "POST":

        Pregnancies = request.form.get('Pregnancies')
        Glucose = request.form.get('Glucose')
        BloodPressure = request.form.get('BloodPressure')
        SkinThickness = request.form.get('SkinThickness')
        Insulin = request.form.get('Insulin')
        Age = request.form.get('Age')
        BMI = request.form.get('BMI')

        try:
            prediction = preprocessDataAndPredict(
                Pregnancies,  Glucose, BloodPressure, SkinThickness, Insulin, Age, BMI)

            return render_template('results_check.html', prediction=prediction)

        except ValueError:
            return "Please Enter valid values"

        pass
    pass


def preprocessDataAndPredict(Pregnancies,  Glucose, BloodPressure, SkinThickness, Insulin, Age, BMI):

    # keep all inputs in array
    test_data = [Pregnancies,  Glucose, BloodPressure,
                 SkinThickness, Insulin, Age, BMI]
    print(test_data)

    # convert value data into numpy array
    test_data = np.array(test_data)

    # reshape array
    test_data = test_data.reshape(1, -1)
    print(test_data)

    # open file
    file = open("content/Diabetes_model.pkl", "rb")

    # load trained model
    trained_model = joblib.load(file)

    # predict
    prediction = trained_model.predict(test_data)

    return prediction

    pass


@app.route('/description/')
def description():
    return render_template('description.html')


if __name__ == '__main__':
    app.run(debug=True)
