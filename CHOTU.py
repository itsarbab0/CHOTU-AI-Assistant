import datetime
import os
import sys
import time
import webbrowser
import pyautogui
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
    


def greetMe(name):
    hour = int(datetime.datetime.now().hour)
    ti = time.strftime("%I:%M:%p")
    day = get_Day()

    if (hour >= 0) and (hour < 12) and ("AM" in ti):
        speak(f"Good Morning {name}, Chotu here its {day} and the time is {ti}")
    elif (hour >= 12 and hour < 16) and ("PM" in ti):
        speak(f"Good Afternoon {name}, Chotu here its {day} and the time is {ti}")
    elif (hour >= 16 and hour < 20) and ("PM" in ti):
        speak(f"Good Evening {name}, Chotu here its {day} and the time is {ti}")
    else:
        speak(f"Good Night {name}, Chotu here its {day} and the time is {ti}")

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

def maniaSchedule():
    day = get_Day()
    speak(f"My Highness Mania, Your University Schedule for {day} is as follows:")
    week_days = {
        "Monday": "My Highness, You have three classes today. First one is Probability and Statistics at 9:00 AM to 10:20 AM and the second one is Operating System at 12:30 AM to 1:20 PM and the third one is Technical and Business writing at 1:30 PM to 2:20 PM",
        "Tuesday": "My Highness, You have two class and one Lab today. First one is Organizational Behavior at 9:30 AM to 10:20 AM and the Second one is Lab of Database at 10:30 AM to 12:20 PM and the third one is Database Class at 12:30 PM to 1:20 PM",
        "Wednesday": "My Highness, You have three classes today. First one is Probability and Statistics at 9:00 AM to 10:20 AM and the second one is Operating System at 12:30 AM to 1:20 PM and the third one is Technical and Business writing at 1:30 PM to 2:20 PM",
        "Thursday": "My Highness, You have two class and one Lab today. First one is Organizational Behavior at 9:30 AM to 10:20 AM and the Second one is Lab of Database at 10:30 AM to 12:20 PM and the third one is Database Class at 12:30 PM to 1:20 PM",
        "Friday": "My Highness, Today is your off day. Enjoy your day",
        "Saturday": "My Highness, Today is your off day. Enjoy your day",
        "Sunday": "My Highness, Today is your off day. Enjoy your day"  
    }
    if day in week_days.keys():
        speak(week_days[day])

def mySchedule():
    day = get_Day()
    speak(f"My Liege Arbab, Your University Schedule for {day} is as follows:")
    week_days ={
        "Monday": "My Liege, You have two classes today. First one is Artificial Intelegence at 11:30 AM to 1:00 PM and the second one is Compiler Construction at 1:00 PM to 2:30 PM",
        "Tuesday": "My Liege, You have three classes today. First one is Cyber Security at 9:00 AM to 10:30 AM and the second one is Software Engineering at 10:00 AM to 11:30 PM and the third one is Parallel Distributed Computing at 1:00 PM to 2:30 PM",
        "Wednesday": "My Liege, You have two classes today. First one is Artificial Intelegence at 11:30 AM to 1:00 PM and the second one is Compiler Construction at 1:00 PM to 2:30 PM",
        "Thursday": "My Liege, You have three classes today. First one is Cyber Security at 9:00 AM to 10:30 AM and the second one is Software Engineering at 10:00 AM to 11:30 PM and the third one is Parallel Distributed Computing at 1:00 PM to 2:30 PM",
        "Friday": "My Liege, You have only a LAB of Artificial Intelegence today at 8:30 AM to 11:30 AM",
        "Saturday": "My Liege, Today is your off day. Enjoy your day",
        "Sunday": "My Liege, Today is your off day. Enjoy your day"  
    }
    if day in week_days.keys():
        speak(week_days[day])

import os

