from flask import Flask, request, session, render_template
import pickle as pkl 
from app import app
import json
import numpy as np
import pandas as pd

model = pkl.load(open("./models/model.pkl", "rb"))
scaler = pkl.load(open("./models/scaler.pkl", "rb"))
onehot_enc = pkl.load(open("./models/onehot_enc.pkl", "rb"))
target_enc = pkl.load(open("./models/target_enc.pkl", "rb"))

app.secret_key = "00091100"

with open("./app/static/onehot_index.json", "r", encoding="utf-8") as file:
    onehot = json.load(file)
with open("./app/static/target_index.json", "r", encoding="utf-8") as file:
    target = json.load(file)

#point final par défaut
@app.route('/')
def home():
    session["price"] = 0.0
    
    session["min"] = 0.0
    
    session["max"] = 0.0

    #app.root_path
    with open("./app/static/index.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        session["data"] = data
    with open("./app/static/num_index.json", "r", encoding="utf-8") as file:
        nums = json.load(file)
        session["nums"] = nums
        
    return render_template('index.html')

#définition du point final de la prédication
@app.route('/predict', methods=['POST'])
def predict():   
    numerical_vals = {}
    onehot_vals = {}
    target_vals = {}
    
    #Récuperation des valeurs
    for key in session["nums"]:
        numerical_vals[key] = request.form.get(key)   
    for key in onehot:
        onehot_vals[key] = request.form.get(key)   
    for key in target:
        target_vals[key] = request.form.get(key)
        
    #Création de dataframe
    num_df = pd.DataFrame([numerical_vals])
    ohe_df = pd.DataFrame([onehot_vals])
    tg_df = pd.DataFrame([target_vals])
    
    #Encodage
    ohe_df = pd.DataFrame(onehot_enc.transform(ohe_df), columns=onehot_enc.get_feature_names_out())
    tg_df = pd.DataFrame(target_enc.transform(tg_df), columns=target)
    df = pd.concat([num_df, ohe_df, tg_df], axis = 1)
    df = scaler.transform(df)
    
    #Prédiction
    pred = model.predict(df)[0]
    session["price"] = pred
    session["min"] = pred - 4225
    session["max"]  = pred + 4225
    
    return render_template('index.html')
    