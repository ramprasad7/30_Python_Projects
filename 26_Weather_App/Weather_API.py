import datetime
import json
from typing import Final, Any
import requests
from Model import Weather, dt


API_KEY: Final[str] = '3ceac4ce852db1fe0d2e4cde31d6205f'
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'


def get_weather(city_name: str, mock: bool = True) -> dict:
    if mock:
        with open('dummy_data.json', 'r') as file:
            return json.load(file)

    payload: dict = {'q' : city_name, 'appid': API_KEY, 'units': 'metric'}
    request = requests.get(url=BASE_URL, params=payload)

    data: dict = request.json()

    with open('dummy_data.json', 'w') as file:
        json.dump(data, file)

    return data


def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get('list')

    if not days:
        raise Exception(f'Problem with json: {weather}')

    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather := day.get('weather')),
                             description=weather[0].get('description')
                             )
        list_of_weather.append(w)

    return list_of_weather


