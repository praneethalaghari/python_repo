import random

def generatepassword(password_length):
    dict_A = {'1': 'A','2': 'B','3': 'C','4': 'D','5': 'E','6': 'F','7': 'G','8': 'H','9': 'I','10': 'J','11': 'K','12': 'L','13': 'M','14':'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y','26': 'Z'}
    dict_B = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j',
              '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's',
              '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}
    password = []

    for x in range(0,password_length):
        variant = random.randint(0,2)
        if variant == 0:
            password.append(dict_A[str(random.randint(1,26))])
        elif variant == 1:
            password.append(str(random.randint(0,10)))
        else:
            password.append(dict_B[str(random.randint(1, 26))])


    str_passwd = "".join(str(x) for x in password) # This is to convert a list containing integer to make it a string
    print(str_passwd)

    return str_passwd


def main():
    while (1):
        password_prompt = input('Do you wish to generate a new password Enter - Y')
        print(password_prompt)

        if password_prompt != 'Y' and password_prompt !='y':
            break

        password_length = int(input('Enter the length of password to generate (MAX - 8 MIN - 4)'))

        if not 4 <= password_length <= 8:
            print("Max length should be 8  and  Min length should be 4")
            continue

        password = generatepassword(password_length)
        print(password)

if __name__ == '__main__':
    main()