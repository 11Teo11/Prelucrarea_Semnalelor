import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).parent

fs = 6

f1 = 8
f2 = np.abs(f1 - fs)
f3 = np.abs(f1 - 2*fs)

T = 1
t = np.linspace(0, T, 2000)
ts = np.arange(0, T, 1/fs)

x1 = np.cos(2*np.pi*f1*t)
x2 = np.cos(2*np.pi*f2*t)
x3 = np.cos(2*np.pi*f3*t)

xs1 = np.cos(2*np.pi*f1*ts)
xs2 = np.cos(2*np.pi*f2*ts)
xs3 = np.cos(2*np.pi*f3*ts)


fig, ax = plt.subplots(3,1,figsize=(10, 7), sharex=True, sharey=True)

ax[0].plot(t, x1, color='tab:blue', label=f'original: {f1} Hz')
ax[1].plot(t, x2, color='tab:red', label=f'alias: {f2} Hz')
ax[2].plot(t, x3, color='tab:green', label=f'alias: {f3} Hz')

ax[0].plot(ts, xs1, 'o', color='gold', markeredgecolor='black', markersize=7, zorder=5)
ax[1].plot(ts, xs2, 'o', color='gold', markeredgecolor='black', markersize=7, zorder=5)
ax[2].plot(ts, xs3, 'o', color='gold', markeredgecolor='black', markersize=7, zorder=5, label='esantioane comune')

ax[2].set_xlim(0, T)
ax[2].set_ylim(-1.2, 1.2)
ax[2].set_xlabel('timp [s]')
ax[2].set_ylabel('x(t)')
ax[0].grid(True, alpha=0.4)

ax[1].set_xlim(0, T)
ax[1].set_ylim(-1.2, 1.2)
ax[1].grid(True, alpha=0.4)

ax[2].set_xlim(0, T)
ax[2].set_ylim(-1.2, 1.2)
ax[2].grid(True, alpha=0.4)
plt.suptitle(f'Aliasing: f = {f1} Hz, fs = {fs} Hz, '
             f'Nyquist = {fs/2} Hz')
fig.legend(loc='upper right')

fig.tight_layout()
fig.savefig(BASE / 'fig_2.pdf')
plt.show()