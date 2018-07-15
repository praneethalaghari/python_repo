def hot():
    print(a)

global cool
def cool():
   global a
   a = 5
   print(a)
   print(b)


b = 9
cool()
hot()
#print(a)