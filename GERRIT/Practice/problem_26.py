
def display_board(colu,board_size):
    print("--"*(board_size*2 +1))
    for a in range(board_size):
       print(" ".join(str(p) for p in colu[a]))
       print("--"* (board_size*2 +1))


def print_coordinates(board_size):
    for a in range(board_size):
        lis_struc = []
        for b in range(board_size*2 +1):
            if b%2 ==0:
                lis_struc.append('')
            else:
                lis_struc.append(str(a)+str(b))
        print(" ".join(str(b) for b in lis_struc))

def check_slot(table,a,b):
    if table[a][b] != " ":
        return False
    else:
        print("It is available")
        return True

def play(colu,board_size):
   while(True):
    display_board(colu,board_size)

    print_coordinates(board_size)

    while(True):
      tuple_play_1_input = input("Player A - Enter the position to set your mark :")
      play_1_input = tuple_play_1_input.split(',')
      while(check_slot(colu,int(play_1_input[0]),int(play_1_input[1]))):
         colu[int(play_1_input[0])][int(play_1_input[1])] = 'a'
         break
      else:
         print("Please select a different co-ordinate")
         continue
      break

    display_board(colu, board_size)

    print_coordinates(board_size)

    while (True):
        tuple_play_2_input = input("Player B - Enter the position to set your mark :")
        play_2_input = tuple_play_2_input.split(',')
        while (check_slot(colu, int(play_2_input[0]), int(play_2_input[1]))):
            colu[int(play_2_input[0])][int(play_2_input[1])] = 'b'
            break
        else:
            print("Please select a different co-ordinate")
            continue
        break

    display_board(colu, board_size)

    print_coordinates(board_size)

    while (True):
        tuple_play_3_input = input("Player C - Enter the position to set your mark :")
        play_3_input = tuple_play_3_input.split(',')
        while (check_slot(colu, int(play_3_input[0]), int(play_3_input[1]))):
            colu[int(play_3_input[0])][int(play_3_input[1])] = 'c'
            break
        else:
            print("Please select a different co-ordinate")
            continue
        break

    '''
        display_board(colu,board_size)

        print_coordinates(board_size)
        tuple_play_1_input = input("Player A - Enter the position to set your mark")
        play_1_input = tuple_play_1_input.split(',')
        colu[int(play_1_input[0])][int(play_1_input[1])] = 'a'

        display_board(colu,board_size)

        print_coordinates(board_size)
        tuple_play_2_input = input("Player B - Enter the position to set your mark")
        play_2_input = tuple_play_2_input.split(',')
        colu[int(play_2_input[0])][int(play_2_input[1])] = 'b'

        display_board(colu, board_size)

        print_coordinates(board_size)
        tuple_play_3_input = input("Player C - Enter the position to set your mark")
        play_3_input = tuple_play_3_input.split(',')
        colu[int(play_3_input[0])][int(play_3_input[1])] = 'c'

        display_board(colu, board_size) '''

    cont = input("Do you want to continue(Y/N)")
    if cont == 'N' or cont == 'n':
     break

def drawboard(board_size=int(input("Enter the size of the board : "))):
    print("--"*(board_size*2 +1))
    list_struct_all = []
    for a in range(board_size):
       list_struct = []
       for b in range(board_size*2 +1):
         if b%2 ==0:
          list_struct.append('|')
         else:
          list_struct.append(' ')
       list_struct_all.append(list_struct)

       print(" ".join(str(x) for x in list_struct))
       print("--"* (board_size*2 +1))
    return list_struct_all,board_size

colu,board_size = drawboard()
play(colu,board_size)

