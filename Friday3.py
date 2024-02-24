print(">> Starting The Friday : Wait For Some Seconds.")
from Body.Speak import Speak 
from Features.Wakeup import Listen
def WakeupDetected():
    

    query = Listen().lower()

    if "wake up" in query or 'make up' in query or 'friday' in query:
        print("")
        print(">> Starting Face Recognition >>")
        Speak("Starting Face Recognition")
        print("")
        from Face import FaceLock
        FaceLock()
    else:
        pass

WakeupDetected()








