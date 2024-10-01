import requests
from datetime import datetime

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def get_weather_data(city):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    API_KEY = ''  # Fill in your OpenWeatherMap API key
    params = {
        "q": city,
        "appid": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = kelvin_to_celsius(data['main']['temp'])
        description = data['weather'][0]['description']
        return temperature, description
    
    return None, None
def tell_date():
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    print("Current Date =", current_date)

def tell_time_of_day():
    print('hello')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    hour = int(current_time.split(':')[0])
    if 6 <= hour < 12:
        print("Good morning!")
    elif 12 <= hour < 18:
        print("Good afternoon!")
    elif 18 <= hour < 22:
        print("Good evening!")
    else:
        print("Good night!")

def tell_weather(city):
    temperature, description = get_weather_data(city)
    if temperature is not None and description is not None:
        print(f"Location: {city}")
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
    else:
        print("Could not retrieve weather data")


def should_sleep():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = int(current_time.split(':')[0])
    if 22 <= hour < 5:
        print("You should be sleeping now!")
    else:
        print("the day is still young, keep going!")

def shouldnt_be_outside(temperature, description):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = int(current_time.split(':')[0])
    if temperature < 10 and description in ['rain', 'overcast clouds', 'broken clouds'] and hour > 22 and hour < 5:
        print("Maybe going outside isn't the best option for now, but you can socialize online, just don't go on Twitter")

def comemorative_dates (): 
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    if current_date.startswith("25/12"):
        print("Merry Christmas!")
    elif current_date.startswith("31/12"):
        print("Happy New Year!")
    else:
        print("")




tell_date()
comemorative_dates()
tell_time_of_day()
city = input("Location name: ")
tell_weather(city)
should_sleep()

