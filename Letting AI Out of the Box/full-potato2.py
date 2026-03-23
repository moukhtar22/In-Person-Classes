import speech_recognition as sr
from openai import OpenAI
import pyttsx3
from gpiozero import LED
from time import sleep
import os
from dotenv import load_dotenv
import tool_file

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

with open('tool_file.py','r') as file:
     tools = file.read()

led_ready = LED(17)
led_processing = LED(27)
led_answering = LED(22)

r = sr.Recognizer()
r.pause_threshold = 1.0          
r.phrase_threshold = 0.3
r.non_speaking_duration = 1

engine = pyttsx3.init()
engine.setProperty('voice', 'english-us')
engine.setProperty('rate', 170)

def stt():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=0.5)

        print("Say something (you can pause briefly)...")
        audio = r.listen(source, timeout=None, phrase_time_limit=15)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        message = text
    except:
        print("Sorry, I could not understand the audio.")
        message = "error"

    return message

def ai(query):
    injection = 'Answer in fewer than 20 words'
    query = f'{injection} - {query}'
    response = client.responses.create(
        model="gpt-5-nano",
        input=query
    )
    return response.output_text

def ai_tool(query, tools):
    response = client.responses.create(
        model="gpt-5-nano",
        input=f'''Return only the name of the function from this file of functions based onthis query: {query}\n
                    List of functions: {tools}'''
    )
    return response.output_text

def ai_response(query, data):
    query = f'''
        Answer in fewer than 15 words.\n
        Answer this question:{query}\n
        Based on this response from a function: {data}'''
    response = client.responses.create(
        model="gpt-5-nano",
        input=query
    )
    return response.output_text

def tts(text):
    engine.say(text)
    engine.runAndWait()

while True:
    led_ready.on()
    query = stt()
    led_ready.off()
    print(query)
    if query != 'error' and 'hey potato' in query:
        query = query.replace('hey potato', '')
        print(query)
        tts(query)
        led_processing.on()
     
        func = ai_tool(query, tools)
        func = func.replace('()','')
        func = func.strip()
        print(f'--{func}--') # Verify what LLM is returning

        try:
            tool = getattr(tool_file, func)
            try:
                response = tool()
            except:
                response = f'tool failed {tool}'
        except:
            response = 'Get Attribute Failed'

        if response[1] == 'yes':
            response = ai_response(query,response)

        led_processing.off()
        print(response)
        led_answering.on()
        tts(response)
        led_answering.off()
    else:
        sleep(.5)