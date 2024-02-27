import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

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

# to convert voice into text 
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
    
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("whom do you want to message ")
    voice = takeCommand().lower()
    # a = int(input('''Person 1 - 1
    # Person 2 -2'''))
    if "send message to bishal" in voice:
        speak("Whats the message")
        message = takeCommand()#str(input("Enter the message"))
        pywhatkit.sendwhatmsg("+916003387072",message,time_hour=strTime,time_min=update)
    elif "send message to Arpit" in voice:
        speak("Whats the message ")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+916002599236",message,time_hour=strTime,time_min=update)
    elif "send message to dip" in voice:
        speak("Whats the message ")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+916026951032",message,time_hour=strTime,time_min=update)
    elif "send message to deep sir" in voice:
        speak("Whats the message ")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+919864242722",message,time_hour=strTime,time_min=update)
    elif "send message to Sanatan"  in voice:
        message = takeCommand()
        speak("Whats the message ")
        pywhatkit.sendwhatmsg("+917099809661",message,time_hour=strTime,time_min=update)