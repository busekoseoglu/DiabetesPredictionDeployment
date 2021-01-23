import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    features = [str(x) for x in request.form.values()]

    
        

    final_features = [np.array(features)]
    prediction = model.predict_proba(final_features)

    output='{0:.{1}f}'.format(prediction[0][1], 2)


    return render_template('index.html',pred='Your probability of diabetes is % {}'.format(str(float(output)*100)))

