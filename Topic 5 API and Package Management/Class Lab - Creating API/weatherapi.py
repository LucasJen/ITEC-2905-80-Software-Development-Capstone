''' 
Below was created using the video guides as reference with to establish connection and query for the 5-day forecast. 
Claude was used to improve organize syntax and explain common error handling techniques
Comments provided to explain functionality
'''

import os
import requests
from datetime import datetime

# 'global' variable assignments, including api key, lat/lon for location information as well as unit types.
api_key = os.environ.get('WEATHER_KEY') #stores api key in os user env variables
lat = 44.97
lon = -93.26
units = 'metric'
unit_label = 'C' if units == 'metric' else 'F' # suggested by Claude to apply to f string output should units change.
url = 'https://api.openweathermap.org/data/2.5/forecast'

# get_forecast is used to read the json output once a query has already been made
def get_forecast(weather_data, city):
    try:
        print(f'\n5-Day Forecast for {city}:')
        # for loop will loop through keys associated with the 'list' object within the JSON data and create variables assigned to relevant keys within
        for entry in weather_data['list']:
            timestamp = datetime.fromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M') # pulls current time and formats to year-mont-day hour:minute
            temp = entry['main']['temp']
            description = entry['weather'][0]['description']
            wind = entry['wind']['speed']
            print(f'{timestamp} | Temp: {temp}{unit_label} | {description.capitalize()} | Wind: {wind} m/s')
    
    #Common errors expected during api request parsing.
    except KeyError as e:
        print(f'Missing expected data field: {e}')
    except Exception as e:
        print(f'Unexpected error while parsing forecast: {e}')

# the query is completed 
def main():
    try:
        # check to ensure api key is included
        if not api_key:
            raise ValueError('WEATHER_KEY environment variable not set')
        
        params = {'lat': lat, 'lon': lon, 'units': units, 'appid': api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        get_forecast(weather_data, 'Minneapolis') # lat and lon are seperate variables, so including city name is just for formatting.

    # Common errors caught during connecting and requesting items from the API
    except ValueError as e:
        print(f'Configuration error: {e}')
    except requests.exceptions.ConnectionError:
        print('Could not connect to the weather service. Check your internet connection.')
    except requests.exceptions.Timeout:
        print('The request timed out. Try again later.')
    except requests.exceptions.HTTPError as e:
        print(f'HTTP error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

# calls main function when program is ran
if __name__ == '__main__':
    main()