import random

list_A = []
for i in range(0, 6):list_A.append(random.randint(0, 100))
print(list_A)

list_B = []
for i in range(0,6):list_B.append(random.randint(0,35))
print(list_B)

print([x for x in list_B if x%2 == 0])


