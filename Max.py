import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
from ast import Break
from re import search
import smtplib
import pytz
import random
import requests
from requests import get
import openai
import config
import bs4
from bs4 import BeautifulSoup
import pyautogui
import tkinter as ttk
import speedtest_cli
from plyer import notification
import pywhatkit as kit
# import googlemaps
# from openweathermap import WeatherClient

# for the password
for i in range(3):
    a = input("Enter password to open :- ")
    pw_file = open("D:\\AI IMAGE\\JESI\\KOKA\\password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP......")
        break
    elif (i==2 and a!=pw):
        print("Try Again")
    
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

def alarm(query):
    timehere = open("Alarm.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("D:\\AI IMAGE\\JESI\\KOKA\\alarm.py")

if __name__ == "__main__":
    # wishMe()
    
    while True:
        query = takeCommand().lower()
        if "wake up" in query or "hemax"in query:
            from GreetMe import greetMe
            greetMe()
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query or "sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break
                ###################JARVIS:- THE TRILOGY-----######################
                
                elif "change password" in query:
                    speak("What is the new password ")
                    new_pw = input("Enter the new passowrd")
                    new_password = open("D:\\AI IMAGE\\JESI\\KOKA\\password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir !")
                    speak(f"Sir! your new password is{new_pw} ")
                
                
                
                
                
                # Logic for executing tasks based on query
                elif 'wikipedia' in query:
                    speak('Searching Wikipdia')
                    query = query.replace("wikipedia","")
                    query = query.replace("wikipedia", "")
                    query = query.replace("Max","")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                #coversation section
                elif "hello" in query:
                    speak("hello sir, how are you")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("perfect, sir")
                elif "thank" in query:
                    speak("you are welcome, sir")
                elif "who is my roomate" in query:
                    speak("your roomate is arpit")
                elif "who are you" in query:
                    speak("i am ai based assistant, you can ask me about anything that you want to know !")
                elif "who made you" in query:
                    speak("mr. bishal")
                elif "what is your name?" in query:
                    speak("Thank you! My name is MAX ")
                elif "i love you" in query:
                    speak("love you too")
                elif "old are you " in query:
                    speak(" 25 days old, i am new to this world")
                # sites
                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                elif "play" in query:                 
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "pause" in query:
                    pyautogui.press("k")
                elif "play" in query:
                    pyautogui.press("k")
                elif "forward" in query:
                    pyautogui.press("l") 
                elif "backward" in query:
                    pyautogui.press("j")  
                elif "mute" in query: 
                    pyautogui.press("m")
                    speak ("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up sir!")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down Sir!")
                    volumedown()
                elif "google" in query:                  
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif 'stack overflow' in query:
                    webbrowser.open("stackoverflow.com")
                elif 'google' in query:
                    webbrowser.open("google.com")
                elif 'the time' in query:
                    #strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    #speak(f" ")
                    hour = datetime.datetime.now().strftime("%H")
                    min = datetime.datetime.now().strftime("%M")
                    speak(f"sir the time is {hour} bachkay {min} minutes")
                elif "open notepad" in query:
                    path = "C:\\Windows\\notepad.exe"
                    os.startfile(path)
                elif "open command prompt" in query:
                    os.system("start cmd")
                elif 'shutdown' in query:
                    speak("do you really? want to shutdown your system")
                    reply = takeCommand()
                    if 'yeah' in reply:
                        os.system('shutdown /s /t 1')
                    else:
                        Break
                elif 'restart' in query:
                    speak("do you really? want to restart your system")
                    reply = takeCommand()
                    if 'yes' in reply:
                        os.system('shutdown /r /t 1')
                    else:
                        Break
                elif 'logout' in query:
                    speak("do you really? want to logout your system")
                    reply = takeCommand()
                    if 'yes' in reply:
                        os.system('shutdown -1')
                    else:
                        Break

                elif 'stop' in query:
                    quit()
                elif 'go to sleep' in query:
                    speak("Ok sir! You can call me anytime..")
                    break
                elif 'exit' in query:
                    speak("ok sir!")
                    quit()
                elif "play music" in query: 
                    music_dir = "C:\\Users\\bisha\\Music"
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    for song in songs:
                        if song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, song))
                elif "ip address" in query:
                    ip = get('https://api.ipify.org').text
                    speak(f"Your IP address is {ip}")
                
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("D:\\AI IMAGE\\JESI\\KOKA\\FocusMode.py")
                        exit()

                    
                    else:
                        pass
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                elif "open bird" in query:
                    webbrowser.open("https://bard.google.com")
                    speak("Now You can use your Bard sir")
                elif "Open chat GPT" in query:
                    webbrowser.open("https://wwww.ai.com") 
                    speak("Now you can search, sir!")
                
                elif "open" in query:
                    speak("Launching, sir!")
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "set an alarm" in query:
                    print("input time example:- 18 and 42 and 42")
                    speak("set the  alarm")
                    a = input("Please tell the time :-")
                    alarm(a)
                    speak("Done sir")
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("max","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to"  + remember.read())
                elif "i want to listen song" in query:
                    speak("playing your favroute song")
                    a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=03e2Hocu37c&list=RD03e2Hocu37c&start_radio=1k")
                    elif b == 2:
                        Webbrowser.open("https://www.youtube.com/watch?v=0_sZlZn8aLY&list=RD03e2Hocu37c&index=2")
                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=sFMRqxCexDk&list=RD03e2Hocu37c&index=10")
                    elif b == 4:
                        webbrowser.open("https://www.youtube.com/watch?v=Zlqf9cuaOBw&list=RD03e2Hocu37c&index=11")
                    elif b == 5:
                        webbrowser.open("https://www.youtube.com/watch?v=KUpwupYj_tY&list=RD03e2Hocu37c&index=17")
                    elif b == 6:
                        webbrowser.open("https://www.youtube.com/watch?v=nJZcbidTutE&list=RD03e2Hocu37c&index=19")
                    elif b == 7:
                        webbrowser.open("https://www.youtube.com/watch?v=UbMgcdmYC70&list=RD03e2Hocu37c&index=20")
                    elif b == 8:
                        webbrowser.open("https://www.youtube.com/watch?v=ko7YMs9Q3KU")
                    elif b == 9:
                        webbrowser.open("https://www.youtube.com/watch?v=syFZfO_wfMQ")
                    elif b == 10:
                        webbrowser.open("https://www.youtube.com/watch?v=Z9yaG27quz0")
                    elif b == 11:
                        webbrowser.open("https://www.youtube.com/watch?v=XjqahRrIpj4")
                    elif b == 12:
                        webbrowser.open("https://www.youtube.com/watch?v=lzQpS1rH3zI")
                    elif b == 13:
                        webbrowser.open("https://www.youtube.com/watch?v=l5-8G7jqmqg")
                    elif b == 14:
                        webbrowser.open("https://www.youtube.com/watch?v=NLKwRW2y-sg")
                    elif b == 16:
                        webbrowser.open("https://www.youtube.com/watch?v=DAOZJPquY_w") 
                    elif b == 17:
                        webbrowser.open("https://www.youtube.com/watch?v=2vMH8lITTCE") 
                    elif b == 17:
                        webbrowser.open("https://www.youtube.com/watch?v=qk2WMmiiVFE") 
                    elif b == 18:
                        webbrowser.open("https://www.youtube.com/watch?v=ZA9CXGIfiJ8") 
                    elif b == 19:
                        webbrowser.open("https://www.youtube.com/watch?v=a6cJAFFQn_I") 
                    elif b == 20:
                        webbrowser.open("https://www.youtube.com/watch?v=o4VvqPPB6iU")
                    elif b == 21:
                        webbrowser.open("https://www.youtube.com/watch?v=Xd29mNwjUQQ&list=RD03e2Hocu37c&index=8")
                    else:
                        speak("sorry, i couldn't play a song for you.")
                elif "news" in query:
                    from news import latestnews
                    latestnews()
                elif "calculate" in query:
                    from calculate import  WolfRamAlpha
                    from calculate import Calc
                    query = query.replace("calculate", "")
                    query = query.replace("max", "")
                    Calc(query)
                
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    try:
                        temp_element = data.find("div", class_="BNeane")
                        if temp_element is not None:
                            temp = temp_element.text
                            speak(f"Current {search} is {temp}")
                        else:
                            speak("Sorry, I couldn't find the temperature information")
                    except AttributeError:
                        speak("Sorry, I couldn't find the temperature information.")

                    # temp = data.find("div", class_ = "BNeane").text
                    # speak(f"current{search} is {temp}")
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                
                elif "internet speed" in query: # it does not give the excat speed of the net speed but it is closer
                    wifi = speedtest.Speedtest() # pip isntall speedtest-cli
                    upload_net = wifi.upload()/1048576  
                    download_net = wifi.download()/1048576
                    print("wifi Upload speed is", upload_net)
                    print("wifi download speed is", download_net)
                    speak(f"wifi upload speed is {upload_net}")
                    speak(f"wifi download speed is {download_net}")
                    
                elif "schedule my day" in query:
                    tasks = [] #empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)") 
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("task.task","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of task :-"))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :-"))
                            file = open("tasks.txt",'a')
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query: 
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :-"))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                            
                    elif "show my schedule" in query:
                        
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("notification.mp3")
                        mixer.music.play()
                        notification.notify(
                            title = "My schedule :-",
                            message = content,
                            timeout = 15
                            )
                
                elif "play a game" in query:
                    from Rock import game_play
                    game_play()
                
                elif "screenshot" in query:
                    import pyautogui #pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save("s2.jpg")
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                    
                # translator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                elif "translate" in query:
                    from Trans import translategl
                    query = query.replace("Max","")
                    query = query.replace("translate","")
                    translategl(query)

                elif "play see you again" in query:
                    kit.playonyt("see you again") 
                elif "play kajra re" in query:
                    kit.playonyt("kajra re")
                elif "play perfect" in query:
                    kit.playonyt(query)
                elif "Bye" in query:
                    kit.playonyt("Bye")
                