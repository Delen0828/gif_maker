import random
from matplotlib import pyplot as plt
import numpy as np

def func(x):
	A=4-8*random.random()
	B=4-8*random.random()
	C=5-8*random.random()
	return A*np.sin(B*x+C)

def rand_func():
	xlist=[]
	ylist=[]
	for xval in np.linspace(-10, 10, 100):
		xlist.append(xval)
		temp_y=0
		for _ in range(0,8):
			temp_y+=func(xval)
		ylist.append(temp_y)
	return xlist, ylist

# plt.plot(xlist,ylist)
# plt.savefig('test.png')