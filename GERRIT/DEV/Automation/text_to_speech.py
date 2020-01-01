import pyttsx3

engine = pyttsx3.init()

a =1
engine.say("Hellow !! Have a nice day")
engine.say("Hello the num is {}".format(a))
engine.runAndWait()
