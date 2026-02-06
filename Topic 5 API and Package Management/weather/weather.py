from pprint import pprint
import requests
import os

key = os.environ.get('WEATHER_KEY')
print(key)

url = 'https://api.openweathermap.org/data/2.5/weather?q=minneapolis&units=imperial&appid=d3599d17d99dc9d4b0e46ee554f53a63'

data = requests.get(url).json()

pprint(data)

temp = data['main']['temp']
print(temp)