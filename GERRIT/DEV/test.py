import functools


col = [1,2,3,4]
print(map(lambda x,y:x*y, col))
print(functools.reduce(lambda x,y:x*y,col))