import random


while(1):
    rand_number = random.randint(1, 9)
    user_input = int(input("Guess number between 1-9 : "))


    if user_input<rand_number:
        print("You guess is very low")
    elif user_input>rand_number:
        print("You guess is very high ")
    else:
        print("Congratulations!!! you guessed it right")


    print("Random number is :", rand_number)

    inp = input("Do you want to continue : (continue/exit)")

    if inp == "exit":
        break

