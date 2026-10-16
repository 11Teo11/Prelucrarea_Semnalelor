# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:31:43 2026

@author: Teodor Vasile
"""

import numpy as np
import matplotlib.pyplot as plt

# a)
def x(t):
    return np.sin(2*np.pi*400*t) 

fs = 16000
n = 1600
tn = np.arange(n)/fs

plt.plot(tn, x(tn))
plt.title('400 Hz 1600 esantioane')
plt.grid(True)
plt.savefig('fig_2_a.pdf')
plt.show()
plt.close()

# b)
t = 3
n = 100
tn = np.arange(n)/t
f = 800

def x(t,f):
    return np.sin(2*np.pi*f*t) 

plt.plot(tn, x(tn,f))
plt.title('800 Hz 3 secunde')
plt.grid(True)
plt.savefig('fig_2_b.pdf')
plt.show()
plt.close()

# c)


fs = 10000
t = 0.05   
tn = np.arange(0, t, 1/fs)
f = 240

def x(t,f):
    return 2*(t*f - np.floor(t*f)) - 1

plt.plot(tn, x(tn,f))
plt.title('sawtooth')
plt.grid(True)
plt.savefig('fig_2_c.pdf')
plt.show()
plt.close()

# d)

fs = 16000
f = 300
t = 3/f
tn = np.arange(0, t, 1/fs)

def x(t,f):
    return np.sign(np.sin(2*np.pi*f*t))

plt.plot(tn, x(tn,f))
plt.title('square')
plt.grid(True)
plt.savefig('fig_2_d.pdf')
plt.show()
plt.close()

# e)
im = np.random.rand(128,128)
plt.imshow(im)
plt.savefig('fig_2_e.pdf')
plt.show()
plt.close()

# f)
im = np.zeros((128, 128))
im[16:112, 16:112] = 1   
im[32:96, 32:96] = 0.75
im[48:80, 48:80] = 0.5
im[60:68, 60:68] = 0.25  

plt.imshow(im)
plt.savefig('fig_2_f.pdf')
plt.show()
plt.close()
