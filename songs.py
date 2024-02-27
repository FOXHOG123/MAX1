import speech_recognition as sr
import pyttsx3
import pyautogui
import pywhatkit as kit

# to input voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",176)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        r.energy_threshold = 280
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"You said: {query}\n")   
    except Exception as e:
            # print(e)
            speak("Say That again please....")
            return "None"
    return query
def song(query):
    speak("What song do you want to listen from youtube!")
    if "see you again" in query:
        kit.playonyt("see you again")
    elif "Rubaru" in query:
        kit.playonyt("Rubaru")
    elif "taki taki" in query:
        kit.playonyt("Taki Taki")
        