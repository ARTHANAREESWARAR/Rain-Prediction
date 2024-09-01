from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import datetime
import pickle



app = Flask(__name__, template_folder="template")
model = pickle.load(open(r"C:\Users\artha\OneDrive\Desktop\Rain-Prediction-main\models\model1", "rb"))
print("Model Loaded")

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	if request.method == "POST":
		
		
		minTemp = float(request.form['mintemp'])
		
		maxTemp = float(request.form['maxtemp'])
		
		rainfall = float(request.form['rainfall'])
		
		windGustSpeed = float(request.form['windgustspeed'])
		
		windSpeed9am = float(request.form['windspeed9am'])
		
		windSpeed3pm = float(request.form['windspeed3pm'])
		
		humidity9am = float(request.form['humidity9am'])
		
		humidity3pm = float(request.form['humidity3pm'])
		
		pressure9am = float(request.form['pressure9am'])
		
		pressure3pm = float(request.form['pressure3pm'])
		
		temp9am = float(request.form['temp9am'])
		
		temp3pm = float(request.form['temp3pm'])
		location = float(request.form['location'])
		
		winddDir9am = float(request.form['winddir9am'])
		
		winddDir3pm = float(request.form['winddir3pm'])
		
		windGustDir = float(request.form['windgustdir'])
		
		rainToday = float(request.form['raintoday'])

		input_lst = [[location , minTemp , maxTemp , rainfall , 
					 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
					 humidity9am , humidity3pm , pressure9am , pressure3pm , temp9am , temp3pm ,
					 rainToday]]
		pred = model.predict(input_lst)
		output = pred[0]
		if output == 0:
			return render_template("after_sunny.html")
		else:
			return render_template("after_rainy.html")
	return render_template("predictor.html")

if __name__=='__main__':
	app.run(debug=True)