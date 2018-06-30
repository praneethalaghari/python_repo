import random

a = random.sample(range(100),5)  #Command to create random lists
b = random.sample(range(100),8)  #Command to create random lists

print (a)
print (b)

c = [x for x in a if x in b]

print (c)

d = [x*y for x in a for y in b if x%2 == 0]
print(d)