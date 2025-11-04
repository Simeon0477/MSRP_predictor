from flask import Flask, request, jsonify, render_template
import pickle as pkl 
from app import app

model = pkl.load(open("./models/model.pkl", "rb"))

#point final par défaut
@app.route('/')
def home():
    return render_template('index.html')

#définition du point final de la prédication
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    