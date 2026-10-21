# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:41:31 2026

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
T = 0.03
t = np.arange(0,T,ts)
faze = [np.pi/2, np.pi/4, 2*np.pi/3, np.pi]
faze_n = [r'\pi/2', r'\pi/4', r'2\pi/3', r'\pi']
culori = ['red', 'green', 'blue', 'orange']

# a)
def s_sin(faza):
    return A*np.sin(2*np.pi*f*t + faza)


fig, ax = plt.subplots(figsize=(10,3))
for i in range(len(faze)):
    ax.plot(t,s_sin(faze[i]), color=culori[i], label=rf'$x = \sin(240\pi t + {faze_n[i]})$')
ax.grid(True)
fig.legend()
fig.tight_layout()
fig.savefig(BASE + 'fig_2_a.pdf')
plt.show()
plt.close(fig)

# b)
T = 0.1
t = np.arange(0,T,ts)
x = s_sin(faze[0])
z = np.random.normal(0,1, len(x))

snr = [0.1, 1, 10, 100]

fig, axs = plt.subplots(4, figsize=(10,7))

for i in range(len(snr)):
    gamma = np.sqrt((np.linalg.norm(x)**2)/(snr[i]*(np.linalg.norm(z)**2)))
    y = x + gamma * z
    axs[i].plot(t, x, color='gray', label='original')
    axs[i].plot(t, y, color='red', label=f'SNR = {snr[i]}')
    axs[i].grid(True)
    axs[i].legend(loc = 'upper right')
    
fig.tight_layout()
fig.savefig(BASE + 'fig_2_b.pdf')
plt.show()
plt.close(fig)