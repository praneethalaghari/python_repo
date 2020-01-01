import pyttsx3
import speech_recognition as sr
import os
import time

engine = pyttsx3.init()
r = sr.Recognizer()

def listen_func(source):
	print("speak now")
	audio = r.listen(source)
	try:
		recognized_audio = r.recognize_google(audio)
		return recognized_audio
	except:
		listen_func(source)
	

def run():
	print("In run method")
	with sr.Microphone() as source:
		while True:
			print("cool")
			r.adjust_for_ambient_noise(source)
			command = listen_func(source)
			print(command)
			if command in ["start Alexa",'Alexa']:
				os.startfile(r'C:\Users\Praneeth Alaghari\python_repo\GERRIT\DEV\Automation\alexa.bat')
				time.sleep(20)
		
		
if __name__ == '__main__':
	run()
	

