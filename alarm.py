import pyttsx3
import datetime
import os


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

extractedtime = open("Alarm.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarm.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timeset.replace("set an alarm","")
    timenow = timeset.replace("max","")
    timenow = timeset.replace("and",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alam ringing, sir!")
            os.startfile("music.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()
            
ring(time)