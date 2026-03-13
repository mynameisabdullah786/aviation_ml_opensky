from flask import Flask,request,jsonify
import torch
from inference.predict import load_model

app = Flask(__name__)

model = load_model()

@app.route("/predict",methods=["POST"])
def predict():

    data = request.json

    x = torch.tensor(data["features"]).float()

    pred = model(x).detach().numpy()

    return jsonify({"prediction":pred.tolist()})

if __name__ == "__main__":
    app.run()