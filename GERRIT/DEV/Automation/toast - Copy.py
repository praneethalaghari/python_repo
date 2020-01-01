import matplotlib.pyplot as plt
import os

axes = plt.plot([1,2,3,4,5,6,7,8,9,10],[81,78,65,59,48,51,62,74,83,91])
axes.set_xlabel('Time(in mins)')
axes.set_ylabel('Battery %')
axes.suptitle('Battery Analysis')
axes.set_xticks(range(0,20,5))
axes.set_yticks(range(0,100,10))

plt.savefig('plot.png')
os.startfile('plot.png')