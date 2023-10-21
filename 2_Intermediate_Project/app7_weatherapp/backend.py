import requests as r
import pandas as pd
from datetime import datetime

api_key = "79b749d6f5bd7aecd7fd1bd622b20d3e"


def get_data(place, forecast_days):
    base_url = (
        f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    )
    # Request
    response = r.get(base_url)

    # Load Data
    data = response.json()

    # Filter Data from the json

    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    get_data(place="Tokyo", forecast_days=2)
