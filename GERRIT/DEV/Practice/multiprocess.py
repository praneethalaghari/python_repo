from multiprocessing import Process
import time

x = 0

def increment():
    x = 0
    for _ in range(10000000):
        x +=1
    print(x)

if __name__ == '__main__':

    start_time = time.time()

    p1 = Process(target=increment)
    p2 = Process(target=increment)
    p3 = Process(target=increment)
    p4 = Process(target=increment)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end_time = time.time()

    print(end_time-start_time)



    #without processess

    st_time = time.time()

    increment()
    increment()
    increment()
    increment()

    ed_time = time.time()

    print("Without processess.. time taken {}".format(ed_time - st_time))
