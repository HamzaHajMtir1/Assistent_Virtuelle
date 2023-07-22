import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
try:
    with sr.Microphone() as source:
        print("parlez maintenant")
        voix = listener.listen(source)
        command = listener.recognize_google(voix)
        print(command)
        engine.say(command)
        engine.runAndWait()
except:
    pass