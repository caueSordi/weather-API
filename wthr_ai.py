import requests
import tkinter as tk
from tkinter import messagebox

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = ''  # Fill in your OpenWeatherMap API key

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fetch_weather():
    city = city_entry.get()
    params = {
        "q": city,
        "appid": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temperature = kelvin_to_celsius(data['main']['temp'])
        description = data['weather'][0]['description']
        display_weather(city, temperature, description)
        # Store weather data for later use
        global weather_data
        weather_data = {
            'temperature': temperature,
            'description': description
        }
    else:
        messagebox.showerror("Error", "Failed to retrieve weather data. Please check your input or try again later.")

def display_weather(city, temperature, description):
    result_text.set(f"Location: {city}\nTemperature: {temperature:.2f}°C\nDescription: {description}")
    
    if temperature > 30:
        weather_comment.set("It's hot today.")
    elif 20 <= temperature <= 30:
        weather_comment.set("The weather is nice today :)")
    elif 10 <= temperature < 20:
        weather_comment.set("It's cold today.")
    else:
        weather_comment.set("You should wear a coat today.")
    
    if description == 'clear sky':
        weather_advice.set("Remember to use sunscreen.")
    elif description == 'rain':
        weather_advice.set("You will need an umbrella.")
    elif description == 'scattered clouds':
        weather_advice.set("I recommend you to take an umbrella.")
    else:
        weather_advice.set("")

def make_recommendation():
    activity = activity_entry.get().lower().strip()
    if 'weather_data' in globals():
        temperature = weather_data['temperature']
        description = weather_data['description']
    else:
        messagebox.showwarning("No Data", "Weather data not available. Please fetch the weather first.")
        return

    if activity in ['sport', 'exercise', 'train']:
        sport_recommendation(temperature, description)
    elif activity in ['hangout', 'go out with friends']:
        hangout_recommendation(temperature, description)
    elif activity in ['socialize', 'meet new people']:
        social_recommendation(temperature, description)
    elif activity in ['date', 'dating', 'romantic', 'romance']:
        date_recommendation(temperature, description)
    else:
        messagebox.showinfo("Invalid Input", "Invalid activity input.")

def sport_recommendation(temperature, description):
    if temperature > 20 and description in ['clear sky', 'sunny']:
        recommendation.set("The weather is perfect to play tennis or go for a run.")
    elif temperature < 15 and description in ['rain', 'overcast clouds', 'broken clouds']:
        recommendation.set("Maybe it's better to stay inside today, maybe hit the gym or do some yoga.")

def hangout_recommendation(temperature, description):
    if temperature > 20 and description in ['clear sky', 'sunny']:
        recommendation.set("The weather is perfect for a picnic.")
    elif temperature < 15 and description in ['rain', 'overcast clouds', 'broken clouds']:
        recommendation.set("The weather isn't the best for outside activities today, maybe go to the mall or watch a movie at home.")

def social_recommendation(temperature, description):
    if temperature > 20 and description in ['clear sky', 'sunny']:
        recommendation.set("Maybe today try to find new friends, go to a park or a cafe.")
    elif temperature < 15 and description in ['rain', 'overcast clouds', 'broken clouds']:
        recommendation.set("Maybe going outside isn't the best option for now, but you can socialize online, just don't go on Twitter.")

def date_recommendation(temperature, description):
    if temperature > 20 and description in ['clear sky', 'sunny']:
        recommendation.set("What a lovely day to go on a date in the park or maybe a cafe.")
    elif temperature < 15 and description in ['rain', 'overcast clouds', 'broken clouds']:
        recommendation.set("Maybe stay at home, watch a movie, or cook together.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create input fields and buttons
tk.Label(root, text="Enter City:").grid(row=0, column=0)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1)

fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.grid(row=0, column=2)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text).grid(row=1, column=0, columnspan=3)

weather_comment = tk.StringVar()
tk.Label(root, textvariable=weather_comment).grid(row=2, column=0, columnspan=3)

weather_advice = tk.StringVar()
tk.Label(root, textvariable=weather_advice).grid(row=3, column=0, columnspan=3)

tk.Label(root, text="Activity:").grid(row=4, column=0)
activity_entry = tk.Entry(root)
activity_entry.grid(row=4, column=1)

recommend_button = tk.Button(root, text="Get Recommendation", command=make_recommendation)
recommend_button.grid(row=4, column=2)

recommendation = tk.StringVar()
tk.Label(root, textvariable=recommendation).grid(row=5, column=0, columnspan=3)

# Initialize weather_data as a global variable
weather_data = {}

# Run the application
root.mainloop()
