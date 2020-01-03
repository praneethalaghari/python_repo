import psutil
import pyttsx3
import time
import os
import matplotlib.pyplot as plt

battery = psutil.sensors_battery()
battery_level = str(battery.percent)

engine = pyttsx3.init()

engine.say("Battery Monitor Activated")

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

	
	xtick_labels = [time.strftime('%H-%M',time.localtime(x)) for x,y in charge_discharge_data.items()]
	x_ticks = list(charge_discharge_data.keys())
	plt.xticks([x_ticks[i] for i in range(len(x_ticks)) if i%10 == 0],[xtick_labels[i] for i in range(len(xtick_labels)) if i%10 == 0]) # To reduce x axis scale
	plt.yticks(range(0,100,10))
	
	#	xy = list(np.linspace(0,len(x_ticks)-1,10).astype('int'))
	#	plt.xticks([x_ticks[i] for i in xy],[dict_keys_2[i] for i in xy])
	#	plt.yticks(range(0,100,10))
	#	- Use the above in case of complications in dividing huge number of elements in above code 
	#	- i.e in already existing code 1000 will be divided with 10 yields 100 values
	#	- where as above commented code will make 1000 into 10 equal parts.. what ever the size of elems.. it will divid into 10 hence scale will be good 

	
	date = time.strftime("%d-%m-%Y")
	time_of_day = time.strftime("%H_%M_%S")
	
	plt.suptitle('Battery Analysis_' + str(date) + '_' + str(time_of_day))
	
	#def convert_epoch_to_time(x):
	#return time.strftime('%H-%M',time.localtime(x))

	#dict_keys_2 = list(map(lambda x: time.strftime('%H-%M',time.localtime(x)),dict))
	#print(dict_keys_2)

	#dict_keys_3 = list(map(convert_epoch_to_time,dict))
	#print(dict_keys_3)
	
	fig_name = 'Battery Analysis_' + str(date) + '_' + str(time_of_day) + '.png'
	plt.savefig(fig_name)
	os.startfile(fig_name)


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
