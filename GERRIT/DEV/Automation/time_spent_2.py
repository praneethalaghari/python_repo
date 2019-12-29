import atexit
import time

with open("time_register.csv",'a') as f:
        f.write(str(int(time.time())) + '\n')

def exit_handler():
    with open("time_register.csv",'a') as f:
            f.write(str(int(time.time())))
        

atexit.register(exit_handler)

while(True):
    pass




