import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source) 
    audio = r.listen(source)

try:
    print("Transcribing...")
    text = r.recognize_whisper(audio, model="base") 
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Whisper could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Whisper local service; {e}")