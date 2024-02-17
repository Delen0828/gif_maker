from manim import *
import numpy as np
# import pandas as pd
import random
import pickle
SAMPLE_TIME=1
DURATION=100
SPIKE_H=10
config.background_color = WHITE
config["background_color"] = WHITE

def xList_create(duration):
	return list(range(0,duration,1))
def yList_create(avg,var,spike,spike_h,duration):
	baseline=np.ones(duration)*avg
	variation=np.random.random(duration)*var
	if spike is True:
		variation[np.random.randint(duration)]+=spike_h*var
	return baseline+variation
def sampler_line(high_data,low_data):
	return random.sample(high_data,1)[0],random.sample(high_data,1)[0]

def build_plot(axes, x, y, color):
	line = axes.plot_line_graph(x, y, add_vertex_dots=False, line_color=color)
	return VDict({"line": line})

class MyBeautifulGraph(Scene):
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
		self.load()
		AVG,AVG2=sampler_line(self.AVG_HIGH,self.AVG_LOW)
		VAR,VAR2=sampler_line(self.VAR_HIGH,self.VAR_LOW)
		SPIKE,SPIKE2=sampler_line([True],[False]) 
		y = yList_create(AVG,VAR,SPIKE,SPIKE_H,DURATION)
		y2 = yList_create(AVG2,VAR2,SPIKE2,SPIKE_H,DURATION)

		x = xList_create(DURATION)
		x_min, x_max, x_step = 0, DURATION, 10
		y_min, y_max, y_step = 200, 700, 100
		axes = Axes(
			x_range=[x_min, x_max + x_step, x_step],
			y_range=[y_min, y_max + y_step, y_step],
			tips=False,
			axis_config={'color': BLACK}
		)


		plot = build_plot(axes, x, y, color=RED)
		plot2 = build_plot(axes, x, y2, color=BLUE)
		self.add(axes)
		self.play(Create(plot["line"],run_time=6,rate_func=rate_functions.unit_interval(linear)))
		self.play(Create(plot2["line"],run_time=2,rate_func=rate_functions.unit_interval(linear)))
		self.wait()