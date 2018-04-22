import random

def generatenewlist(mesg = "Generating Random list"):
    a = random.sample(range(0, 10), 6)
    return a

def newlistwithextremes(new_list):
    len_of_list = len(new_list)
    print(new_list)
    print([new_list[x] for x in range(0,len_of_list) if x == 0 or x == (len_of_list-1)])

newlistwithextremes(generatenewlist())
