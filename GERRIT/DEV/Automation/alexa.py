import pyttsx3    				# Python text to Speech converter
import getpass    				# Imported to get logged in user
import speech_recognition as sr	# Python speech to text recognition
import random
import time

#speech_recognition configuration

sample_rate = 48000
chunk_size	= 2048
microphone_list = sr.Microphone.list_microphone_names()
microphone_to_select = microphone_list[1]

repeat_strings = ['Speak now!!','Are you There??','I am waiting for your command..','On your Command master!!','Are you Slept?']
max_attemps_exceeded_strings = ["Seems you are busy!! Catch you later! Bye!","Dont waste my time Master!! Bye!","Hmm.. Its enough i am going to sleep"]

def speak_now(source):
	try :
		audio = r.listen(source)
		engine.say(random.choice(repeat_strings))
		engine.runAndWait()
		audio_data = r.recognize_google(audio)
		return audio_data
	except:
		return 0

def run():

	with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source :
			r.adjust_for_ambient_noise(source)
			
			num_of_attempts = 0
			
			while True:
				num_of_attempts +=1
				
				audio_data = speak_now(source)
				if audio_data:
					print("You :" + audio_data)
					break
				elif num_of_attempts > 2:
					engine.say(random.choice(max_attemps_exceeded_strings))
					break
				
	
		
		
if __name__ == '__main__':

	r = sr.Recognizer()			# Starting Speech recognizer
	engine = pyttsx3.init()		# Starting Text recognizer

	engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')


	# Fetching logged in user
	username = getpass.getuser()
	engine.say("Hello "+ username + "!! your Virtual assistant Alexa here..")
	engine.say("How may i help you.. :")
	engine.runAndWait()

	run()
		
	engine.runAndWait()
	engine.stop()
