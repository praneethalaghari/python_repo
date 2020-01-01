import matplotlib.pyplot as plt
import os

fig = plt.plot([1,2,3,4,5,6,7,8,9,10],[81,78,65,59,48,51,62,74,83,91])
plt.xlabel('Time(in mins)')
plt.ylabel('Battery %')
plt.suptitle('Battery Analysis')
print(fig)
plt.xticks(range(0,20,5))
plt.yticks(range(0,100,10))

plt.savefig('plot.png')
os.startfile('plot.png')