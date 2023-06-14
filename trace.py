import matplotlib.animation as anime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from rand_func import rand_func

fig = plt.figure()
l, = plt.plot([], [], 'k-')
l2, = plt.plot([], [], 'r--')
# p1, = plt.plot([], [], 'ko')
# p2, = plt.plot([], [], 'mo')

plt.xlim(-10, 10)
plt.ylim(-20, 20)
 
metadata = dict(title="Movie", artist="sourabh")
writer = anime.PillowWriter(fps=50, metadata=metadata)

with writer.saving(fig, "trace.gif", 100):
	xlist, ylist=rand_func()
	for i in range(0,100):
		l.set_data(xlist[:i], ylist[:i])
		writer.grab_frame()
	xlist2, ylist2=rand_func()
	for i in range(0,100):
		l2.set_data(xlist2[:i], ylist2[:i])
		writer.grab_frame()