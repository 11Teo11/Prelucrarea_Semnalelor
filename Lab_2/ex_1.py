# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:14:27 2026

@author: Teodor Vasile
"""

import numpy as np
import matplotlib.pyplot as plt

BASE = ''

f = 120
A = 1
p = np.pi/3
fs = 2000
ts = 1/fs
T = 0.1
t = np.arange(0,T,ts)

x_sin = A*np.sin(2*np.pi*f*t + p)
x_cos = A*np.cos(2*np.pi*f*t + p - np.pi/2)

fig, axs = plt.subplots(2, figsize=(10,7))
axs[0].grid(True)
axs[0].plot(t, x_sin, color='red')
axs[0].set_title(r'$x = \sin(240\pi t + \pi/3)$')

axs[1].grid(True)
axs[1].plot(t, x_cos, color='green')
axs[1].set_title(r'$y = \cos(240\pi t + \pi/3 - \pi/2)$')

fig.savefig(BASE + 'fig_1.pdf')
plt.show()
plt.close(fig)
