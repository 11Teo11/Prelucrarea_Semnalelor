# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:35:07 2026

@author: Teodor Vasile
"""
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile


BASE = ''

def sinus(t,f):
    return np.sin(2*np.pi*f*t)

def sawtooth(t,f):
    return 2*(t*f - np.floor(t*f)) - 1

fs = 2000
T = 0.1
ts = 1/fs
t = np.arange(0,T,ts)

f_sin = 50
f_saw = 30

x1 = sinus(t, f_sin)
x2 = sawtooth(t, f_saw)

y = x1+x2

fig, axs = plt.subplots(3,1, figsize=(10,8), sharex=True)

axs[0].grid(True)
axs[0].plot(t, x1, color='red')
axs[0].set_title(f'Sinus, f = {f_sin} Hz')

axs[1].grid(True)
axs[1].plot(t, x2, color='green')
axs[1].set_title(f'Sawtooth, f = {f_saw} Hz')

axs[2].grid(True)
axs[2].plot(t, y, color='blue')
axs[2].set_title('suma')

plt.tight_layout()
fig.savefig(BASE + 'fig_4.pdf')
plt.show()
plt.close(fig)


