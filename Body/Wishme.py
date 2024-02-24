import pyttsx3
import speech_recognition as sr
import datetime
#import os 
#import wikipedia
#import webbrowser




engine = pyttsx3.init('sapi5')  #//voice api microsoft
voices = engine.getProperty('voices')
    #//print(voices[1].id)
engine.setProperty('voice',voices[1].id)   #// set id for voice type

    #// speak function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    #// wish function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    elif hour>=16 and hour<19:
        speak("Good Evening!")
    else:
        speak("Hii!")
   
    speak("I Am Friday. Please tell me how may I healp you")

