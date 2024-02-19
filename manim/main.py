from manim import *
import argparse
import numpy as np
# import pandas as pd
import random
import pickle
from tqdm import tqdm
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
for acfg in AVG_CFG:
	for vcfg in VAR_CFG:
		for scfg in SPIKE_CFG:
			CFG_LIST.append((acfg,vcfg,scfg))

def xList_create(duration):
	return list(range(0,duration,1))
def yList_create(avg,var,spike,spike_h,duration):
	baseline=np.ones(duration)*avg
	variation=np.random.random(duration)*var
	if spike is True:
		variation[np.random.randint(duration)]+=spike_h*var
	return baseline+variation

def build_plot(axes, x, y, color):
	line = axes.plot_line_graph(x, y, add_vertex_dots=False, line_color=color)
	return VDict({"line": line})

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
		for cfg in tqdm(CFG_LIST):
			acfg=cfg[0]
			vcfg=cfg[1]
			scfg=cfg[2]
			self.load()
			pallete=random.sample(IBM_PALLETE,LINE_NUM)
			colorName=''
			for color in pallete:
				colorName+=(COLOR_NAME[IBM_PALLETE.index(color)])
			self.next_section(name=f"trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}.gif")	
			self.clear()
			AVG=sampler_line('hhhh',AVG_HIGH,AVG_LOW)
			VAR=sampler_line('hhhh',VAR_HIGH,VAR_LOW)
			SPIKE=sampler_line('llll',[True],[False]) #This is deterministic
			x_min, x_max, x_step = 0, DURATION, 10
			y_min, y_max, y_step = 200, 700, 100
			axes = Axes(
				x_range=[x_min, x_max + x_step, x_step],
				y_range=[y_min, y_max + y_step, y_step],
				tips=False,
				axis_config={'color': BLACK}
			)
			self.add(axes)
			#TODO: USE ARGS HERE
			# if args.move=='seq' and args.trace and args.history :
			for i in range(LINE_NUM):
				plot=build_plot(axes, xList_create(DURATION), yList_create(AVG[i],VAR[i],SPIKE[i],SPIKE_H,DURATION), color=pallete[i])
				self.play(Create(plot["line"],run_time=1,rate_func=rate_functions.unit_interval(linear)))
			
			# config["output_file"]=f"trace_{colorName}.gif"
			# with writer.saving(fig, f"testgif/seq_trace_his/line{LINE_NUM}/trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}_{sample}.gif", 100):
			self.wait()
			self.next_section(name=f"trace_AVG{acfg}_VAR{vcfg}_SPIKE{scfg}_{colorName}.gif")


#TODO: USE ARGS HERE
if args.move=='seq' and args.trace and args.history :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"seq_trace_his{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='seq' and args.trace and not args.history :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"seq_trace_nohis{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='seq' and not args.trace and args.history :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"seq_notrace_his{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='seq' and not args.trace and not args.history :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"seq_notrace_nohis{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='sync' and args.trace :
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"sync_trace{LINE_NUM}","flush_cache":True,"progress_bar":'none'}
elif args.move=='sync' and not args.trace:
	cfg={"quality": "low_quality","frame_rate":60,"background_color": WHITE, "save_sections": True, "silent":True, "verbosity": 'ERROR',"use_opengl_renderer":True, "media_dir":f"sync_notrace{LINE_NUM}","flush_cache":True,"progress_bar":'none'}

with tempconfig(cfg):
	scene = Plot()
	scene.render()