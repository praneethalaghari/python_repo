

with open("txt1","w+") as f:
     f.write("\n".join([str(k) for k in range(1,1000) if [k for k in range(k,k+1) if [k%y==0 for y in range(2,k)].count(True) == 0]]))

with open("txt2","w+") as g:
    cool = set()

    for n in range(1001):
        temp_n = n
        past = set()

        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in past:
              break
            past.add(n)
        else:
            cool.add(temp_n)
    g.write("\n".join(str(p) for p in sorted(cool)))


with open("txt1","r") as h:
    lin = h.readlines()
    prime_set = set([kt.rstrip('\n') for kt in lin])

with open("txt2","r") as o:
    lin_o = o.readlines()
    happy_set = set([ot.rstrip('\n') for ot in lin_o])

print(prime_set)
print(happy_set)
print((happy_set.intersection(prime_set)))




