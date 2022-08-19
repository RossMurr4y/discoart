from easing_functions import *
import numpy as np
import matplotlib.pyplot
import io
import sys
import json

def easing_normalize(arr, t_min, t_max):
    norm_arr = []
    for i in arr:
        norm_arr.append((((i - min(arr))*(t_max - t_min))/(max(arr) - min(arr))) + t_min)
    return norm_arr

def dd_easing_int(start=1, end=9, steps=1000, easing_fn="ExponentialEaseInOut"): return list(np.rint(easing_normalize(list(map(eval(easing_fn + "(start=start, end=end, duration=steps)"), np.arange(0, steps, 1))), min([start, end]), max([start, end]))).astype(int))
def easeint(st=1, en=9, s=1000, fn="ExponentialEaseInOut"): return dd_easing_int(start=st, end=en, steps=s, easing_fn=fn)
def dd_easing_float(start=1, end=9, steps=1000, easing_fn="ExponentialEaseInOut"): return list(easing_normalize(list(map(eval(easing_fn + "(start=start, end=end, duration=steps)"), np.arange(0, steps, 1))), min([start, end]), max([start, end])))
def easeflt(st=1, en=9, s=1000, fn="ExponentialEaseInOut"): return dd_easing_float(start=st, end=en, steps=s, easing_fn=fn)

def create_plot(title, path, cut_easing_fn, cut_overview, cut_innercut, cut_ic_pow):
    plt = matplotlib.pyplot
    plt.plot(np.arange(0, 1000, 1), eval(cut_overview), label='overview cuts')
    plt.plot(np.arange(0, 1000, 1), eval(cut_innercut), label='inner cuts')   

    total_cuts = []
    cut_overview_evaled = eval(cut_overview)
    cut_innercut_evaled = eval(cut_innercut)

    for i in np.arange(0, 1000, 1):
        total_cuts = total_cuts + [cut_overview_evaled[i] + cut_innercut_evaled[i]]

    f = io.BytesIO()
    plt.plot(np.arange(0, 1000, 1), total_cuts, label='total cuts')
    plt.plot(np.arange(0, 1000, 1), eval(cut_ic_pow), label='ic_pow')
    plt.legend(loc='best')
    plt.title(title)
    plt.savefig(path)
    print(f'Plot {name} saved to: {path}')

# open schedules.json
with open('./schedules.json') as f:
    data = json.load(f)
    
#cut_easing_fn = "CubicEaseInOut"
#cut_overview = "[23]*100+dd_easing_int(start=23, end=1, steps=800, easing_fn=cut_easing_fn)+[1]*100"
#cut_innercut = "[1]*100+dd_easing_int(start=1, end=23, steps=800, easing_fn=cut_easing_fn)+[23]*100"
#cut_ic_pow = "dd_easing_float(start=10, end=1, steps=1000, easing_fn=cut_easing_fn)"
#cut_icgray_p = "[0.6]*100+[0.2]*100+[0.1]*100+[0.05]*100+[0]*600"

for plot in data:
    name = plot['DisplayName']
    path = plot['Path']
    cut_easing_fn = plot['cut_easing_fn']
    cut_overview = plot['cut_overview']
    cut_innercut = plot['cut_innercut']
    cut_ic_pow = plot['cut_ic_pow']
    cut_icgray_p = plot['cut_icgray_p']
    create_plot(name, path, cut_easing_fn, cut_overview, cut_innercut, cut_ic_pow)
