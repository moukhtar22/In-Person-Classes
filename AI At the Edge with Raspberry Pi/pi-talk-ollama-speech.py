import speech_recognition as sr
from ollama import chat, ChatResponse
import pyttsx3

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

    response: ChatResponse = chat(model='granite3.3:2b', messages=[
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
    query = stt()
    print(query)
    if query != 'error':
        tts(query)
        response = ai(query)
        print(response)
        tts(response)