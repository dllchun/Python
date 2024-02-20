import pandas as pd
from datetime import datetime


def get_station_id(station):
    # Prepare station dataframe

    station_header = ["id", "station_name", "cn", "lat", "lon", "hght"]
    station_df = pd.read_csv(
        "/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app6_build_weather_api/additional/data_small/stations.txt",
        skiprows=18,
        sep=",",
        names=station_header,
    )

    req_station_id = station_df.loc[station_df["station_name"].str.strip() == station][
        "id"
    ].values[0]

    full_data = str(req_station_id).zfill(6)

    # print(full_data)
    return full_data


# Prepare weather data


def request_weather(station, date):
    req_station_id = get_station_id(station)

    weather_df_header = ["station_id", "sou_id", "date", "temp", "q_tg"]

    weatherdf = pd.read_csv(
        f"/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app6_build_weather_api/additional/data_small/TG_STAID{req_station_id}.txt",
        skiprows=21,
        sep=",",
        names=weather_df_header,
    )

    req_record = weatherdf.loc[weatherdf["date"] == date]
    req_weather = str(req_record["temp"].values[0])
    return req_weather


# request_weather("ZAGREB-GRIC", 18600102)

# get_station_id("ZAGREB-GRIC")
