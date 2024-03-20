import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = ''


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

    if temperature > 20 and description == 'clear sky' or description == 'scattered clouds' :
        print("The weather is perfect for a picnic")
    elif temperature <15 and description == 'rain' or description == 'overcast clouds'or description == 'broken clouds':
        print("such a cozy day to watch a film right?")
        answer = input("do you have a partner to watch it with?\n")
        
        if answer == 'yes':
            print("you are lucky")
        elif answer == 'no':
            print("you should call someone \n")
        else:
            print("I don't know what to say about that")
            lonely = input("do you have someone to call? \n")
            if lonely == 'yes':
                print("then you problably should call them")
            else:
                print("it's okay to be alone sometimes, but there's a whole of people out there waiting for you to meet them")

        
    print('have a nice day :)')
else:
    print("Failed ", response.status_code)
