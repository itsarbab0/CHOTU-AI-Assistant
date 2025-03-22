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
        print("Listening...")
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
        print("Recognizing...")
        query = rec.recognize_google(audio, language = "en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

if __name__ == "__main__":
    while True:
        query = command().lower()
        speak(query)
        if "exit" in query:
            break

