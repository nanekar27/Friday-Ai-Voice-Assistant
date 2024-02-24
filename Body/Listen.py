import speech_recognition as sr
from googletrans import Translator 
   

#listen function
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source,0,5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")

    except:
        return""

    query = str(query).lower()
    return query

# translator

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"User :{data}")
    return data


# connecting mic and translator

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data


 