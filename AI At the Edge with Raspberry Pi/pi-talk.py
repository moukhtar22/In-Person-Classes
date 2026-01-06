import speech_recognition as sr

recognizer = sr.Recognizer()

# Tweak how sensitive it is to silence
recognizer.pause_threshold = 1.0          # increase if it still cuts off
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 1

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

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        message = "Sorry, I could not understand the audio."

    except sr.RequestError as e:
        print(f"Speech recognition request failed: {e}")
        message = f"Speech recognition request failed: {e}"

    # Append to HTML log
    with open("conversation.htm", "w") as f:
        f.write('<meta http-equiv="refresh" content="1">')
        f.write(f'<p>{message}</p>')

while True:
    main()
