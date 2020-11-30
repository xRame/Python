import random
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from sklearn import datasets
#iris = datasets.load_iris()

random.seed(4, version=2) 
time = (20-8)*60
t=[8,9,10,11,12,13,14,15,16,17,18,19,20]
interaval = [5,10]
cnt_b = 0
cnt_p = 0
bus_list= []
p_list= []
while time > 0:
	r = random.choice(interaval)
	time -= r
	cnt_b+=1
	p_list.append(r)
	if time % 60 == 0:
		bus_list.append(cnt_b)
		cnt_b = 0
	

x = range(len(bus_list))
ax = plt.gca()
ax.bar(x, bus_list, align='edge') # align='edge' - выравнивание по границе, а не по центру
ax.set_xticks(x)
ax.set_xticklabels(t)
plt.show()

disp = np.var(p_list)
math_wait = 5*.5+10*.5
print("dispersion = "+ str(disp))
print("math_wait = "+ str(math_wait))
x = range(len(p_list))
ax = plt.gca()
ax.bar(x, p_list, align='edge') # align='edge' - выравнивание по границе, а не по центру
ax.set_xticks(x)
plt.show()