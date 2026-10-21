# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:47:14 2026

@author: Teodor Vasile
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile
import time

BASE = ''


def sinus(t,f):
    return np.sin(2*np.pi*f*t)

def sawtooth(t,f):
    return 2*(t*f - np.floor(t*f)) - 1

def square(t, f):
    return np.sign(np.sin(2*np.pi*f*t))

f_a = 400
fs_a = 16000
ts_a = 1/fs_a
T_a = 1
t_a = np.arange(0,T_a,ts_a)
x_a = sinus(t_a,f_a)

f_b = 800
fs_b = 8000
ts_b = 1/fs_b
T_b = 3
t_b = np.arange(0,T_b,ts_b)
x_b = sinus(t_b, f_b)


f_c = 240
fs_c = 10000
ts_c = 1/fs_c
T_c = 1
t_c = np.arange(0,T_c,ts_c)
x_c = sawtooth(t_c, f_c)


f_d = 300
fs_d = 16000
ts_d = 1/fs_d
T_d = 1
t_d = np.arange(0,T_d,ts_d)
x_d = square(t_d, f_d)


semnale = [('2(a) sin 400 Hz     ', x_a, fs_a),
           ('2(b) sin 800 Hz     ', x_b, fs_b),
           ('2(c) sawtooth 240 Hz', x_c, fs_c),
           ('2(d) square 300 Hz  ', x_d, fs_d)]


for n,s,fs in semnale:
    print(f'{n} | fs = {fs} Hz | durata = {len(s)/fs:.3f} s')
    sd.play((0.3*s).astype(np.float32), fs)
    sd.wait()
    time.sleep(0.3) 

wavfile.write(BASE + 'semnal_sinus_400hz.wav', int(fs_a), np.round(x_a*32767).astype(np.int16))

fs, x = wavfile.read(BASE + 'semnal_sinus_400hz.wav')
x = x/32768.0

sd.play((0.3*x).astype(np.float32), fs)
sd.wait()



