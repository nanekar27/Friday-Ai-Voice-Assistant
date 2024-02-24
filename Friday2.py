from Brain.AIBrain import ReplyBrain 
from Brain.Qna import QuestionsAnswer 
from Body.Listen import MicExecution
from Body.Wishme import wishMe
import webbrowser
import datetime
import wikipedia
import numpy as np
import os
import pyautogui as p
from datetime import date
import cv2
import requests
from bs4 import BeautifulSoup

print(">> Starting The Friday : Wait For Some Seconds.")
from Body.Speak import Speak



def MainExecution():
    p.press('esc')
    Speak("access granted")

    wishMe()


    while True:

        Data = MicExecution()
        Data = str(Data)
        query = str(Data).lower()
        chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        if len(Data)<4:
            pass

        elif "what is" in Data or "Where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            Speak(Reply) 
        elif  'wikipedia' in query: #// wikipedia code
            Speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)
        elif "open youtube" in query: #// youtube open only code
            url1 = "youtube.com"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url1)
        elif "time" in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strTime} ")
        elif "date" in query:
            today = date.today()
            d1 = today.strftime("%B %d, %Y ")
            Speak(d1)
        elif 'open whatsapp' in query: #// whatsapp web open only code
            url2 = "https://web.whatsapp.com/"
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url2)
        elif "open google" in query: #// google open only code
            url3 = "https://www.google.co.in/"
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url3) 
        elif "close" in query or "Close" in Data:
            WakeupDetected()
        elif 'open visual studio' in query:
            vscodePath = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
        #elif 'open jupiter notebook' in query:
        #   jypPath = "C:\\Users\\ADMIN\\anaconda3\\python.exe"
         #   os.startfile(jypPath)
        elif 'open chrome' in query:
            chrPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrPath)
        #elif 'open nfs' in query:
         #   nfsPath = "D:\\need for speed 2012\\R.G. Catalyst\\Need for Speed - Most Wanted\\NFS13.exe"
          #  os.startfile(nfsPath)
        elif 'open hotstar' in query:
            url4="https://www.hotstar.com/in"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url4)
        elif 'open instagram' in query:
            url5="https://www.instagram.com/"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url5)
        elif'open facebook' in query:
            url6='https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C550525804944%7Cb%7Cfacebook%20%27%7C&placement=&creative=550525804944&keyword=facebook%20%27&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696220912%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-327195741349%26loc_physical_ms%3D9300140%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQiA4aacBhCUARIsAI55maGF_chcaNU6YmbMCPummEsQWaZcXiauAUsNIwZUFACC4Vzdssr9DywaAlFeEALw_wcB'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url6)
        elif 'open physics wallaha' in query:
            url7='https://www.pw.live/study/batches'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url7)
        elif 'cricket score' in query:
            url8='https://www.google.com/search?q=cricket+score&rlz=1C1VDKB_enIN1031IN1031&oq=cricket&aqs=chrome.3.69i57j35i39j0i131i433i512j0i433i512j46i433i512j0i131i433i512l2j0i433i512l3.7419j0j15&sourceid=chrome&ie=UTF-8#sie=lg;/g/11n1ntn76g;5;/m/021q23;mt;fp;1;;;'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url8)
        elif 'open stackoverflow' in query:
            url9='https://stackoverflow.com/'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url9)
        elif'open amazon' in query:
            url10='https://www.amazon.in/'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url10)
        elif 'play ed sheeran song' in query or 'open music' in query or 'play sheeran' in query or 'favourat english music' in query or 'english music' in query:
            Speak("opening on youtube")
            url11='https://music.youtube.com/watch?v=ORrFJ63nlcA&list=OLAK5uy_mHzt_lZ0Vdnv3NAqvCLQw5CiYe0q96iBs'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url11)

        elif 'play arjit singh song' in query or 'play arijit singh' in query or 'play arijit' in query or 'romantic music' in query or 'play romantic music' in query :
            Speak("opening on youtube")
            url12='https://music.youtube.com/watch?v=NJAv_7lHUIU&list=OLAK5uy_nq81InQBifozkEJvDr7L9K3kURX7BfMlo'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url12)
        elif 'play old song' in query or 'old melody' in query or 'play ninghtys song' in query:
            Speak("opening on youtube")
            url13='https://music.youtube.com/watch?v=TFr6G5zveS8&list=RDCLAK5uy_nLOvZAnN86K4f-fJ6tUi0xHUPBHLBBkVE'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url13)
        elif 'your location' in query or 'you are location' in query:
            fpath="F:\\friday"
            os.startfile(fpath)
            Speak("my store location is drive F: friday")
        elif ' what is your version right now' in query or 'your version' in query:
            Speak("I am running currently on friday 3 point 2 version")
        elif 'open news' in query or 'news' in query or 'latest news' in query:
            url14 = 'https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url14)
        elif 'temperature' in query:
            search= "temperature in pune"
            url15 =f"https://www.google.com/search?q={search}"
            r = requests.get(url15)
            data= BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            Speak(f"current {search} is {temp}")
        elif 'book movie ticket' in query or 'book movie' in query or 'movies ticket' in query or 'open book my show'in query:
            Speak('opening book my show')
            url16 = 'https://in.bookmyshow.com/'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url16)

        else :
            Reply = ReplyBrain(Data)
            Speak(Reply)
 

def FaceLock(): 
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('F:\\friday\\Features\\trainer.yml')   #load trained model
    cascadePath = "F:\\friday\\Features\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 5 #number of persons you want to Recognize


    names = ['','JAYESH','CHAITRA','KRISHNA','SAGAR']  #names, leave first empty bcz counter starts from 0


    cam = cv2.VideoCapture(1, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    # flag = True

    while True:

        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

            # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 48):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                MainExecution()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                Speak("access denied")
                pass
                
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

    # Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()

from Features.Wakeup import Listen
def WakeupDetected():
    

    query = Listen().lower()

    if "wake up" in query:
        FaceLock()
    elif "friday" in query:
        FaceLock()
    elif "make up " in query:
        FaceLock()
    elif "wake up friday" in query:
        FaceLock()
    else:
        WakeupDetected()

WakeupDetected()








