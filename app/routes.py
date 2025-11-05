from flask import Flask, request, session, render_template
import pickle as pkl 
from app import app
import json

model = pkl.load(open("./models/model.pkl", "rb"))
app.secret_key = "00091100"

#point final par défaut
@app.route('/')
def home():
    #app.root_path
    with open("./app/static/index.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        session["data"] = data
    
    return render_template('index.html')

#définition du point final de la prédication
@app.route('/predict', methods=['POST'])
def predict():
    year = request.form.get("year")
    cylinder = request.form.get("cylinder")
    HP = request.form.get("HP")
    make = request.form.get("Make")
    engine = request.form.get("Engine Fuel Type")
    driven = request.form.get("Driven_Wheels")
    market = request.form.get("Market Category")
    modele = request.form.get("Model")
    market = request.form.get("Vehicle Size")
    modele = request.form.get("Vehicle Style")
    transmission = request.form.get("Transmission Type")
    
    return render_template('index.html')
    