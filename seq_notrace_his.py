import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap
for filename in os.listdir('data'):
	if filename!='.DS_Store':
		purename=re.split('\.',filename)[0]
		f = os.path.join('data', filename)
		# print(filename)
		with open(f,'rb') as fo:
			data0=pd.read_parquet(fo,engine="fastparquet")
		data0.fillna(9999,inplace=True)
		delay=data0.groupby('cdn')['ttfb_ms'].apply(list).to_dict()
		timestamp=data0.groupby('cdn')['start_time_ms'].apply(list).to_dict()
		
		city_num=len(delay.keys())
		fig=plt.figure()
		cfg_list=[]
		cfgl_list=[]
		data_pair_list=[]
		cmap = plt.get_cmap('tab10')
		it=0
		for city, late in delay.items():
			color = cmap(it)
			cfg, = plt.plot([], [], color=color,marker='o')
			cfgl, = plt.plot([], [], color=color)
			cfg_list.append(cfg)
			cfgl_list.append(cfgl)
			time = timestamp[city]
			time = list((np.array(time)-time[0])/1000)
			# plt.plot(time,late)
			data_pair_list.append((time, late))
			it += 1

		writer = anime.PillowWriter(fps=50)
		with writer.saving(fig, os.path.join('res/seq_notrace_his', purename+'.gif'), 100):
			plt.xlim(0, data_pair_list[0][0][100])
			plt.ylim(200, 400)
			plt.title("Latency over Time")
			plt.xlabel('Timestamp (s)')
			plt.ylabel('Latency (ms)')
			
			for i in range(len(cfg_list)):
				for j in range(0,100):
					cfg_list[i].set_data(data_pair_list[i][0][j],data_pair_list[i][1][j])
					writer.grab_frame()
				cfgl_list[i].set_data(data_pair_list[i][0][:100],data_pair_list[i][1][:100])
				writer.grab_frame()
			# cfgl_list[i].set_data([],[])
			for _ in range(10):
				writer.grab_frame()