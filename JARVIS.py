import pyttsx3
import speech_recognition as sr


### initializing Phase
def initializing_Voices():
    engine = pyttsx3.init("sapi5")
    voice = engine.getProperty("voices")
    # We have two voices in our system
    engine.setProperty("voice", voice[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 30) # Speed of voice i.e. hit and trial 
    vol = engine.getProperty("volume")
    engine.setProperty("colume", vol + 0.25) # Volume of voice i.e. hit and trial
    return engine

### the Speaking Phase
def speak(text):
    engine = initializing_Voices()
    engine.say(text)
    engine.runAndWait()


speak("Hello, I am Friday. How may I help you?")