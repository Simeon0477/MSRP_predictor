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
        
    ids = session["data"].keys()
    for id in ids:
        id = id.split(" ")[0]
    
    return render_template('index.html')

#définition du point final de la prédication
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    