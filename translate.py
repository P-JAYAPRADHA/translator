import speech_recognition as sr
from googletrans import Translator
from langdetect import detect
import pyttsx3

# create a recognizer object
r = sr.Recognizer()
translator = Translator(service_urls=['translate.google.com'])
tts = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        print("Speak Something")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        input_language = detect(text)
        if input_language  == 'es':
            translation = translator.translate(text, dest='en')
            print(f"Translated to English: {translation.text}")
            tts.say(translation.text)
            tts.runAndWait()

        elif input_language =="en":
            translation = translator.translate(text, dest ='es')
            print(f"Translated to Spanish: {translation.text}")
            tts.say(translation.text)
            tts.runAndWait()

        else:
            print("Unsupported language")

    except sr.UnknownValueError:
        print("GoogleSpeech Recognition could not understood audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
