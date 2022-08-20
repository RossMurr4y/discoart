from easing_functions import *
import numpy as np
import matplotlib.pyplot as plt
import io
import sys
import json

easing_functions = ["LinearInOut", "QuadEaseInOut", "CubicEaseInOut", "QuarticEaseInOut", "QuinticEaseInOut", "SineEaseInOut", "CircularEaseInOut", "ExponentialEaseInOut", "ElasticEaseInOut", "BackEaseInOut", "BounceEaseInOut"]

def easing_normalize(arr, t_min, t_max):
    norm_arr = []
    for i in arr:
        norm_arr.append((((i - min(arr))*(t_max - t_min))/(max(arr) - min(arr))) + t_min)
    return norm_arr

def dd_easing_int(start=1, end=9, steps=1000, easing_fn="ExponentialEaseInOut"): return list(np.rint(easing_normalize(list(map(eval(easing_fn + "(start=start, end=end, duration=steps)"), np.arange(0, steps, 1))), min([start, end]), max([start, end]))).astype(int))
def easeint(st=1, en=9, s=1000, fn="ExponentialEaseInOut"): return dd_easing_int(start=st, end=en, steps=s, easing_fn=fn)
def dd_easing_float(start=1, end=9, steps=1000, easing_fn="ExponentialEaseInOut"): return list(easing_normalize(list(map(eval(easing_fn + "(start=start, end=end, duration=steps)"), np.arange(0, steps, 1))), min([start, end]), max([start, end])))
def easeflt(st=1, en=9, s=1000, fn="ExponentialEaseInOut"): return dd_easing_float(start=st, end=en, steps=s, easing_fn=fn)

def create_plot(title, path, cut_easing_fn, cut_overview, cut_innercut, cut_ic_pow, cut_icgray_p):
    
    # calculate total cuts
    total_cuts = []
    cut_overview_evaled = eval(cut_overview)
    cut_innercut_evaled = eval(cut_innercut)
    for i in np.arange(0, 1000, 1):
        total_cuts = total_cuts + [cut_overview_evaled[i] + cut_innercut_evaled[i]]

    # copy total_cuts & sort
    y_axis = total_cuts
    y_axis.sort()

    fig, host = plt.subplots()
    
    par1 = host.twinx()
    
    host.set_xlim(0, 1000)

    
    host.set_xlabel("")
    host.set_ylabel("Cuts Per Itteration")
    #par1.set_ylabel("Addl. Grayscale Cut %")

    host.plot(np.arange(0, 1000, 1), eval(cut_overview), label='overview cuts')
    host.plot(np.arange(0, 1000, 1), eval(cut_innercut), label='inner cuts')   
    host.plot(np.arange(0, 1000, 1), total_cuts, label='total cuts')
    host.plot(np.arange(0, 1000, 1), eval(cut_ic_pow), label='ic_pow')
    par1.plot(np.arange(0, 1000, 1), eval(cut_icgray_p), color=plt.cm.viridis(0), linestyle='dashed', label='icgray_p')
    
    host.spines['right'].set_position(('outward', 0))
    
    par1.spines['right'].set_position(('outward', 15))
    par1.spines['right'].set_visible(True)
    par1.yaxis.set_label_position('right')
    par1.yaxis.set_ticks_position('right')

    par1.yaxis.label.set_color(plt.cm.viridis(0))
    
    host.legend(bbox_to_anchor=(0., -0.02, 0.48, -1.02), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    #par1.legend(bbox_to_anchor=(0.52, 1.02, 0.48, 1.02,), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    
    # set title based on cut_easing_fn
    if cut_easing_fn != "":
        plt.title(f'[{cut_easing_fn}] {title}')
    else:
        plt.title(title)
        
    plt.savefig(path)
    print(f'Plot {name} saved to: {path}')
    # clear current plot
    plt.clf()



# open schedules.json
with open(sys.argv[1]) as f:
    data = json.load(f)

for plot in data:
    name = plot['DisplayName']
    path = plot['Path']
    cut_easing_fn = plot['cut_easing_fn']
    cut_overview = plot['cut_overview']
    cut_innercut = plot['cut_innercut']
    cut_ic_pow = plot['cut_ic_pow']
    cut_icgray_p = plot['cut_icgray_p']
    create_plot(name, path, cut_easing_fn, cut_overview, cut_innercut, cut_ic_pow, cut_icgray_p)
