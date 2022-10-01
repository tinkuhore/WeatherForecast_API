from datetime import datetime
import requests
from timezonefinder import TimezoneFinder
import pytz

API_KEY = "d15bc915024f98f126cc1c5c33cd9374"
API_CALL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


def weather(city):
    global dict
    try:
        response = requests.get(API_CALL.format(city, API_KEY))
        data = response.json()
        tz = TimezoneFinder().timezone_at(lng=data['coord']['lon'], lat=data['coord']['lat'])

        local_time = datetime.now(pytz.timezone(tz)).strftime("%I:%M %p")
        if len(data) != 0:
            dict = {'city': city, 'country': data['sys']['country'], 'location': data['coord'],
                    'local_time': local_time,
                    'description': data['weather'][0]['description'],
                    'temp': round(data['main']['temp'] - 273),
                    'feels_like': round(data['main']['feels_like'] - 273),
                    'temp_min': round(data['main']['temp_min'] - 273),
                    'temp_max': round(data['main']['temp_max'] - 273),
                    'humidity': data['main']['humidity'], 'wind_speed': round(data['wind']['speed'])}

        else:
            print('Failed to fetch any update.')

    except Exception as e:
        dict = None
        print("API_CALL Failed! Error : ", e)

    return dict

