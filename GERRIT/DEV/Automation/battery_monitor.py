import psutil
import pyttsx3
import time

battery = psutil.sensors_battery()
battery_level = str(battery.percent)

engine = pyttsx3.init()


if int(battery_level) >= 20 and int(battery_level) <= 90:
	engine.say("Battery levels are fine. Running at" + battery_level + "Percent")
	engine.runAndWait()


to_plug_warning_given = False
to_unplug_warning_given = False
	
while True:
	battery = psutil.sensors_battery()
	if battery.power_plugged:
		to_plug_warning_given = False    # This param is to make flag to false to be able to again give warning in else loop 
		if int(battery.percent) > 90:
			if not to_unplug_warning_given:
				engine.say("Battery sufficiently charged!! Please disconnect the power source")
				engine.runAndWait()
				to_unplug_warning_given = True
		time.sleep(10)  # Monitors for every 10 secs
	else:
		to_unplug_warning_given = False
		if int(battery.percent) <20:
			if not to_plug_warning_given: 
				engine.say("Battery levels are critical!! Connect to a power source immediately")
				engine.runAndWait()
				to_plug_warning_given = True
		time.sleep(10)  # Monitors for every 10 secs
        
engine.runAndWait()
engine.stop()
