import speech_recognition as sr
from ollama import chat, ChatResponse
import pyttsx3
from gpiozero import LED, OutputDevice
from time import sleep
import datetime

led_ready = LED(17)
led_processing = LED(27)
led_answering = LED(22)

relay = OutputDevice(10, active_high = True)

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

    response: ChatResponse = chat(model='granite4:350m', messages=[
    {
        'role': 'user',
        'content': query,
    },
    ])

    return response.message.content

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
        if 'end session' in query:
            exit()
        elif 'what time is it' in query:
            response = datetime.datetime.now().strftime("%H:%M:%S")
        elif 'light on' in query:
            relay.on()
            response = 'light turned on'
        elif 'light off' in query:
            relay.off()
            response = 'light turned off'
        else:    
            response = ai(query)
        led_processing.off()
        print(response)
        led_answering.on()
        tts(response)
        led_answering.off()
    else:
        sleep(.5)