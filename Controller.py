import pandas as pd
from flask import Flask, request
from Model import *



app = Flask(__name__,static_folder="Static",static_url_path='')
model = Model()

@app.route("/")
def LandingPage():
    return model.GetLandingPage()

@app.route("/LoginPage")
def LoginPage():
    return model.GetLoginPage()

@app.route("/FetchUserData", methods = ["GET", "POST"])
def LoadUserData():
    form = request.form
    return model.GetLoginDetails(form["Username"], form["Password"])

if __name__ == '__main__': app.run(host='0.0.0.0', debug=True)
