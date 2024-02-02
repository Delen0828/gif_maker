import matplotlib.animation as anime
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import random
import pickle
SAMPLE_TIME=1
DURATION=100
SPIKE_H=10

with open('mean.pkl','rb') as f:
	mean_list=pickle.load(f)
with open('var.pkl','rb') as f:
	var_list=pickle.load(f)
def xList_create(duration):
	return list(range(0,duration,1))
def yList_create(index,avg,var,spike,spike_h,duration):
	baseline=np.ones(duration)*avg
	variation=np.random.random(duration)*var
	if spike is True:
		variation[np.random.randint(duration)]+=spike_h*var
	return baseline+variation


###############
### 2 Lines ###
###############

def sampler_2line(cfg,high_data,low_data):
	if cfg == 'hh':
		return random.sample(high_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'hl':
		return random.sample(high_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'lh':
		return random.sample(low_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'll':
		return random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	else:
		return None
	
LINE_NUM=2
AVG_HIGH=[i for i in mean_list if i > np.median(mean_list)]
AVG_LOW=[i for i in mean_list if i < np.median(mean_list)]
AVG_CFG2=['hh','hl','lh','ll']
VAR_HIGH=[i for i in var_list if i > np.median(var_list)]
VAR_LOW=[i for i in var_list if i < np.median(var_list)]
VAR_CFG2=['hh','hl','lh','ll']
SPIKE_CFG2=['hh','hl','lh','ll']
CFG_LIST=[]

IBM_PALLETE=['#648FFF','#DC267F','#FE6100','#FFB000'] 
COLOR_NAME=['b','r','o','y']
for acfg in AVG_CFG2:
	for vcfg in VAR_CFG2:
		for scfg in SPIKE_CFG2:
			CFG_LIST.append((acfg,vcfg,scfg))
			
def draw(cfg):
	acfg=cfg[0]
	vcfg=cfg[1]
	scfg=cfg[2]		
	fig = plt.figure()
	xList=[] #Length of the line
	yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
	lineList=[]
	pallete=IBM_PALLETE[:LINE_NUM]
	colorName=''
	for color in pallete:
		colorName+=(COLOR_NAME[IBM_PALLETE.index(color)])
	AVG=sampler_2line(acfg,AVG_HIGH,AVG_LOW)
	VAR=sampler_2line(vcfg,VAR_HIGH,VAR_LOW)
	SPIKE=sampler_2line(scfg,[True],[False])
	for i in range(LINE_NUM):
		l, = plt.plot([], [], color=pallete[i])
		xList.append(xList_create(DURATION))
		yList.append(yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
		plt.xlim(0,DURATION) #depend on Duration
		plt.ylim(0,500) #TODO: How to determine the upper bound?
		lineList.append(l)
	plt.close()

	writer = anime.PillowWriter(fps=50)

	with writer.saving(fig, f"gif/trace/line2/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}.gif", 100):
		for i in range(LINE_NUM):
			for j in range(DURATION):
				lineList[i].set_data(xList[i][:j], yList[i][:j])
				writer.grab_frame()

###############
### 3 Lines ###
###############

def sampler_3line(cfg,high_data,low_data):
	if cfg == 'hhh':
		return random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'hll':
		return random.sample(high_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'lhl':
		return random.sample(low_data,1)[0],random.sample(high_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'llh':
		return random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'lll':
		return random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	else:
		return None
	
LINE_NUM=3
AVG_HIGH=[i for i in mean_list if i > np.median(mean_list)]
AVG_LOW=[i for i in mean_list if i < np.median(mean_list)]
AVG_CFG3=['hhh','hll','lhl','llh','lll']
VAR_HIGH=[i for i in var_list if i > np.median(var_list)]
VAR_LOW=[i for i in var_list if i < np.median(var_list)]
VAR_CFG3=['hhh','hll','lhl','llh','lll']
SPIKE_CFG3=['hhh','hll','lhl','llh','lll']


IBM_PALLETE=['#648FFF','#DC267F','#FE6100','#FFB000'] 
COLOR_NAME=['b','r','o','y']
for acfg in AVG_CFG3:
	for vcfg in VAR_CFG3:
		for scfg in SPIKE_CFG3:
			fig = plt.figure()
			xList=[] #Length of the line
			yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
			lineList=[]
			pallete=IBM_PALLETE[:LINE_NUM]
			colorName=''
			for color in pallete:
				colorName+=(COLOR_NAME[IBM_PALLETE.index(color)])
			AVG=sampler_3line(acfg,AVG_HIGH,AVG_LOW)
			VAR=sampler_3line(vcfg,VAR_HIGH,VAR_LOW)
			SPIKE=sampler_3line(scfg,[True],[False])
			for i in range(LINE_NUM):
				l, = plt.plot([], [], color=pallete[i])
				xList.append(xList_create(DURATION))
				yList.append(yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
				plt.xlim(0,DURATION) #depend on Duration
				plt.ylim(0,500) #TODO: How to determine the upper bound?
				lineList.append(l)
			plt.close()

			writer = anime.PillowWriter(fps=50)

			with writer.saving(fig, f"gif/trace/line3/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}.gif", 100):
				for i in range(LINE_NUM):
					for j in range(DURATION):
						lineList[i].set_data(xList[i][:j], yList[i][:j])
						writer.grab_frame()

def sampler_4line(cfg,high_data,low_data):
	if cfg == 'hhhh':
		return random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'hlll':
		return random.sample(high_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'lhll':
		return random.sample(low_data,1)[0],random.sample(high_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'llhl':
		return random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(high_data,1)[0],random.sample(low_data,1)[0]	
	elif cfg == 'lllh':
		return random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'llll':
		return random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	else:
		return None
	
LINE_NUM=4
AVG_HIGH=[i for i in mean_list if i > np.median(mean_list)]
AVG_LOW=[i for i in mean_list if i < np.median(mean_list)]
AVG_CFG4=['hhhh','hlll','lhll','llhl','lllh','llll']
VAR_HIGH=[i for i in var_list if i > np.median(var_list)]
VAR_LOW=[i for i in var_list if i < np.median(var_list)]
VAR_CFG4=['hhhh','hlll','lhll','llhl','lllh','llll']
SPIKE_CFG4=['hhhh','hlll','lhll','llhl','lllh','llll']


IBM_PALLETE=['#648FFF','#DC267F','#FE6100','#FFB000'] 
COLOR_NAME=['b','r','o','y']
for acfg in AVG_CFG4:
	for vcfg in VAR_CFG4:
		for scfg in SPIKE_CFG4:
			fig = plt.figure()
			xList=[] #Length of the line
			yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
			lineList=[]
			pallete=IBM_PALLETE[:LINE_NUM]
			colorName=''
			for color in pallete:
				colorName+=(COLOR_NAME[IBM_PALLETE.index(color)])
			AVG=sampler_4line(acfg,AVG_HIGH,AVG_LOW)
			VAR=sampler_4line(vcfg,VAR_HIGH,VAR_LOW)
			SPIKE=sampler_4line(scfg,[True],[False])
			for i in range(LINE_NUM):
				l, = plt.plot([], [], color=pallete[i])
				xList.append(xList_create(DURATION))
				yList.append(yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
				plt.xlim(0,DURATION) #depend on Duration
				plt.ylim(0,500) #TODO: How to determine the upper bound?
				lineList.append(l)
			plt.close()

			writer = anime.PillowWriter(fps=50)

			with writer.saving(fig, f"gif/trace/line4/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}.gif", 100):
				for i in range(LINE_NUM):
					for j in range(DURATION):
						lineList[i].set_data(xList[i][:j], yList[i][:j])
						writer.grab_frame()