import pyttsx3    				# Python text to Speech converter
import getpass    				# Imported to get logged in user
import speech_recognition as sr	# Python speech to text recognition
import random
import time
import sys
import os
import subprocess
import weather_report
import webbrowser
import requests
from bs4 import BeautifulSoup
import winsound


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
leaving_strings = ['Good bye!! See you soon','Ok !! bye !! Catch you later','Bye!! Have a nice day ahead','Hope i served you better today! Bye','Always at your help!! Master !! See you !']
not_understood_strings = ["Sorry i cant understand what you said!!! May be you can ask!!! what can i do"]

def speak_now(source):
	try :
		winsound.Beep(350,350)
		audio = r.listen(source)
		audio_data = r.recognize_google(audio)
		print(audio_data)
		return audio_data
	except sr.RequestError as e:
		engine.say("Could not request results from Google Speech Recognition service... Please check your network connection")
		return 0
	except Exception as e:
		engine.say(random.choice(repeat_strings))
		print(e)
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
			
def activate_battery_monitor():
	#subprocess.Popen([r"C:\Users\Praneeth Alaghari\python_repo\GERRIT\DEV\Automation\battery_monitor.bat"],shell=True)
	os.startfile(r"C:\Users\Praneeth Alaghari\python_repo\GERRIT\DEV\Automation\battery_monitor.bat")
	time.sleep(5)
	return
	
def plot_a_graph():
	import matplotlib.pyplot as plt
	graph = plt.plot([0,1],[3,4])
	plt.savefig("graph.png",bbox_inches='tight')
	os.startfile("graph.png")
	
def activate_key_logger():
	os.startfile(r"C:\Users\Praneeth Alaghari\python_repo\GERRIT\DEV\Automation\keylogger.bat")
	return
	
def shut_down(source):
	engine.say('Do you want me to shut down the PC?')
	proceed = interact(source)
	if proceed in ['yes','Yes','s','S']:
		os.system("shutdown /s /t 1")
		engine.say('Ok.. proceeding to shut down the system')
		sys.exit(0)
	else:
		return

def restart(source):
	engine.say('Do you want me to restart the PC?')
	proceed = interact(source)
	if proceed in ['yes','Yes','s','S']:
		os.system("shutdown /r /t 1")
		engine.say('Ok.. proceeding to restart the system')
		sys.exit(0)
	else:
		return
		
def google_search(source):
	engine.say("Ok.. what do you want to search for ?")
	search_string = interact(source)
	google_url = 'www.google.com/search?q='
	url = google_url + search_string
	webbrowser.open(url)
	engine.say("Ok.. showing search results for " + search_string)
	
def play_video_song(to_search):
	google_url = 'https://www.google.com/search?q='
	url = google_url + to_search
	webbrowser.open(url)
	
	response = requests.get(url)
	soup = BeautifulSoup(response.content,'html5lib')
	
	class_retriever = soup.findAll('div',attrs={'class' : 'twQ0Be'})
	print(class_retriever)
	
	
def lookup_meaning(word):
	import fetch_meaning
	mean_ing = fetch_meaning.meaning(word)
	engine.say(mean_ing)
	
		
def web_search(source):
	engine.say("Ok.. which website you want me to open?")
	search_string = interact(source)
	url = 'www.'+search_string+'.com'
	webbrowser.open(url)
	engine.say("Ok.. Proceeding to open" + search_string + '.com')
	

def what_can_i_do():
	pass

	
			
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

def match_score_updates():
	os.startfile(r"C:\Users\Praneeth Alaghari\python_repo\GERRIT\DEV\Automation\cricbuzz.bat")
	time.sleep(10)
	
def emptyrecyclebin():
	winshell.recycle_bin().empty(confirm=False, show_progress=True, sound = True)
	return 

def login(to_website):
	if to_website == 'Freecharge' :
		engine.say("cool.. Proceeding to login!!Please wait for a moment")
		import freecharge_login
		freecharge_login.run()
		
def run(r):
	
	engine.say("How may i help you.. !!")
	
	while True:
		with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source :
				r.adjust_for_ambient_noise(source)
				command = interact(source)
				
				if command in ['open explorer','windows explorer','explorer','Windows Explorer']:
					engine.say("Proceeding to open windows explorer")
					openexplorer()
					engine.say("Task Accomplished")
					
				elif command in ['empty recycle bin','clean recycle bin','free recycle bin','recycle bin']:
					engine.say("Proceeding to empty recycle bin...")
					emptyrecyclebin()
					engine.say("Task Accomplished." + "All items in the bin are removed successfully")
					
				elif command in ['weather report']:
					engine.say("Ok.. DAVID is up with the details for you")
					weather_report.run()
					change_voice()
					
				elif command in ['activate Battery Monitor','battery status','Battery Monitor']:
					engine.say("Ok.. Activating battery monitor..")
					activate_battery_monitor()
					engine.say("Battery Monitor Activated")
				
				elif command in ['Google','search Google','Google search','open Google','ok Google']:
					google_search(source)
					
				elif command in ['open website','web search']:
					web_search(source)
					
				elif command.startswith('meaning of'):
					to_search = "".join(command.split(' ')[2:])
					engine.say("Ok ",to_search)
					lookup_meaning(to_search)
					
				elif command.startswith('login'):
					to_website = "".join(command.split(' ')[1:])
					engine.say("Okay")
					login(to_website)
				
				elif command in ['Cricbuzz','score update','match score','score please','activate score update','cricket']:
					engine.say("Sure.. Activating score update..")
					match_score_updates()
				
				elif command in ['activate keylogger','keylogger']:
					engine.say("Activating Keylogger")
					activate_key_logger()

				elif command.startswith('play'):
					to_search = "".join(command.split(' ')[1:])
					engine.say("Ok playing",to_search)
					play_video_song(to_search)
					break

				elif command in ['shutdown','restart']:
					if command == 'shutdown':
						shut_down(source)
					if command == 'restart':
						restart(source)
				
				elif command in ['bye','good bye','get lost','see you','nothing','goodbye','good night','enough']:
					engine.say(random.choice(leaving_strings))
					break
					
				else:
					engine.say(random.choice(not_understood_strings))
					time.sleep(0.8)
					
				
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
