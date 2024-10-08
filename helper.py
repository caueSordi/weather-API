import requests
from datetime import datetime
import sys
import time

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
        in_case_of_radiation()
        typing(" I'm sure {city} is a lovely place, but I can't get the weather data for it. Please try again later.\n maybe I'll travel to {city} someday!")

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
        typing(f"You have {remaining_hours} hours, {remaining_minutes} minutes, and {remaining_seconds} seconds remaining in the day.\n enjoy while you still can :)")

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

def in_case_of_radiation():
    typing("sending bombs to your location <3.\n Stay safe!")

def get_name():
    name = input("What's your name? ")
    typing(f"Nice to meet you, {name}!")
    typing(f" {name} is a lovely name! I would call my first born {name} if I could.\n you know, if I was a human and could have children.\n but I'm not, so I can't. \n I'm a program.no children, no emotions, just a code \n I'm sorry, I'm rambling again. \n What can I do for you today?")






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
            typing("Here are your tasks for today:")
            for i, task in enumerate(tasks, start=1):
                typing(f"{i}. {task.strip()}")
        else:
            typing("No tasks found!")
    except FileNotFoundError:
        typing("No tasks found!")

def mark_done():
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            typing("No tasks to mark as done.")
            return
        
        show_tasks()
        task_num = int(input("Enter the task number you've completed: ")) - 1

        if 0 <= task_num < len(tasks):
            task = tasks[task_num].strip()
            tasks.pop(task_num)
            
            with open("todo_list.txt", "w") as file:
                file.writelines(tasks)
            
            typing(f"Task '{task}' marked as done.")
        else:
            typing("Invalid task number.")
    except FileNotFoundError:
        typing("No tasks found!")
    except ValueError:
        typing("Please enter a valid number.")

def manage_tasks():
    while True:
        action = input("What would you like to do? (add: task, remove: task, done, show, quit): ").strip().lower()
        
        if action.startswith("add:"):
            task = action[5:].strip()
            add_task(task)
        
        elif action.startswith("remove:"):
            task = action[8:].strip()
            remove_task(task)
        
        elif action == "done":
            mark_done()
        
        elif action == "show":
            show_tasks()

        elif action == "quit":
            typing("Exiting the to-do list manager.")
            break

        else:
            typing("Invalid command, please try again.")












typing("Hello! I am your personal assistant.")
get_name()
tell_date()
comemorative_dates()
tell_time_of_day()
city = input("Location name: ")
tell_weather(city)
should_sleep()
manage_tasks()

