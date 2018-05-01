import random

a = random.sample(range(10,100),5)
print(a)

b = [1, 1, 2, 2, 3, 3, 4, 4]
print(b)

c = set(b)  #Python is converting list into set thus eliminating duplicates
print(c)

d = [1,1,4,5,6,7,7,8,8,9]
e = []
for x in d :
    if x not in e:
        e.append(x)
print(e)