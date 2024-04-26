import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '1970964766849a2799302cc1b7e1fdab'  # Fill in your OpenWeatherMap API key

def sport_recommendation(temperature, description):
    if temperature > 20 and description in ['clear sky', 'sunny']:
        print("The weather is perfect to play tennis or go for a run")
    elif temperature < 15 and description in ['rain', 'overcast clouds', 'broken clouds']:
        print("Maybe it's better to stay inside today, maybe hit the gym or do some yoga")

def hangout_recommendation(temperature, description):
    if temperature > 20 and description in ['clear sky', 'sunny']:
        print("The weather is perfect for a picnic")
    elif temperature < 15 and description in ['rain', 'overcast clouds', 'broken clouds']:
        print("The weather isn't the best for outside activities today, maybe go to the mall or watch a movie at home")

def social_recommendation(temperature, description):
    if temperature > 20 and description in ['clear sky', 'sunny']:
        print("Maybe today try to find new friends, go to a park or a cafe")
        print("Maybe a club or a bar")
    elif temperature < 15 and description in ['rain', 'overcast clouds', 'broken clouds']:
        print("Maybe going outside isn't the best option for now, but you can socialize online, just don't go on Twitter")

def date_recommendation(temperature, description):
    if temperature > 20 and description in ['clear sky', 'sunny']:
        print("What a lovely day to go on a date in the park or maybe a cafe")
    elif temperature < 15 and description in ['rain', 'overcast clouds', 'broken clouds']:
        print("Maybe stay at home, watch a movie, or cook together")

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

CITY = input("Location name: ")

params = {
    "q": CITY,
    "appid": API_KEY
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = kelvin_to_celsius(data['main']['temp'])  # Extract temperature from 'main' section
    description = data['weather'][0]['description']  # Extract description
    print(f"Location: {CITY}")
    print(f"Temperature: {temperature:.2f}°C")
    if temperature > 30:
        print("It's hot today")
    elif 20 <= temperature <= 30:
        print("The weather is nice today :)")
    elif 10 <= temperature < 20:
        print("It's cold today")
    elif temperature < 10:
        print("You should wear a coat today")

    print(f"Today there will be: {description}")
    if description == 'clear sky':
        print("Remember to use sunscreen")
    elif description == 'rain':
        print("You will need an umbrella")
    elif description == 'scattered clouds':
        print("I recommend you to take an umbrella")

    match = input("What are you planning to do today? \n")
    if match == 'sport':
        sport_recommendation(temperature, description)
    elif match == 'hangout':
        hangout_recommendation(temperature, description)
    elif match == 'social':
        social_recommendation(temperature, description)
    elif match == 'date':
        date_recommendation(temperature, description)
    else:
        print("Invalid input.")
else:
    print("Failed to retrieve weather data. Please check your internet connection or try again later.")
