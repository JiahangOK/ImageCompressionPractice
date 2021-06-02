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
color_arr = np.array([[83, 133, 236], [216, 80, 64], [88, 165, 92], [
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
dnn_bpp = [0.207275391, 0.273763021, 0.353881836, 0.472066243,
           0.698120117, 0.962687174, 1.216430664,	1.595967611, 2.029663086]
webp_bpp = [0.5716959635416666, 0.8172607421875, 1.0247395833333333, 1.1917724609375, 1.3519694010416667,
            1.5189615885416667, 1.6651204427083333, 2.0400390625]
jpeg_bpp = [0.4399617513020833, 0.70916748046875, 0.92279052734375, 1.0948689778645833, 1.2577921549479167,
            1.4360758463541667, 1.7090250651041667, 2.1482340494791665]
dnn_msssim = [0.948790865, 0.961786908, 0.972080157, 0.980415542,
              0.988137288, 0.9925368, 0.99480813,	0.996803014, 0.997964678]
webp_msssim = [0.9500408924076179, 0.966619007499018, 0.9749447649031916, 0.9796008752047053, 0.9832732525636337,
               0.9864496400303047, 0.9883668507304344, 0.9920620427367572]
jpeg_msssim = [0.9174701424096905, 0.9561016178436144, 0.9720340111662615, 0.9780115806283137, 0.982222849569216,
               0.985614579186816, 0.989011731991468, 0.9922698461363977]


dnn_msssim = list(-10*np.log10(np.ones(9)-dnn_msssim))
webp_msssim = list(-10*np.log10(np.ones(8)-webp_msssim))
jpeg_msssim = list(-10*np.log10(np.ones(8)-jpeg_msssim))

# draw
_, ax = plt.subplots(1, 1, figsize=(15, 5))
ax.xaxis.grid(True, linestyle='--', color='gray', lw=1.)
ax.yaxis.grid(True, linestyle='--', color='gray', lw=1.)
l1 = ax.plot(jpeg_bpp, jpeg_msssim,
             color=color_arr[0], marker='o', markersize=8, markeredgewidth=2, linewidth=2, markerfacecolor='white', label='JPEG')
l2 = ax.plot(dnn_bpp, dnn_msssim,
             color=color_arr[1], marker='D', markersize=8, markeredgewidth=2, linewidth=2, markerfacecolor='white', label='DNN')
l3 = ax.plot(webp_bpp, webp_msssim,
             color=color_arr[2], marker='^', markersize=8, markerfacecolor='white', markeredgewidth=2, linewidth=2, label='WEBP')
ax.set_xlabel('bpp')
ax.set_ylabel('MS-SSIM')

ax.legend()
plt.savefig('exp3_msssim.png')
