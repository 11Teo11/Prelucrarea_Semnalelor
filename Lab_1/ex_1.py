# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:45:04 2026

@author: Teodor Vasile
"""

import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.cos(520*np.pi*t + np.pi/3) 

def y(t):
    return np.cos(280*np.pi*t - np.pi/3) 

def z(t):
    return np.cos(120*np.pi*t + np.pi/3)


## a)
t = np.arange(0, 0.03, 0.0001)

## b)
fig, axs = plt.subplots(3, figsize=(10,7))
axs[0].grid(True)
axs[0].plot(t, x(t), color='red')
axs[0].set_title(r'$x = \cos(520\pi t + \pi/3)$')

axs[1].grid(True)
axs[1].plot(t, y(t), color='green')
axs[1].set_title(r'$y = \cos(280\pi t - \pi/3)$')

axs[2].grid(True)
axs[2].plot(t, z(t), color='orange')
axs[2].set_title(r'$z = \cos(120\pi t + \pi/3)$')

plt.tight_layout()

fig.savefig('fig_1_b.pdf')
plt.show()
plt.close(fig)


## c)
fs = 200
ts = 1/fs
tn = np.arange(0, 0.03 + ts, ts)

fig, axs = plt.subplots(3, figsize=(10,7))
axs[0].grid(True)
axs[0].stem(tn, x(tn))
axs[0].set_title(r'$x[n]$')

axs[1].grid(True)
axs[1].stem(tn, y(tn))
axs[1].set_title(r'$y[n]$')

axs[2].grid(True)
axs[2].stem(tn, z(tn))
axs[2].set_title(r'$z[n]$')

plt.tight_layout()

fig.savefig('fig_1_c.pdf')
plt.show()
plt.close(fig)
