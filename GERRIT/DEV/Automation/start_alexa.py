import pyttsx3
import speech_recognition as sr
import os
import time
import winsound


class unrecognizable_event(Exception):
	pass


sample_rate = 48000
chunk_size	= 2048
microphone_list = sr.Microphone.list_microphone_names()
microphone_to_select = microphone_list[1]


engine = pyttsx3.init()
r = sr.Recognizer()

def listen_func(source):
	print("speak now")
	audio = r.listen(source)
	try:
		recognized_audio = r.recognize_google(audio)
		print('Recognized audio is ' + recognized_audio)
		return recognized_audio
	except:
		return
		
	

def run():
	with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
		while True:
			print("Loop")
			r.adjust_for_ambient_noise(source)
			command = listen_func(source)
			if command == None:
				continue
			else:
				print("Command to execute :" + command)
				if command in ["start Alexa",'Alexa']:
					os.startfile(r'C:\Users\Praneeth Alaghari\python_repo\GERRIT\DEV\Automation\alexa.bat')
					time.sleep(20)
		
		
if __name__ == '__main__':
	run()
	

