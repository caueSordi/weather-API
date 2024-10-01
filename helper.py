import requests
from datetime import datetime
import sys
import time

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def get_weather_data(city):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    API_KEY = '51624c701e2ceaefb78368f8876959f2'  # Fill in your OpenWeatherMap API key
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
    typing(f"Current Date = {current_date}")

def tell_time_of_day():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    typing(f"Current Time = {current_time}")
    hour = int(current_time.split(':')[0])
    if 6 <= hour < 12:
        typing("Good morning!")
    elif 12 <= hour < 18:
        typing("Good afternoon!")
    elif 18 <= hour < 22:
        typing("Good evening!")
    else:
        typing("Good night!")

def tell_weather(city):
    temperature, description = get_weather_data(city)
    if temperature is not None and description is not None:
        typing(f"Location: {city}")
        typing(f"Temperature: {temperature:.2f}°C")
        if temperature > 30:
            typing("It's hot today")
        elif 20 <= temperature <= 30:
            typing("The weather is nice today :)")
        elif 10 <= temperature < 20:
            typing("It's cold today")
        elif temperature < 10:
            typing("You should wear a coat today")
        typing(f"Today there will be: {description}")
    else:
        typing("Could not retrieve weather data")

def should_sleep():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = int(current_time.split(':')[0])
    if 22 <= hour < 5:
        typing("You should be sleeping now!")
    else:
        typing("The day is still young, keep going!")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        hour, minute, second = map(int, current_time.split(':'))
        remaining_seconds = 24 * 3600 - (hour * 3600 + minute * 60 + second)
        remaining_hours = remaining_seconds // 3600
        remaining_minutes = (remaining_seconds % 3600) // 60
        remaining_seconds = remaining_seconds % 60
        typing(f"You have {remaining_hours} hours, {remaining_minutes} minutes, and {remaining_seconds} seconds remaining in the day.")

def shouldnt_be_outside(temperature, description):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = int(current_time.split(':')[0])
    if temperature < 10 and description in ['rain', 'overcast clouds', 'broken clouds'] and hour > 22 and hour < 5:
        typing("Maybe going outside isn't the best option for now, but you can socialize online, just don't go on Twitter")

def comemorative_dates(): 
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    if current_date.startswith("25/12"):
        typing("Merry Christmas!")
    elif current_date.startswith("31/12"):
        typing("Happy New Year!")
    else:
        typing("")

def typing(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # To move to the next line after the message is printed



def get_name():
    name = input("What's your name? ")
    typing(f"Nice to meet you, {name}!")

typing("Hello! I am your personal assistant.")
get_name()
tell_date()
comemorative_dates()
tell_time_of_day()
city = input("Location name: ")
tell_weather(city)
should_sleep()

