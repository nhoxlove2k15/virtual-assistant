import speech_recognition 
from datetime import date ,datetime
import pyttsx3
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
while True :
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
        print("Robot:...")
    try :
        you = robot_ear.recognize_google(audio)
    except :
        you =""
    
    print("You say: " , you)
    now = datetime.now() 
    today = date.today() 
    
    if "hello" in you:
        robot_brain = "hello master yi"
    elif "today" in you:
        robot_brain = today.strftime("%B %d, %Y")
    elif "president" in you:
        robot_brain = "Biden"
    elif you == "":
        robot_brain = "I can't hear you"
    elif "time" in you:
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you :
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else :
        robot_brain ="I'm fine thank you and you"
    print("Robot says: " , robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()



    