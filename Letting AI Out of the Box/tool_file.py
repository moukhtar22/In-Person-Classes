import datetime
from gpiozero import OutputDevice
from ollama import chat, ChatResponse
import requests

relay = OutputDevice(10, active_high = True)

def say_hello():
    # say hello
    response = 'hello'
    return response

def say_goodbye():
    # say goodbye
    response = 'goodbye'
    return response

def close_script():
    # Turn script off
    exit()
    # return 'shutting down'
    
def time():
     #provide current time
     response = datetime.datetime.now().strftime("%H:%M:%S")
     return response

def weather():
    key = '89fedce1f4141fbd44b06e9a8e625a8a'
    lat = '35.5947'
    lon = '-82.5545'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=imperial'
    response = requests.get(url).json()
    ai = 'yes'
    #provide current weather
    return response, ai
 
def on():
    # turn light on
    relay.on()
    response = 'light turned on'
    return response

def off():
    # turn light off
    relay.off()
    response = 'light turned off'
    return response
