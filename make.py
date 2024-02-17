import argparse
import matplotlib.animation as anime
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import random
import pickle
SAMPLE_TIME=1
DURATION=100
SPIKE_H=10


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Sample")

# Define the expected named arguments
parser.add_argument("--line", type=int, help="line number")
parser.add_argument("--trace", type=bool, default=False)
parser.add_argument("--history", type=bool, default=False)
parser.add_argument("--move", choices=['seq','sync', 'stat'],help="seq or sync or stat")
parser.add_argument("--static", type=bool, default=False)
parser.add_argument("--sample", type=int, default=5)

# Parse the command-line arguments
args = parser.parse_args()
print(args)

with open('mean.pkl','rb') as f:
	mean_list=pickle.load(f)
with open('var.pkl','rb') as f:
	var_list=pickle.load(f)


def sampler_line(cfg,high_data,low_data):
	if cfg == 'hh':
		return random.sample(high_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'hl':
		return random.sample(high_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'lh':
		return random.sample(low_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'll':
		return random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'hhh':
		return random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'hll':
		return random.sample(high_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'hhl':
		return random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'lll':
		return random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'hhhh':
		return random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(high_data,1)[0]
	elif cfg == 'hlll':
		return random.sample(high_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'hhll':
		return random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	elif cfg == 'hhhl':
		return random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(high_data,1)[0],random.sample(low_data,1)[0]	
	elif cfg == 'llll':
		return random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0],random.sample(low_data,1)[0]
	else:
		return None
	
LINE_NUM=args.line

AVG_HIGH=[i for i in mean_list if i > np.median(mean_list)]
AVG_LOW=[i for i in mean_list if i < np.median(mean_list)]
VAR_HIGH=[i for i in var_list if i > np.median(var_list)]
VAR_LOW=[i for i in var_list if i < np.median(var_list)]

if LINE_NUM==2:
	AVG_CFG=['hh','hl','ll']
	VAR_CFG=['hh','hl','ll']
	SPIKE_CFG=['hh','hl','ll']
elif LINE_NUM==3:
	AVG_CFG=['hhh','hhl','hll','lll']
	VAR_CFG=['hhh','hhl','hll','lll']
	SPIKE_CFG=['hhh','hhl','hll','lll']	
elif LINE_NUM==4:
	AVG_CFG=['hhhh','hhhl','hhll','hlll','llll']
	VAR_CFG=['hhhh','hhhl','hhll','hlll','llll']
	SPIKE_CFG=['hhhh','hhhl','hhll','hlll','llll']

CFG_LIST=[]

IBM_PALLETE=['#117733','#88CCEE','#DDCC77','#AA4499'] 
COLOR_NAME=['g','b','y','p']
for acfg in AVG_CFG:
	for vcfg in VAR_CFG:
		for scfg in SPIKE_CFG:
			CFG_LIST.append((acfg,vcfg,scfg))
			
def draw(cfg,args):
	for sample in range(args.sample):
		acfg=cfg[0]
		vcfg=cfg[1]
		scfg=cfg[2]		
		fig = plt.figure()
		pallete=random.sample(IBM_PALLETE,LINE_NUM)
		colorName=''
		for color in pallete:
			colorName+=(COLOR_NAME[IBM_PALLETE.index(color)])
		AVG=sampler_line(acfg,AVG_HIGH,AVG_LOW)
		VAR=sampler_line(vcfg,VAR_HIGH,VAR_LOW)
		SPIKE=sampler_line(scfg,[True],[False]) #This is deterministic

		writer = anime.PillowWriter(fps=50)
		if args.move=='seq' and args.trace and args.history :
			xList=[] #Length of the line
			yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
			lineList=[]
			for i in range(LINE_NUM):
				l, = plt.plot([], [], color=pallete[i])
				xList.append(xList_create(DURATION))
				yList.append(yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
				plt.xlim(0,DURATION) #depend on Duration
				plt.ylim(0,max(500,max(AVG+VAR*(SPIKE_H+1))) )
				lineList.append(l)
			plt.close()
			with writer.saving(fig, f"testgif/seq_trace_his/line{LINE_NUM}/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.gif", 100):
				for i in range(LINE_NUM):
					for j in range(DURATION):
						lineList[i].set_data(xList[i][:j], yList[i][:j])
						writer.grab_frame()
				for _ in range(200):
					writer.grab_frame()
		elif args.move=='seq' and args.trace and not args.history :
			xList=[] #Length of the line
			yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
			lineList=[]
			for i in range(LINE_NUM):
				l, = plt.plot([], [], color=pallete[i])
				xList.append(xList_create(DURATION))
				yList.append(yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
				plt.xlim(0,DURATION) #depend on Duration
				plt.ylim(0,max(500,max(AVG+VAR*(SPIKE_H+1))) )
				lineList.append(l)
			plt.close()
			with writer.saving(fig, f"testgif/seq_trace_nohis/line{LINE_NUM}/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.gif", 100):
				for i in range(LINE_NUM):
					for j in range(DURATION):
						lineList[i].set_data(xList[i][:j], yList[i][:j])
						writer.grab_frame()
					lineList[i].set_data([],[])
				for _ in range(200):
					writer.grab_frame()
		elif args.move=='seq' and not args.trace and args.history :
			xList=[] #Length of the line
			yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
			lineList=[]
			sublineList=[]
			for i in range(LINE_NUM):
				l, = plt.plot([], [], color=pallete[i],marker='o')
				subl, =plt.plot([], [], color=pallete[i])
				xList.append(xList_create(DURATION))
				yList.append(yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
				plt.xlim(0,DURATION) #depend on Duration
				plt.ylim(0,max(500,max(AVG+VAR*(SPIKE_H+1))) )
				lineList.append(l)
				sublineList.append(subl)
			plt.close()
			with writer.saving(fig, f"testgif/seq_notrace_his/line{LINE_NUM}/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.gif", 100):
				for i in range(LINE_NUM):
					for j in range(DURATION):
						lineList[i].set_data([xList[i][j]], [yList[i][j]])
						writer.grab_frame()
					lineList[i].set_data([],[])
					sublineList[i].set_data(xList[i][:DURATION], yList[i][:DURATION])
					writer.grab_frame()
				for _ in range(200):
					writer.grab_frame()
		elif args.move=='seq' and not args.trace and not args.history :
			xList=[] #Length of the line
			yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
			lineList=[]
			for i in range(LINE_NUM):
				l, = plt.plot([], [], color=pallete[i],marker='o')
				xList.append(xList_create(DURATION))
				yList.append(yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
				plt.xlim(0,DURATION) #depend on Duration
				plt.ylim(0,max(500,max(AVG+VAR*(SPIKE_H+1))) )
				lineList.append(l)
			plt.close()
			with writer.saving(fig, f"testgif/seq_notrace_nohis/line{LINE_NUM}/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.gif", 100):
				for i in range(LINE_NUM):
					for j in range(DURATION):
						lineList[i].set_data([xList[i][j]], [yList[i][j]])
						writer.grab_frame()
				for _ in range(200):
					writer.grab_frame()
		elif args.move=='sync' and args.trace :
			xList=[] #Length of the line
			yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
			lineList=[]
			for i in range(LINE_NUM):
				l, = plt.plot([], [], color=pallete[i])
				xList.append(xList_create(DURATION))
				yList.append(yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
				plt.xlim(0,DURATION) #depend on Duration
				plt.ylim(0,max(500,max(AVG+VAR*(SPIKE_H+1))) )
				lineList.append(l)
			plt.close()
			with writer.saving(fig, f"testgif/sync_trace/line{LINE_NUM}/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.gif", 100):
				for j in range(DURATION):
					for i in range(LINE_NUM):
						lineList[i].set_data(xList[i][:j], yList[i][:j])
						writer.grab_frame()
				for _ in range(200):
					writer.grab_frame()
		elif args.move=='sync' and not args.trace:
			xList=[] #Length of the line
			yList=[] #function that INPUT: AVG,VAR,SPIKE,OUTPUT: A series of num
			lineList=[]
			for i in range(LINE_NUM):
				l, = plt.plot([], [], color=pallete[i],marker='o')
				xList.append(xList_create(DURATION))
				yList.append(yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION))
				plt.xlim(0,DURATION) #depend on Duration
				plt.ylim(0,max(500,max(AVG+VAR*(SPIKE_H+1))) )
				lineList.append(l)
			plt.close()
			with writer.saving(fig, f"testgif/sync_notrace/line{LINE_NUM}/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.gif", 100):
				for j in range(DURATION):
					for i in range(LINE_NUM):
						lineList[i].set_data([xList[i][j]], [yList[i][j]])
						writer.grab_frame()
				for _ in range(200):
					writer.grab_frame()

def static_draw(cfg,args):
	for sample in range(args.sample):
		acfg=cfg[0]
		vcfg=cfg[1]
		scfg=cfg[2]		
		fig = plt.figure(dpi=100)
		pallete=random.sample(IBM_PALLETE,LINE_NUM)
		colorName=''
		for color in pallete:
			colorName+=(COLOR_NAME[IBM_PALLETE.index(color)])
		AVG=sampler_line(acfg,AVG_HIGH,AVG_LOW)
		VAR=sampler_line(vcfg,VAR_HIGH,VAR_LOW)
		SPIKE=sampler_line(scfg,[True],[False]) #This is deterministic
		plt.xlim(0,DURATION) #depend on Duration
		plt.ylim(0,max(500,max(AVG+VAR*(SPIKE_H+1))) )
		for i in range(LINE_NUM):
			plt.plot(xList_create(DURATION), yList_create(i,AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION),color=pallete[i])
		fig.savefig(f"testgif/static/line{LINE_NUM}/static_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.png")
		plt.close()
if args.static is True:
	for cfg in CFG_LIST:
		static_draw(cfg,args)
else:
	for cfg in CFG_LIST:
		draw(cfg,args)