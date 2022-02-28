from email import header
from sqlite3 import Row
from flask import render_template
import csv
import pandas as pd

class Model:
    def GetLandingPage(self):
        return render_template('index.html')


    def GetLoginPage(self):
        return render_template("LoginPage.html")

    def GetLoginDetails(self, Username, Password):
        df = pd.read_csv("ClientsData.csv")
        print(df.to_string())
        print(df.loc["Username", "Password"])

        if Username == UserName:
            print("correct")
            return render_template()
        

