
import random

player_A = input("Please Enter player 1 name :")
player_B = input("Please Enter player 2 name :")

choice = 'y'
game = 1
wins_for_player_A = 0
wins_for_player_B = 0
tie = 0

dict = {'1': "Paper", '2': "Scissors",'3': "Rock"}



while choice == 'y' or choice == 'Y':
    print("Game :", game)
    win_records = {}
    winner = "default"

    player_A_result = random.randint(1,3)
    print(player_A, " :", dict[str(player_A_result)])

    player_B_result = random.randint(1,3)
    print(player_B, " :", dict[str(player_B_result)])

    win_records[player_A] = player_A_result
    win_records[player_B] = player_B_result

    print(win_records.values())


    if ( player_A_result == player_B_result):
        print("Match Drawn both are same")
        tie+=1
        contineu = input(" Do you want to continue the game : Y/N ")
        if contineu == 'y' or contineu == 'Y':
            game += 1
            continue
        else:
            break
        continue



    if 1 in win_records.values() and 2 in win_records.values():
        print("Congratulations!!! Winner is :",list(win_records.keys())[list(win_records.values()).index(2)])
        winner = list(win_records.keys())[list(win_records.values()).index(2)]

    if 2 in win_records.values() and 3 in win_records.values():
        print("Congratulations!!! Winner is :",list(win_records.keys())[list(win_records.values()).index(3)])
        winner = list(win_records.keys())[list(win_records.values()).index(3)]

    if 3 in win_records.values() and 1 in win_records.values():
        print("Congratulations!!! Winner is :",list(win_records.keys())[list(win_records.values()).index(1)])
        winner = list(win_records.keys())[list(win_records.values()).index(1)]

    if winner == player_A:
        wins_for_player_A+=1
    else:
        wins_for_player_B+=1


    print ("Total wins for ", player_A, " : ", wins_for_player_A)
    print ("Total wins for ", player_B, " : ", wins_for_player_B)
    print ("Total ties are ", tie)



    contineu = input(" Do you want to continue the game : Y/N ")
    if contineu == 'y' or contineu == 'Y':
        game+=1
        continue
    else:
        break