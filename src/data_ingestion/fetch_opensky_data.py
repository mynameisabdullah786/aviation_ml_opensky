import requests
import pandas as pd

URL = "https://opensky-network.org/api/states/all"

def fetch_flight_data():

    r = requests.get(URL)
    data = r.json()["states"]

    columns = [
        "icao24","callsign","origin_country","time_position",
        "last_contact","longitude","latitude","baro_altitude",
        "on_ground","velocity","heading","vertical_rate"
    ]

    df = pd.DataFrame(data)

    df = df.iloc[:, :len(columns)]
    df.columns = columns

    df.to_csv("data/opensky_flights.csv", index=False)

    print("OpenSky dataset saved")

if __name__ == "__main__":
    fetch_flight_data()