def openApp(command):
    if "calculator" in command:
        speak("Opening Calculator")
        os.startfile("calc")
    elif "notepad" in command:
        speak("Opening Notepad")
        os.startfile("notepad")
    elif "paint" in command:
        speak("Opening Paint")
        os.startfile("mspaint")
    elif "brave" in command:
        speak("Opening Brave Browser")
        os.startfile(r'"C:\Users\karee\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"')
    elif "vs code" in command:
        speak("Opening Visual Studio Code")
        os.startfile("code")
    elif "chrome" in command:
        speak("Opening Chrome Browser")
        os.startfile(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')
         
    elif "pc" in command:
        speak("Opening This PC")
        os.startfile("explorer")
    elif "control panel" in command:
        speak("Opening Control Panel")
        os.startfile("control")
    elif "settings" in command:
        speak("Opening Settings")
        os.system("start ms-settings:")
    elif "microsoft edge" in command:
        speak("Opening Microsoft Edge")
        os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    elif "excel" in command or "ms excel" in command:
        speak("Opening Microsoft Excel")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
    elif "word" in command or "ms word" in command:
        speak("Opening Microsoft Word")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
    else:
        speak("Sorry, I am not able to open this Application")

def closeApp(command):
    if "calculator" in command:
        speak("Closing Calculator")
        os.system("taskkill /f /im calc.exe")
    elif "notepad" in command:
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")
    elif "paint" in command:
        speak("Closing Paint")
        os.system("taskkill /f /im mspaint.exe")
    elif "brave" in command:
        speak("Closing Brave Browser")
        os.system("taskkill /f /im brave.exe")
    elif "vs code" in command:
        speak("Closing Visual Studio Code")
        os.system("taskkill /f /im code.exe")
    elif "chrome" in command:
        speak("Closing Chrome Browser")
        os.system("taskkill /f /im chrome.exe")
    elif "pc" in command:
        speak("Closing This PC")
        os.system("taskkill /f /im explorer.exe")
    elif "control panel" in command:
        speak("Closing Control Panel")
        os.system("taskkill /f /im control.exe")
    elif "settings" in command:
        speak("Closing Settings")
        os.system("taskkill /f /im systemsettings.exe")
    elif "microsoft edge" in command:
        speak("Closing Microsoft Edge")
        os.system("taskkill /f /im msedge.exe")

if __name__ == "__main__":
    speak("Whose there?")
    name = command()
    while name == "None":
        speak("Can you please tell me your name again")
        name = command()
    greetMe(name)
    name = name.lower()
    while True:
        
        query = command().lower()
        if "exit" in query:
            speak("Good Bye My Lord, Its pleasure to serve you")
            sys.exit()
        if ("youtube" in query) or ("whatsapp" in query) or ("google" in query) or ("instagram" in query) or ("facebook" in query):
            social_media(query)
        elif ("time table" in query) or ("schedule" in query):
            if name == "arbab":
                mySchedule()
            elif name == "manya" or name == "mania":
                maniaSchedule()
        elif ("volume up" in query) or ("increase the volume" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")
            speak("Volume Increased")
        elif ("volume down" in query) or ("decrease the volume" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak("Volume Decreased")
        elif ("volume mute" in query) or ("mute the volume" in query):
            pyautogui.press("volumemute")
            speak("Volume Muted")
        elif ("open calculator" in query) or ("open word" in query) or ("open ms word" in query) or ("open ms excel" in query) or ("open excel" in query) or ("calculator" in query) or ("open notepad" in query)  or ("open paint" in query)  or ("open brave" in query)  or ("open vs code" in query) or ("open visual studio code" in query)  or ("open chrome" in query) or ("chrome browser" in query) or ("open pc" in query) or ("this pc" in query) or ("open control panel" in query) or ("control panel" in query) or ("open settings" in query) or ("open microsoft edge" in query) or ("open msedge" in query):
            openApp(query)
        elif ("close calculator" in query) or ("close ms word" in query) or ("close word" in query) or ("close ms excel" in query) or ("close excel" in query) or ("close notepad" in query) or ("close paint" in query) or ("close brave" in query) or ("close vs code" in query) or ("close chrome" in query) or ("close this pc" in query) or ("close pc" in query) or ("close control panel" in query) or ("close settings" in query) or ("close microsoft edge" in query) or ("close msedge" in query):
            closeApp(query)

        


