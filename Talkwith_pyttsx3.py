import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)  

engine.say("Hello, welcome to the code practices section. Do you know Hridoy bro will be the best future coder?")

engine.runAndWait()
