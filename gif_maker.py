import matplotlib.animation as anime
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import random
import pickle

with open('mean.pkl','rb') as f:
	mean_list=pickle.load(f)
with open('var.pkl','rb') as f:
	var_list=pickle.load(f)
def xList_create(duration):
	return list(range(0,duration,1))
def yList_create(index,avg,var,spike,spike_h,duration):
	baseline=np.ones(duration)*avg
	variation=np.random.random(duration)*var
	if (spike[0] > 1):
		variation[np.random.randint(duration)]+=spike_h*var
	return baseline+variation

DURATION=100
LINE_NUM=2
#TODO: Devide AVG sample in to low medium high based on line 2,3,4
#TODO: Same for VAR
#TODO Based on low/high 
# AVG_LIST=[[-5,5],[5,-5],[-5,-5],[5,5]]
# VAR_LIST=[[6,3],[3,6],[3,3],[6,6]]
# SPIKE_LIST=[[0,1],[1,0],[0,0],[1,1]]
AVG_HIGH2=[i for i in mean_list if i > np.median(mean_list)]
AVG_LOW2=[i for i in mean_list if i < np.median(mean_list)]
# print(AVG_LOW)
SPIKE_H=10
CBF_PALLETE=['#648FFF','#DC267F','#FE6100','#FFB000'] 
CBF_NAME=['b','r','o','y']
# for AVG in AVG_LIST:
# 	for VAR in VAR_LIST:
# 		for SPIKE in SPIKE_LIST:
fig = plt.figure()
xList=[] #Length of the line
yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
lineList=[]
pallete=random.sample(CBF_PALLETE,k=LINE_NUM)
colorName=''
for color in pallete:
	colorName+=(CBF_NAME[CBF_PALLETE.index(color)])
for i in range(LINE_NUM):
	l, = plt.plot([], [], color=pallete[i])
	AVG=int(random.sample(mean_list,1)[0])
	VAR=int(random.sample(var_list,1)[0])
	SPIKE=random.sample([1,5],1)
	xList.append(xList_create(DURATION))
	yList.append(yList_create(i,AVG,VAR,SPIKE,SPIKE_H,DURATION))
	plt.xlim(0,DURATION) #depend on Duration
	plt.ylim(0, 500)
	lineList.append(l)
plt.close()

writer = anime.PillowWriter(fps=50)

with writer.saving(fig, f"gif/trace_AVG{AVG}_VAR{VAR}_SPIKE{SPIKE}_{colorName}.gif", 100):
	for i in range(LINE_NUM):
		for j in range(DURATION):
			lineList[i].set_data(xList[i][:j], yList[i][:j])
			writer.grab_frame()
# print(DURATION*LINE_NUM/50)