from flask import Flask, request, jsonify, render_template
import pickle as pkl 
from app import app
import json

model = pkl.load(open("{{url_for('models', filename='model.pkl')}}", "rb"))

#point final par défaut
@app.route('/')
def home():
    with open("{{url_for('static', filename='style.css')}}", "r", encoding="utf-8") as file:
        data = json.load(file)
    return render_template('index.html', data=data)

#définition du point final de la prédication
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    