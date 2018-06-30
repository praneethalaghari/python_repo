import string
import random



def passwordGenerator(b):
    everything = ''
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    number = string.digits
    everything = upper + lower + special + number
    print(everything)
    password = random.sample(everything, b)
    #print(password)
    random.shuffle(password)
    for i in password:
        password = ''.join(password)
    return password

print("The password is ", passwordGenerator(int(input("Enter the desired length of the password "))))




#def generate():
#string=''
#for i in range (0,10):
#string+=chr(random.randint(33,126))
#print (string)


