import pyttsx3


#window api sapi5 based
def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',170)
    print("")
    print(f"User: {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()



