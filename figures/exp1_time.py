# -*- coding:utf-8 -*-
from matplotlib.pylab import *
import numpy as np
import scipy.io as sio
import matplotlib as mpl
import matplotlib.ticker as ticker

# 全局参数设置
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
matplotlib.rcParams['font.serif'] = ['Times New Roman']
# plt.rc('xtick', labelsize='x-small')
# plt.rc('ytick', labelsize='x-small')
csfont = {'fontname': 'Comic Sans MS'}
hfont = {'fontname': 'Helvetica'}
tfont = {'fontname': 'Times New Roman'}
color_arr = np.array([[83, 133, 236], [216, 80, 64], [77, 175, 74], [
                     152, 78, 163], [255, 127, 0], [27, 158, 119]])
color_arr = color_arr * 1.0 / 255
color_arr = color_arr.tolist()
hatches = ['///', '+++', 'xxx', '\\\\\\', '---', 'xxx']
params = {
    'axes.labelsize': 8,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'text.usetex': False,
    'axes.labelsize': 12,
    'figure.figsize': [4.5, 3]
}
rcParams.update(params)


# data
webp_bpp = [0.8172607421875, 1.0247395833333333, 1.1917724609375, 1.3519694010416667,
            1.5189615885416667, 1.6651204427083333, 2.0400390625, 2.9042154947916665, 3.6994222005208335]
jpeg_bpp = [0.70916748046875, 0.92279052734375, 1.0948689778645833, 1.2577921549479167,
            1.4360758463541667, 1.7090250651041667, 2.1482340494791665, 3.1559244791666665, 4.403177897135417]
webp_time = [0.008872509002685547, 0.009596824645996094, 0.010564327239990234, 0.011977434158325195,
             0.012280464172363281, 0.01323080062866211, 0.014484882354736328, 0.019852876663208008, 0.022947072982788086]
jpeg_time = [0.007439136505126953, 0.008527278900146484, 0.00882577896118164, 0.009124279022216797,
             0.009420633316040039, 0.010093212127685547, 0.01028585433959961, 0.012298583984375, 0.013383626937866211]

webp_time = list(-10*np.log10(np.ones(9)-webp_time))
jpeg_time = list(-10*np.log10(np.ones(9)-jpeg_time))
# draw
_, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.xaxis.grid(True, linestyle='--', color='gray', lw=1.)
ax.yaxis.grid(True, linestyle='--', color='gray', lw=1.)
l1 = ax.plot(jpeg_bpp, jpeg_time,
             color=color_arr[0], marker='o', markersize=8, markerfacecolor='white', markeredgewidth=2, linewidth=2, label='JPEG')
l2 = ax.plot(webp_bpp, webp_time,
             color=color_arr[1], marker='D', markersize=8, markerfacecolor='white', markeredgewidth=2, linewidth=2, label='WEBP')

ax.set_xlabel('bpp')
ax.set_ylabel('Encode Time(s)')

ax.legend()
plt.savefig('exp1_time.png')
