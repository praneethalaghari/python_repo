name = input("Enter a string :")
flag = 0

for i in range(0, int(len(name)/2)):
    if name[i] != name[len(name)-i-1]:
        flag = 1
        break

if not flag:
    print("Voila,The input given is a palindrome")