import random


def guess_number():
   guess_num = random.randint(1,100)
   number_of_guess = 0
   list_of_coll = []
   minimum = 1
   maximum = 100

   while True:
       number_of_guess += 1
       print(guess_num)
       assertion = input("Choose the following : 1. choose_num > guess_num 2. choose_num < guess_num 3. choose_num == guess_naum 4.Exit")
       list_of_coll.append(guess_num)

       if int(assertion) == 1:
           choose_num_is_less_than_guess_num = False
       elif int(assertion) == 2:
           choose_num_is_less_than_guess_num = True
       elif int(assertion) == 3:
           return guess_num,number_of_guess
       elif int(assertion) == 4:
           return None,None





       if choose_num_is_less_than_guess_num:
          if number_of_guess == 1:
            guess_num = random.randint(1, guess_num)
          else:
            maximum = guess_num
            guess_num = random.randint(minimum, maximum)
            if guess_num in list_of_coll:
                continue
       else:
          if number_of_guess == 1:
            guess_num = random.randint(guess_num, 100)
          else:
            minimum = guess_num
            guess_num = random.randint(minimum, maximum)
            if guess_num in list_of_coll:
                continue


print("Choose a number between 1-100")
number,number_of_guess = guess_number()

if number_of_guess != None:
 print("Congrats!!! you won in " + str(number_of_guess) + "chances")
else:
 print("Interruption!!!")