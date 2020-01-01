import psutil
import pyttsx3
import time
import matplotlib.pyplot as plt

battery = psutil.sensors_battery()
battery_level = str(battery.percent)

engine = pyttsx3.init()


if int(battery_level) >= 20:
	engine.say("Battery levels are fine. Running at" + battery_level + "Percent")
	engine.runAndWait()


to_plug_warning_given = False
to_unplug_warning_given = False
battery_power_plugged_in_event_noted = False
battery_power_plugged_out_event_noted = False

def plot_charge_discharge_data(charge_discharge_data):
	plt.plot(charge_discharge_data.keys(),charge_discharge_data.values())
	plt.xlabel('Time(in mins)')
	plt.ylabel('Battery %')
	plt.suptitle('Battery Analysis')
	plt.xticks(charge_discharge_data.keys())
	plt.yticks(range(0,100,10))
	plt.savefig('plot.png')
	os.startfile('plot.png')


charge_discharge_data = {}

	
while True:
	battery = psutil.sensors_battery()
	
	charge_discharge_data[time.time()] = battery.percent
	print(charge_discharge_data)
	
	
	if battery.power_plugged:
	
		to_plug_warning_given = False    				# This param is to make flag to false to be able to again give warning in else loop 
		battery_power_plugged_out_event_noted = False   # This param is to make flag to false to be able to again give discharge rate in else loop
		
		#Noting battery power,plugged_in event time for charging rate calculation
		if not battery_power_plugged_in_event_noted:	
			plug_in_time = time.time()
			plug_in_time_battery_power = battery.percent
			battery_power_plugged_in_event_noted = True
			
		
		if int(battery.percent) > 90:
			if not to_unplug_warning_given:
				engine.say("Battery sufficiently charged!! Please disconnect the power source")
				engine.runAndWait()
				to_unplug_warning_given = True
				
				#Noting battery power,plugged_in event time for charging rate calculation after reached 90
				charging_completed_time = time.time()
				charging_completed_battery_power = battery.percent
				
				if charge_discharge_data:
					plot_charge_discharge_data(charge_discharge_data)
				
				#Calculating the rate of charge
				rate_of_charging =  "%.2f" % round((charging_completed_battery_power - plug_in_time_battery_power)/((charging_completed_time - plug_in_time)/60),2)
				engine.say("Battery charged at a rate of {} per minute".format(rate_of_charging))
				engine.runAndWait()
				
								
		time.sleep(60)  # Monitors for every 10 secs
	else:
		to_unplug_warning_given = False
		battery_power_plugged_in_event_noted = False
		
		if not battery_power_plugged_out_event_noted:
			plug_out_time = time.time()
			plug_out_time_battery_power = battery.percent
			battery_power_plugged_out_event_noted = True
		
		if int(battery.percent) <20:
			if not to_plug_warning_given: 
				engine.say("Battery levels are critical!! Connect to a power source immediately")
				engine.runAndWait()
				to_plug_warning_given = True
				
				#Noting battery power,plugged_in event time for charging rate calculation after reached 90
				discharging_completed_time = time.time()
				discharging_completed_battery_power = battery.percent
				
				if charge_discharge_data:
					plot_charge_discharge_data(charge_discharge_data)
				
				#Calculating the rate of charge
				rate_of_discharging =  (plug_out_time_battery_power - discharging_completed_battery_power)/((plug_out_time - discharging_completed_time)/60)
				engine.say("Battery discharged at a rate of {} per minute".format(rate_of_discharging))
				engine.runAndWait()
				
		time.sleep(60)  # Monitors for every 10 secs
        
engine.runAndWait()
engine.stop()
