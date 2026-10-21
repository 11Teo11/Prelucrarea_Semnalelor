import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time

def sinus(t, f):
    return np.sin(2*np.pi*f*t)

fs = 16000
ts = 1/fs
T = 1
t = np.arange(0,T,ts)

f1 = 300
f2 = 600
x1 = sinus(t,f1)
x2 = sinus(t,f2)

x = np.concatenate([x1,x2])

sd.play((0.3*x).astype(np.float32), fs)
sd.wait()

## observatie: a 2a jumatate a sunetului este mai ascutita, dar la acelasi volum