import pyttsx3
import requests
import json
import sys
import time
from datetime import datetime

#voices = pyttsx3.init().getProperty('voices')
#print([voice.id for voice in voices])

def run():

	engine = pyttsx3.init()
	
	#engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
	
	if __name__ == '__main__': engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
	else: engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
	
	
	
	# Weather 
	url = "http://api.openweathermap.org/data/2.5/weather?appid=fa2536ab2699a5077d09902716acddc2&q="
	city = 'Hyderabad'

	concat_url = url + city

	response = requests.get(concat_url)
	data = response.json()

	temp = data['main']['temp'] - 273.15  # Converting recieved Kelvins into C
	rounded_temp = "%.1f" % round(temp,2)

	if temp <= 26:
		climate = "cold"
	elif temp > 26 and temp < 32:
		climate = "warm"
	else:
		climate = "hot"

	current_time_hour = int(time.strftime("%H"))

	if current_time_hour < 12:
		time_of_the_day = "Morning"
	elif current_time_hour > 12 and current_time_hour < 16:
		time_of_the_day = "Afternoon"
	else:
		time_of_the_day = "Evening"


	engine.runAndWait()

		
	engine.say("Hello, Good" + time_of_the_day + "Praneth")
	if __name__ == '__main__': engine.say("Hope you are fine")
	engine.say("Its " + climate + "outside. Recording about " + rounded_temp + "Centigrade")
	engine.say("Enjoy the weather")

	voices = engine.getProperty('voices')

	engine.runAndWait()
	engine.stop()



if __name__ == '__main__':
	run()
