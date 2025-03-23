import datetime
import time
import webbrowser
import pyttsx3
import speech_recognition as sr


### initializing Phase
def initializing_Voices():
    engine = pyttsx3.init("sapi5")
    voice = engine.getProperty("voices")
    # We have two voices in our system
    engine.setProperty("voice", voice[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 30) # Speed of voice i.e. hit and trial 
    vol = engine.getProperty("volume")
    engine.setProperty("volume", vol + 0.25) # Volume of voice i.e. hit and trial
    return engine

### the Speaking Phase
def speak(text):
    engine = initializing_Voices()
    engine.say(text)
    engine.runAndWait()

### As I am Tested my Speak Function is working Properply now Lets take the Input from Microphone

def command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source, duration = 0.5)
        print("Listening...", end = "", flush=True)
        rec.pause_threshold = 1.0   # set time to wait after detecting and before recognizing
        rec.phrase_threshold = 0.3 # Wait to check input valid or not
        rec.sample_rate = 48000   # 48000 sample recorded / sec 
        rec.dynamic_energy_threshold = True # To adjust the energy threshold
        rec.operation_timeout = 5   # Twait if no input come
        rec.non_speaking_duration = 0.5 # wait when input completed
        rec.dynamic_energy_adjustment = 2   # Energy adjustment
        rec.energy_threshold = 3000  # Energy threshold
        rec.phrase_time_limit = 10  # Time limit for the phrase
        # print("No of MicroPhones", sr.Microphone.list_microphone_names())
        audio = rec.listen(source)
    try:
        print("\r", end = "", flush=True)
        print("Recognizing...", end = "", flush = True)
        query = rec.recognize_google(audio, language = "en-in")
        print("\r", end = "", flush=True)
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

def get_Day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
    return day_of_week
    


def greetMe():
    hour = int(datetime.datetime.now().hour)
    ti = time.strftime("%I:%M:%p")
    day = get_Day()

    if (hour >= 0) and (hour < 12) and ("AM" in ti):
        speak(f"Good Morning Mania, Chotu here its {day} and the time is {ti}")
    elif (hour >= 12 and hour < 16) and ("PM" in ti):
        speak(f"Good Afternoon Mania, Chotu here its {day} and the time is {ti}")
    elif (hour >= 16 and hour < 20) and ("PM" in ti):
        speak(f"Good Evening Mania, Chotu here its {day} and the time is {ti}")
    else:
        speak(f"Good Night Mania, Chotu here its {day} and the time is {ti}")

def social_media(command):
    if "youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "whatsapp" in command:
        speak("Opening Whatsapp")
        webbrowser.open("https://web.whatsapp.com")
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    else:
        speak("Sorry, I am not able to open this Social Media")


if __name__ == "__main__":
    greetMe()
    while True:
        # query = input("Enter your Command: ").lower()
        query = command().lower()
        if "exit" in query:
            break
        if ("youtube" in query) or ("whatsapp" in query) or ("google" in query) or ("instagram" in query) or ("facebook" in query):
            social_media(query)
             
    #     query = command().lower()
    #     speak(query)
    #     if "exit" in query:
    #         break

