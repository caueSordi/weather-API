import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '1970964766849a2799302cc1b7e1fdab'


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

CITY= input("location name: ")

params = {
    "q": CITY,
    "appid": API_KEY
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = kelvin_to_celsius(data['main']['temp'])  # Extract temperature from 'main' section
    city_name = data['name']  #pick the name on the data 
    time_zone = data['timezone']  #pick the time zone on the data
    description = data['weather'][0]['description']  # picks the description from the raw data, 'weather is the group [0] is the position of the wanted info and  'descriptiom' is the wanetd info
    print(f"location: {city_name}")
    print(f"temperature: {temperature:.2f}°C")
    print(f"timezone: {time_zone}")
    print(f"Today there will be: {description}")
    print('have a nice day :)')
else:
    print("Failed ", response.status_code)
