import wolframalpha
import pyttsx3
import speech_recognition

# to input voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",176)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def WolfRamAlpha(query):  #Wolframalpha is online calucator website
    apikey = "7XHARJ-JQLH7Q3Q67"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    
    try:
        answer = next(requested.results).text
        return answer 
    except:
        speak("The value is not answerable")
                                                                    
def Calc(query):
    Term = str(query)
    Term = Term.replace("max","")
    Term = Term.replace("multiply","+")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    
    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)
        
    except:
        speak("The value is not answerable")
        