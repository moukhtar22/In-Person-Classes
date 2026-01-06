import speech_recognition as sr
import pyttsx3
from gpiozero import LED
import requests

led_ready = LED(17)
led_processing = LED(27)
led_answering = LED(22)

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.0          
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 1

engine = pyttsx3.init()
engine.setProperty('voice', 'english-us')
engine.setProperty('rate', 170)

def main():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        # Shorter calibration is fine; too long can overfit to noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        print("Say something (you can pause briefly)...")
        # phrase_time_limit = max length in seconds it will record for this turn
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        message = text

    except:
        print("Sorry, I could not understand the audio.")
        message = "error"

    # Append to HTML log
    with open("conversation.htm", "w") as f:
        f.write('<meta http-equiv="refresh" content="1">')
        f.write(f'<p>{message}</p>')

    return message

def ai(query):
    injection = 'Answer in fewer than 20 words'
    query = f'{injection} - {query}'

    key = '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'
    url = "https://api.openai.com/v1/responses"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    payload = {
        "model": "gpt-4.1-mini",
        "input": query
    }

    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()

    data = resp.json()

    return data["output"][0]["content"][0]["text"]

def speach(text):
    engine.say(text)
    engine.runAndWait()

while True:
    led_ready.on()
    query = main()
    led_ready.off()
    if query != 'error':
        speach(query)
        led_processing.on()
        response = ai(query)
        led_processing.off()
        print(response)
        with open("conversation.htm", "a") as f:
            f.write('<meta http-equiv="refresh" content="1">')
            f.write('<hr>')
            f.write(f'<p>{response}</p>')
        led_answering.on()
        speach(response)
        led_answering.off()