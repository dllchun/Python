import pandas as pd
from flask import Flask, render_template
import requests
import json

# from data import request_weather


app = Flask(
    __name__,
    template_folder="/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app6_build_weather_api/templates",
    static_folder="/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app6_build_weather_api/static",
)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    station_id = str(station).zfill(6)
    print(station_id)
    weather_df_header = ["station_id", "sou_id", "date", "temp", "q_tg"]
    filename = f"/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app6_build_weather_api/additional/data_small/TG_STAID{station_id}.txt"
    df = pd.read_csv(
        filename,
        skiprows=21,
        sep=",",
        names=weather_df_header,
        parse_dates=["date"],
    )
    temperature = df.loc[df["date"] == date]["temp"].squeeze() / 10
    return {"station": station_id, "date": date, "temperature": temperature}


@app.route("/api/v1/translator/<word>")
def translate(word):
    if word.isupper():
        definition = word.lower()
    else:
        baseURL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        fullURL = baseURL + word

        response = requests.get(fullURL)
        content = response.json()

        meaning = content[0]["meanings"]
        definition = meaning[0]["definitions"][0]["definition"]

    return {"word": word, "definiton": definition}


app.run(debug=True)
