import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = ''

def sport_recommendation(temperature, description):
    if temperature > 20 and description == 'clear sky' or description == 'sunny':
        print("the weather is perfect to play tennis or go for a run")
    elif temperature < 15 and description == 'rain' or description == 'overcast clouds'or description == 'broken clouds':
        print("maybe it's better to stay inside today, maybe hit the gym do some yoga") 


def hangout_recommendation(temperature, description):
    if temperature > 20 and description == 'clear sky' or description == 'sunny':
        print("The weather is perfect for a picnic ")
    elif temperature < 15 and description == 'rain' or description == 'overcast clouds'or description == 'broken clouds':
        print("the weather isn't the best for outside activities today, maybe go to the mall or watch a movie at home")

def social_recommendation():
    if temperature >20 and description == 'clear sky' or description == 'sunny':
        print("maybe today try to find new friends, go to a park or a cafe \n")
        print(' maybe a club or a bar')
    elif temperature < 15 and description == 'rain' or description == 'overcast clouds'or description == 'broken clouds':
        print(" maybe go outside isn't the best option for now, but you can socialize online, just don't go on twitter \n")


def date_recommendation():
    if temperature > 20 and description == 'clear sky' or description == 'sunny':
        print("what a lovely day to go on a date on the park or maybe a cafe")
    elif temperature < 15 and description == 'rain' or description == 'overcast clouds'or description == 'broken clouds':
        print("maybe stay at home, watch a movie or cook together")

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
    if temperature > 30:
        print("It's hot today")
    elif temperature < 20 > 10:
        print("It's cold today")
    elif temperature <10:
        print("you should wear a coat today")
    else:
        print("the weather is nice today :)")

    print(f"timezone: {time_zone}")
    print(f"Today there will be: {description}")
    if description == 'clear sky':
        print("Remember to use sun screen")
    elif description == 'rain':
        print("you will need an umbrella")
    elif description == 'scattered clouds':
        print("I recomend you to take an umbrella")


match = input("what are you planning to do today? \n")
if match == 'sport':
    sport_recommendation(temperature, description)

elif match == 'hangout':
    hangout_recommendation(temperature, description)

elif match == 'social':
    social_recommendation()

elif match == 'date':
    date_recommendation()


