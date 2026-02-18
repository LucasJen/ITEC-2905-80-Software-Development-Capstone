import os
import requests
from pprint import pprint
import datetime

# Minneapolis
lat = 44.97
lon = -93.26
units = 'metric'  # change to 'imperial' for quantities in Fahrenheit, miles per hour etc.

api_key = os.environ['WEATHER_KEY']  # Set this environment variable on your computer

url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'

response = requests.get(url)
weather_forecast = response.json()
pprint(weather_forecast)

list_forecast = weather_forecast['list']
for forecast in list_forecast:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    weather_description = forecast['weather'][0]['description']
    wind_speed = forecast['wind']['speed']
    date = datetime.fromtimestamp(timestamp).strftime("%m-%d-%Y at %I:%M %p")
    print(f'In Minneapolis, on {date}, the temperature will be {temp:.2f}F.\n'
    f'The weather will be {weather_description}, and the wind speed will be {wind_speed:.2f} mph.\n')


# error handling:

"""

when connecting to api (url)
when querying api
when searching api for specific terms
potential error handling for env variables
error handling for location data, are the coords real?
any input validation for user input


"""