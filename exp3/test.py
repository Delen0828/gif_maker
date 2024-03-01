from manim import *
import argparse
import numpy as np
# import pandas as pd
import random
import pickle
from tqdm import tqdm
SAMPLE_TIME=1
DURATION=100
SPIKE_H=5


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
# print(args)

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
# LINE_NUM=2
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
# for acfg in AVG_CFG:
# 	for vcfg in VAR_CFG:
# 		for scfg in SPIKE_CFG:
CFG_LIST.append(('hhhl','hhhh','hhll'))

np.random.seed(42)
def xList_create(duration):
	return list(range(0,duration,1))
def yList_create(avg,var,spike,spike_h,duration):
	baseline=np.ones(duration)*avg
	variation=np.random.random(duration)*var
	if spike is True:
		variation[np.random.randint(duration)]+=spike_h*var
	return baseline+variation

def build_plot(axes, x, y, color,is_dot):
	return axes.plot_line_graph(x, y, add_vertex_dots=is_dot, line_color=color)

def scaleAVG(avg,k=4):
	return k*(((avg-np.min(avg))/(np.max(avg)-np.min(avg)))+1)

def scaleVAR(var,k=4):
	return k*(((var-np.min(var))/(np.max(var)-np.min(var)))+1)

class Plot(Scene):
	def load(self):
		with open('mean.pkl','rb') as f:
			mean_list=pickle.load(f)
		with open('var.pkl','rb') as f:
			var_list=pickle.load(f)
		self.AVG_HIGH=[i for i in mean_list if i > np.median(mean_list)]
		self.AVG_LOW=[i for i in mean_list if i < np.median(mean_list)]
		self.VAR_HIGH=[i for i in var_list if i > np.median(var_list)]
		self.VAR_LOW=[i for i in var_list if i < np.median(var_list)]
		
	def construct(self):
		for sample in range(1):
			for idx,cfg in enumerate(CFG_LIST):
				acfg=cfg[0]
				vcfg=cfg[1]
				scfg=cfg[2]
				self.load()
				pallete=IBM_PALLETE
				colorName=''
				for color in pallete:
					colorName+=(COLOR_NAME[IBM_PALLETE.index(color)])

				self.clear()
				AVG=sampler_line(acfg,AVG_HIGH,AVG_LOW)
				VAR=sampler_line(vcfg,VAR_HIGH,VAR_LOW)
				SPIKE=sampler_line(scfg,[True],[False]) #This is deterministic
				maxAVGcolor=colorName[np.argmax([np.max(arr) for arr in (AVG+np.array(SPIKE)*SPIKE_H/100)])]
				SPIKEL=AVG+VAR*(np.array(SPIKE)*SPIKE_H+1) #TODO: check this
				maxVARcolor=colorName[np.argmax([np.max(arr) for arr in (VAR+np.sqrt(((np.array(SPIKE)*SPIKE_H+1)**2-1)/DURATION))])]
				# print(VAR)
				# print(VAR+np.sqrt(((np.array(SPIKE)*SPIKE_H+1)**2-1)/DURATION))
				maxSPIKEcolor=colorName[np.argmax([np.max(arr) for arr in SPIKEL])]
				answer=maxAVGcolor+maxVARcolor+maxSPIKEcolor

				# if idx==0:
				if args.move == 'stat':
					self.next_section(name=f"static_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)
				if args.move=='seq' and args.trace and args.history :
					self.next_section(name=f"seq_trace_his_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)
				if args.move=='seq' and not args.trace and not args.history :	
					self.next_section(name=f"seq_notrace_nohis_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)
				if args.move=='seq' and not args.trace and args.history :	
					self.next_section(name=f"seq_notrace_his_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)
				if args.move=='seq' and args.trace and not args.history :
					self.next_section(name=f"seq_trace_nohis_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)
				if args.move=='sync' and args.trace:
					self.next_section(name=f"sync_trace_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)
				if args.move=='sync' and not args.trace:
					self.next_section(name=f"sync_notrace_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)

				x_min, x_max, x_step = 0, DURATION, 10
				y_min, y_max, y_step = 100, 700, 50
				axes = Axes(
					x_range=[x_min, x_max + x_step, x_step],
					y_range=[y_min, y_max + y_step, y_step],
					tips=False,
					axis_config={'color': BLACK}
				)
				# self.add(axes)
				self.clear()
				if args.move=='seq' and args.trace and args.history :
					for i in range(LINE_NUM):
						self.add(axes) 
						plot=build_plot(axes, xList_create(DURATION), yList_create(AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION), color=pallete[i], is_dot=False)
						self.play(Create(plot,run_time=1,rate_func=rate_functions.unit_interval(linear)))
					self.wait(1)
					# self.next_section(name=f"seq_trace_his_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)
				if args.move=='seq' and not args.trace and not args.history :	
					for i in range(LINE_NUM):
						self.add(axes) 
						plot=build_plot(axes, xList_create(DURATION), yList_create(AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION),color=pallete[i], is_dot=True)
						d1 = Dot(color=pallete[i]).move_to(axes.c2p(0, 0))
						line_graph = plot["line_graph"]
						self.play(MoveAlongPath(d1, line_graph),run_time=1, rate_func=linear)
						self.remove(d1)
					self.wait(1)
					# self.next_section(name=f"seq_notrace_nohis_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)
				if args.move=='sync' and args.trace:
					self.add(axes) 
					plotlist=[]
					for i in range(LINE_NUM):
						time=1*LINE_NUM
						plotlist.append(build_plot(axes, xList_create(DURATION), yList_create(AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION), color=pallete[i], is_dot=False))
					if LINE_NUM == 2:
						self.play(Create(plotlist[0],run_time=time,rate_func=rate_functions.unit_interval(linear)),Create(plotlist[1],run_time=time,rate_func=rate_functions.unit_interval(linear)))
					if LINE_NUM == 3:
						self.play(Create(plotlist[0],run_time=time,rate_func=rate_functions.unit_interval(linear)),Create(plotlist[1],run_time=time,rate_func=rate_functions.unit_interval(linear)),Create(plotlist[2],run_time=time,rate_func=rate_functions.unit_interval(linear)))
					if LINE_NUM == 4:
						self.play(Create(plotlist[0],run_time=time,rate_func=rate_functions.unit_interval(linear)),Create(plotlist[1],run_time=time,rate_func=rate_functions.unit_interval(linear)),Create(plotlist[2],run_time=time,rate_func=rate_functions.unit_interval(linear)),Create(plotlist[3],run_time=time,rate_func=rate_functions.unit_interval(linear)))
					self.wait(1)
					# self.next_section(name=f"sync_trace_{LINE_NUM}_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.mp4",type=answer)
				if args.move=='sync' and not args.trace:
					self.add(axes) 
					time=1*LINE_NUM
					plotlist=[]
					scaledAVG=scaleAVG(AVG)
					# scaledVAR=scaleVAR(VAR)
					for i in range(LINE_NUM):
						plot=build_plot(axes, xList_create(DURATION), yList_create(AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION),color=pallete[i], is_dot=True)
						d1 = Dot(color=pallete[i]).move_to(axes.c2p(0, 0))
						b = TracedPath(d1.get_center, stroke_color=pallete[i],stroke_width=2,dissipating_time=0.2)
						self.add(b)
						line_graph = plot["line_graph"]
						plotlist.append(MoveAlongPath(d1, line_graph,run_time=scaledAVG[i]))
					if LINE_NUM == 2:
						self.play(plotlist[0],plotlist[1], rate_func=linear)
					elif LINE_NUM == 3:
						self.play(plotlist[0],plotlist[1],plotlist[2], rate_func=linear)
					elif LINE_NUM == 4:
						self.play(plotlist[0],plotlist[1],plotlist[2],plotlist[3], rate_func=linear)
					self.wait(1)

if args.move=='seq' and args.trace and args.history :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"sample/seq_trace_his{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='seq' and args.trace and not args.history :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"sample/seq_trace_nohis{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='seq' and not args.trace and args.history :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"sample/seq_notrace_his{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='seq' and not args.trace and not args.history :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"sample/seq_notrace_nohis{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='sync' and args.trace :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"sample/sync_trace{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='sync' and not args.trace:
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"sample/sync_notrace{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='stat':
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"sample/static{LINE_NUM}","flush_cache":True,"progress_bar":'none'}

with tempconfig(cfg):
	scene = Plot()
	scene.render()