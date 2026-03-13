import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess():

    df = pd.read_csv("data/opensky_flights.csv")

    df = df.dropna()

    features = [
        "longitude",
        "latitude",
        "baro_altitude",
        "velocity",
        "heading",
        "vertical_rate"
    ]

    X = df[features]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled