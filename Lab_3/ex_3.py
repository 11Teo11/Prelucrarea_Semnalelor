
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).parent

fs = 1000
T = 1
N = int(fs * T)
ts = 1/fs
t = np.arange(0,T,ts)

def semnal(frecv):
    x = 0
    for a,f in frecv:
        x += a*np.cos(2*np.pi*f*t)
    
    return x

def z(w,x):
    return np.exp(-2j*np.pi*w*t)*x

frecv = [[1,5],[2,20],[0.5,75]]
x = semnal(frecv)

w = np.arange(1,max(f[1] for f in frecv)+10,1)

n = np.arange(N)
W = np.exp(-2j*np.pi* np.outer(w,n) / N)
X = W @ x

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(t, x, color='green')
ax1.set_xlabel('timp [s]')
ax1.set_ylabel('x(t)')
text = ''
for i in range(len(frecv)):
    text += f'f{i} = {frecv[i][1]} Hz '
    if i < len(frecv) - 1:
        text += ' | '
ax1.set_title('Semnalul compus\n'+text)
ax1.grid(True)

ax2.plot(w, np.abs(X), color='mediumseagreen')
ax2.set_xlabel('w [Hz]')
ax2.set_ylabel('|X(w)|')
ax2.set_title('Modulul transformatei Fourier')
ax2.grid(True)

for _,f in frecv:
    ax2.axvline(f, color='red', ls='--', alpha=0.5)

fig.tight_layout()
fig.savefig(BASE / 'fig_3.pdf', bbox_inches='tight')
plt.show()

