import pyttsx3
import speech_recognition as sr
import datetime
import os 
import wikipedia
import webbrowser
from Body.Speak import Speak

def takeCommand():
     #it takes microphone input and gives retutrn string output
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thresholde = 1
        audio = r.listen(source,0,9)  #// listen time 

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='EN-IN')
        print(f"User said: {query}\n")

    except Exception as e:
        #//print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    
    while True:
        query = takeCommand().lower()

        #// logic for executing tasks based on query
        if 'wikipedia' in query: #// wikipedia code
            Speak('Searchin Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)
        elif 'open youtube' in query: #// youtube open only code
            url1 = "youtube.com"
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url1) 
        elif 'open whatsapp' in query: #// whatsapp web open only code
            url2 = "https://web.whatsapp.com/"
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url2)
        elif 'open google' in query: #// google open only code
            url3 = "https://www.google.co.in/"
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url3) 
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strTime} ")
        elif 'open visual studio' in query:
            vscodePath = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
        elif 'open jupiter notebook' in query:
            jypPath = "C:\\Users\\ADMIN\\anaconda3\\python.exe"
            os.startfile(jypPath)
        elif 'open chrome' in query:
            chrPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrPath)
            
        
        

