
def drawboard(board_size=int(input("Enter the size of the board : "))):
    print("--"*(board_size*2 +1))
    for a in range(board_size):
       list_struct = []
       for b in range(board_size*2 +1):
         if b%2 ==0:
          list_struct.append('|')
         else:
          list_struct.append(' ')

       print(" ".join(str(x) for x in list_struct))
       print("--"* (board_size*2 +1))

drawboard()