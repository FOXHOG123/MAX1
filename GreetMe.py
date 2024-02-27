import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning, sir!")
        elif hour>12 and hour<16:
            speak("Good Afternoon, sir!")
        elif hour>16 and hour<20:
            speak("Good Evening! sir!")
        else:
            speak("Hey Dear!")
            
        speak("Hii!, I am Max, Please tell me how can i help you ")
        
 