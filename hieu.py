
from datetime import date ,datetime
now = datetime.now() 
now_format = now.strftime("%H hours %M minutes %S seconds")
today = date.today() 
today_format = today.strftime("%B %d, %Y")
you = "hello"
if "hello" in you:
    robot_brain = "hello master yi"
elif "today" in you:
    robot_brain = today_format 
elif "president" in you:
    robot_brain = "Biden"
elif you == "":
    robot_brain = "I can't hear you"
else :
    robot_brain ="I'm fine thank you and you"
print(robot_brain)