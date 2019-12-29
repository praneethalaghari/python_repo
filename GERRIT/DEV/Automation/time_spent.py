import time
import threading



with open("report_time.txt",'a') as f:
    f.write(str(int(time.time()))+ '\n')
    f.write(str(threading.get_ident()))

def main():
    try:
        while(True):
            pass
    finally:
        with open("report_time.txt",'a') as f:
            f.write(str(int(time.time()))+ '\n')
main()


