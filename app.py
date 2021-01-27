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
    features = []
    for x in request.form.values():
        features.append(x)

    for col in features:
        if col == "":
            return render_template('index.html',pred='You have to fill all *')
        else:
            
            final_features = [np.array(features)]
            prediction = model.predict_proba(final_features)

            output='{0:.{1}f}'.format(prediction[0][0], 2)


            return render_template('index.html',pred='Your probability of diabetes is % {}'.format(str(float(output)*100)))

if __name__ == "__main__":
    app.run(debug=True)
