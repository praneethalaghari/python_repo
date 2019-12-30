import pyttsx3    				# Python text to Speech converter
import getpass    				# Imported to get logged in user
import speech_recognition as sr	# Python speech to text recognition
import random
import time
import sys
import os
import subprocess
import welcome_message

try:
	import winshell
except:
	subprocess.Popen("pip install winshell",shell=True)

	
#speech_recognition configuration

sample_rate = 48000
chunk_size	= 2048
microphone_list = sr.Microphone.list_microphone_names()
microphone_to_select = microphone_list[1]

#Voice messages configuration

repeat_strings = ['Speak now!!','Are you There??','I am waiting for your command..','On your Command master!!','Are you Slept?']
max_attemps_exceeded_strings = ["Seems you are busy!! Catch you later! Bye!","Dont waste my time Master!! Bye!","Its enough i am going to sleep"]
leaving_strings = ['Good bye!! See you soon','Ok !! bye !! Catch you later','Bye!! Have a nice day ahead','Hope i served you better today','Always at your help!! Master']
not_understood_strings = ["Sorry i cant understand what you said!!! May be you can ask!!! what can i do"]

def speak_now(source):
	try :
		audio = r.listen(source)
		audio_data = r.recognize_google(audio)
		return audio_data
	except:
		engine.say(random.choice(repeat_strings))
		return 0
			
def interact(source):
	num_of_attempts = 0
	while True:
		num_of_attempts +=1
		audio_data = speak_now(source)
		if audio_data:
			print("You :" + audio_data)
			return audio_data
		elif num_of_attempts > 2:
			engine.say(random.choice(max_attemps_exceeded_strings))
			sys.exit(0)
			
def change_voice():
	engine = pyttsx3.init()
	engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')			
			
			

#Decorator function implemented on engine.say() function to modify its behavior.
#i.e To print what bot is saying
# To prevent adding engine.runAndWait() everytime we execute say() function
		
def dec_engine_say(engine_say_func):
	def addon(*args,**kwargs):
		print("Alexa :" + args[0])
		engine_say_func(*args,**kwargs)
		pyttsx3.init().runAndWait()
	return addon
	
pyttsx3.init().say = dec_engine_say(pyttsx3.init().say)
	
	
#Functions
			
def openexplorer():
	os.system('explorer')
	return
	
	
def emptyrecyclebin():
	winshell.recycle_bin().empty(confirm=False, show_progress=True, sound = True)
	return 
		
def run(r):
	
	engine.say("How may i help you.. !!")
	
	while True:
		with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source :
				r.adjust_for_ambient_noise(source)
				command = interact(source)
				
				if command in ['open explorer','windows explorer','explorer']:
					engine.say("Proceeding to open windows explorer")
					openexplorer()
					engine.say("Task Accomplished")
					
				elif command in ['empty recycle bin','clean recycle bin','free recycle bin']:
					engine.say("Proceeding to empty recycle bin...")
					emptyrecyclebin()
					engine.say("Task Accomplished." + "All items in the bin are removed successfully")
					
				elif command in ['weather report']:
					engine.say("Ok.. DAVID is up with the details for you")
					welcome_message.run()
					change_voice()
					
				elif command in ['bye','good bye','get lost','see you','nothing','goodbye']:
					engine.say(random.choice(leaving_strings))
					break
					
				else:
					engine.say(random.choice(not_understood_strings))
					time.sleep(2)
					
				
				engine.say("What else can i do for you!!")
				
				
if __name__ == '__main__':

	global engine
	r = sr.Recognizer()			# Starting Speech recognizer
	engine = pyttsx3.init()		# Starting Text recognizer

	engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')


	# Fetching logged in user
	username = getpass.getuser()
	engine.say("Hello "+ username + "!! your Virtual assistant Alexa here..")
	
	run(r)
		
	engine.stop()
