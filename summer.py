import requests
from datetime import datetime
import sys
import time
import os

# Global variable to store the user's location
user_location = None

# Function to save user data to a file
def save_user_data(name, location):
    with open("user_data.txt", "a") as file:
        file.write(f"{name},{location}\n")

# Function to load user data from the file
def load_user_data():
    if os.path.exists("user_data.txt"):
        with open("user_data.txt", "r") as file:
            return [line.strip().split(',') for line in file.readlines()]
    return []

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather_data(city):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    API_KEY = '51624c701e2ceaefb78368f8876959f2'  # Replace with your OpenWeatherMap API key
    params = {"q": city, "appid": API_KEY}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = kelvin_to_celsius(data['main']['temp'])
        description = data['weather'][0]['description']
        return temperature, description
    return None, None

def typing(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # New line after the message

def greet_user():
    global user_location
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = int(current_time.split(':')[0])
    if 6 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon!"
    elif 18 <= hour < 22:
        greeting = "Good evening!"
    else:
        greeting = "Good night!"
    
    current_date = now.strftime("%d/%m/%Y")
    typing(f"{greeting} Today's date is {current_date}, and the time is {current_time}.")

    # Load user data and ask if the user wants to be remembered
    users = load_user_data()
    typing("Have we met before? (yes/no): ")
    met_before = input().strip().lower()
    
    if met_before == "yes":
        typing("Please enter your name: ")
        name = input().strip()
        
        # Check if the entered name exists in the saved user data
        found_user = None
        for user in users:
            if user[0].lower() == name.lower():
                found_user = user
                break
        
        if found_user:
            location = found_user[1]
            user_location = location  # Store location globally
            typing(f"Welcome back, {name} from {location}! How can I assist you today?")
        else:
            typing(f"Hi, {name}, but I couldn't find you in my records. Let me get to know you!")
            typing("Please tell me your location: ")
            location = input().strip()
            save_user_data(name, location)
            user_location = location  # Store location globally
            typing(f"Nice to meet you, {name} from {location}! How can I assist you today?")
    else:
        typing("What’s your name?")
        name = input("Your Name: ")
        typing(f"Nice to meet you, {name}! How can I assist you today?")
        typing("Please tell me your location: ")
        location = input().strip()
        save_user_data(name, location)
        user_location = location  # Store location globally
    
    return name

def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def tell_date():
    current_date = datetime.now().strftime("%d/%m/%Y")
    typing(f"Today's date is: {current_date}")

def tell_time():
    current_time = get_time()
    typing(f"The current time is: {current_time}")
    hour = int(current_time.split(':')[0])
    if 6 <= hour < 12:
        typing("Good morning!")
    elif 12 <= hour < 18:
        typing("Good afternoon!")
    elif 18 <= hour < 22:
        typing("Good evening!")
    else:
        typing("Good night!")

def tell_weather(city=None):
    global user_location
    
    if user_location and not city:
        city = user_location  # Use stored location if no city is provided
    
    if city:
        temperature, description = get_weather_data(city)
        if temperature is not None and description is not None:
            typing(f"Location: {city}")
            typing(f"Temperature: {temperature:.2f}°C")
            typing(f"Condition: {description}")

            condition = weather_extreme_conditions(description)
        else:
            typing(f"Sorry, I couldn’t retrieve weather data for {city}. Please try again later.")
    else:
        typing("Sorry, I don't have your location information.")

def weather_extreme_conditions(description):
    if "rain" in description or "storm" in description or "snow" in description:
        typing ("bad weather awaits you outside, it's better to stay indoors and be safe")
        return "bad"
    elif "clear" in description or "cloud" in description:
        typing("The weather is nice today, you can go outside and enjoy")
        return "good"
    elif "wind" in description or "haze" in description or "mist" in description:
        typing("kinda foggy outside, be careful when driving")
        return "bad"
    return "normal"

def add_task(task):
    with open("todo_list.txt", "a") as file:
        file.write(f"{task}\n")
    typing(f"Task '{task}' added.")

def remove_task(task):
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
        with open("todo_list.txt", "w") as file:
            removed = False
            for line in tasks:
                if line.strip("\n") != task:
                    file.write(line)
                else:
                    removed = True
        if removed:
            typing(f"Task '{task}' removed.")
        else:
            typing(f"Task '{task}' not found.")
    except FileNotFoundError:
        typing("No tasks found to remove.")

def show_tasks():
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
        if tasks:
            typing("Here are your tasks:")
            for i, task in enumerate(tasks, start=1):
                typing(f"{i}. {task.strip()}")
        else:
            typing("No tasks found!")
    except FileNotFoundError:
        typing("No tasks found!")

def manage_tasks():
    while True:
        action = input("What would you like to do? (add: task, remove: task, show, quit): ").strip().lower()
        if action.startswith("add:"):
            task = action[5:].strip()
            add_task(task)
        elif action.startswith("remove:"):
            task = action[8:].strip()
            remove_task(task)
        elif action == "show":
            show_tasks()
        elif action == "quit":
            typing("Exiting the to-do list manager.")
            break
        else:
            typing("Invalid command, please try again.")

def main():
    name = greet_user()
    while True:
        command = input(f"{name}, what would you like me to do? >> ").lower()
        if "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "weather" in command:
            tell_weather()  # Use stored location if no city is specified
        elif "tasks" in command:
            manage_tasks()
        elif "exit" in command:
            typing(f"Goodbye, {name}! Have a great day!")
            break
        else:
            typing("I'm not sure how to handle that yet. Try 'time', 'date', 'weather', or 'tasks'.")

if __name__ == "__main__":
    main()
