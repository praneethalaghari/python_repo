
def checkforprime(value):
    for x in range(2,value):
        if value%x==0:
            return True




user_input = int(input("Enter a number to check if the number is prime"))

if not checkforprime(user_input):
    print ("Entered number is prime")
else:
    print ("Entered number is not a prime")