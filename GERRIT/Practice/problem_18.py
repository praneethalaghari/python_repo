# COWS - BULLS Game
import random


def generate_random_number(num=int(input('Enter the length of random integer :'))):
    random_num = random.sample(range(0, 9), num)
    return "".join(str(x) for x in random_num)


if __name__ == '__main__':
    to_generate = generate_random_number()
    #print(to_generate)
    tries = 0

    while True:
        user_input = input("Enter a number to match : ")

        if len(user_input) != len(to_generate):
            print("Please enter an " + str(len(to_generate)) + " number")
            continue


        cows = 0
        bulls = 0
        tries += 1

        for i in range(0, len(to_generate)):
            if user_input[i] == to_generate[i]:
                cows += 1
            else:
                bulls += 1

        print("Cows : " + str(cows) + "  Bulls : " + str(bulls))

        if user_input == to_generate:
            print(" Hurray!!! you guessed it right in " + str(tries) + " trails")
            break

        choice = input('Do you want to continue : (Y/N)')
        if choice == 'N' or choice == 'n':
            break
