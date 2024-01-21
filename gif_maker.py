import matplotlib.animation as anime
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import random

def xlist_create(duration):
	return list(range(0,duration,1))
def ylist_create(index,avg,var,spike,spike_h,duration):
	baseline=np.ones(duration)*avg
	variation=np.random.random(duration)*var
	if (spike == 1):
		variation[np.random.randint(duration)]+=spike_h*var
	return baseline+variation

DURATION=100
LINE_NUM=2
AVG_LIST=[[-5,5],[5,-5],[-5,-5],[5,5]]
VAR_LIST=[[6,3],[3,6],[3,3],[6,6]]
SPIKE_LIST=[[0,1],[1,0],[0,0]]
SPIKE_H=5
CBF_PALLETE=['#000000','#F35555','#56B0FF','#E6E335']
for AVG in AVG_LIST:
	for VAR in VAR_LIST:
		for SPIKE in SPIKE_LIST:
			fig = plt.figure()
			xlist=[] #Length of the line
			ylist=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
			linelist=[]
			pallete=random.sample(CBF_PALLETE,k=LINE_NUM)
			for i in range(LINE_NUM):
				l, = plt.plot([], [], color=pallete[i])
				xlist.append(xlist_create(DURATION))
				ylist.append(ylist_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
				plt.xlim(0,DURATION) #depend on Duration
				plt.ylim(-min(ylist[-1])-max(VAR), max(ylist[-1])+max(VAR))
				linelist.append(l)
			
			writer = anime.PillowWriter(fps=50)

			with writer.saving(fig, f"gif/trace_AVG{AVG}_VAR{VAR}_SPIKE{SPIKE}.gif", 100):
				for i in range(LINE_NUM):
					for j in range(DURATION):
						linelist[i].set_data(xlist[i][:j], ylist[i][:j])
						writer.grab_frame()