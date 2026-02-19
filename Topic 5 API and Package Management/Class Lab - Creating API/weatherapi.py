import os
import requests
from datetime import datetime

api_key = os.environ.get('WEATHER_KEY')
lat = 44.97
lon = -93.26
units = 'metric'
unit_label = 'C' if units == 'metric' else 'F'
url = 'https://api.openweathermap.org/data/2.5/forecast'

def get_forecast(weather_data, city):
    try:
        print(f'\n5-Day Forecast for {city}:')
        print('-' * 60)
        for entry in weather_data['list']:
            timestamp = datetime.fromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M')
            temp = entry['main']['temp']
            description = entry['weather'][0]['description']
            wind = entry['wind']['speed']
            print(f'{timestamp} | Temp: {temp}{unit_label} | {description.capitalize()} | Wind: {wind} m/s')
    except KeyError as e:
        print(f'Missing expected data field: {e}')
    except Exception as e:
        print(f'Unexpected error while parsing forecast: {e}')

def main():
    try:
        if not api_key:
            raise ValueError('WEATHER_KEY environment variable not set')
        
        params = {'lat': lat, 'lon': lon, 'units': units, 'appid': api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        get_forecast(weather_data, 'Minneapolis')

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

if __name__ == '__main__':
    main()