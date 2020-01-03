import matplotlib.pyplot as plt
import os
import time
import random
import numpy as np

dict = {1577944305: 96, 1577944365: 94, 1577944425: 94, 1577944485.9137468: 94, 1577944545.9138036: 91, 1577944605.9146113: 91, 1577944665.9155207: 89, 1577944725.9164007: 89, 1577944785.917648: 89}
#dict = {1577949399.3643787: 15}

#[1,2,3,4,5,6,7,8,9,10],[81,78,65,59,48,51,62,74,83,91]

date = time.strftime("%d-%m-%Y")
time_of_day = time.strftime("%H_%M_%S")

fig = plt.plot(dict.keys(),dict.values())
plt.xlabel('Time(in mins)')
plt.ylabel('Battery %')
plt.suptitle('Battery Analysis_' + str(date) + '_' + str(time_of_day))

print(fig)
print(type(dict.keys()))


def convert_epoch_to_time(x):
	return time.strftime('%H-%M',time.localtime(x))

dict_keys_1 = [time.strftime('%H.%M',time.localtime(x)) for x,y in dict.items()]
print(dict_keys_1)


dict_keys_2 = list(map(lambda x: time.strftime('%H-%M',time.localtime(x)),dict))
print(dict_keys_2)

dict_keys_3 = list(map(convert_epoch_to_time,dict))
print(dict_keys_3)

print(type(dict_keys_1))




x_ticks = list(dict.keys())

#plt.xticks([x_ticks[i] for i in range(len(x_ticks)) if i%2 == 0],[dict_keys_2[i] for i in range(len(dict_keys_2)) if i%2 == 0])
#plt.xticks(list(range(len(dict_keys_2))),[dict_keys_2[i] for i in range(len(dict_keys_2)) if i%2 == 0])
xy = list(np.linspace(0,len(x_ticks)-1,10).astype('int'))
print(xy)
print(len(x_ticks))

#print(list(np.linspace(0,len(x_ticks)-1,10)))
plt.xticks([x_ticks[i] for i in xy],[dict_keys_2[i] for i in xy])
plt.yticks(range(0,100,10))


print(date)
print(time_of_day)


abc = [random.randint(10,100) for i in range(50)]

defg = [abc[i] for i in range(len(abc)) if i%10 == 0]

print(abc)
print(defg)




fig_name = 'Battery Analysis_' + str(date) + '_' + str(time_of_day) + '.png'

plt.savefig(fig_name)
os.startfile(fig_name)