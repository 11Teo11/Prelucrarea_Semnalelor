import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).parent

f = 3
fs = 5000
t = np.arange(0, 1, 1/fs)

x = np.cos(2*np.pi*f*t)

def z(w):
    return np.exp(-2j*np.pi*w*t)*x


## a)
fig, axs = plt.subplots(1,2, figsize=(10,6))

## fig 1 stanga
axs[0].plot(t,x, color='green')
axs[0].grid(True)
axs[0].plot([-1,1.5], [0,0],color='black')
axs[0].set_xlim(0,1)
axs[0].set_ylim(-1.1, 1.1)
axs[0].set_xlabel('timp [s]')
axs[0].set_ylabel('x(t)')

## fig 2 dreapta colorat in functie de distanta fata de origine
axs[1].scatter(z(1).real, z(1).imag, s=5, c=np.abs(z(1)), cmap='tab20b', vmin=0, vmax=1)
# axs[1].plot(z(1).real, z(1).imag)
axs[1].grid(True)
axs[1].axhline(0, color='black')
axs[1].axvline(0, color='black')
axs[1].set_xlabel('Real')
axs[1].set_xlim(-1.1, 1.1)
axs[1].set_ylabel('Imaginar')
axs[1].set_ylim(-1.1, 1.1)

## cercul unitate
th = np.linspace(0, 2*np.pi, 300)
axs[1].plot(np.cos(th), np.sin(th), '--', color='gray')

## corespondenta dintre amplitudinea semnalului la un anumit moment de timp si distanta 
## de la originea cercului unitate la punctul [n, x[n]]
idx = int(0.62 * len(t))
axs[0].plot([t[idx],t[idx]], [x[idx],0], color='red')
axs[0].plot(t[idx], x[idx], 'o', color='red')
axs[1].plot([0, z(1)[idx].real], [0, z(1)[idx].imag], color='red')
axs[1].plot(z(1)[idx].real, z(1)[idx].imag, 'o', color='red')
axs[1].set_aspect('equal')

## media
axs[1].plot(np.mean(z(1).real), np.mean(z(1).imag),'o', markersize=7 ,color='black')

plt.tight_layout()
fig.savefig(BASE / 'fig_2_a.pdf')
plt.show()
plt.close(fig)

## b)
w = [[1,2],[f,7]]
fig, axs = plt.subplots(2,2, figsize=(10,9), sharex=True, sharey=True)
for i in range(len(axs)):
    for j in range(len(axs[i])):
        ax = axs[i][j]
        wi = w[i][j]
        zw = z(wi)
        ax.scatter(zw.real, zw.imag, s=5, c=np.abs(zw), cmap='RdYlGn', vmin=0, vmax=1)
        ax.plot(np.mean(zw.real), np.mean(zw.imag),'o', markersize=7 ,color='black')
        ax.plot([0,np.mean(zw.real)], [0,np.mean(zw.imag)],color='black', linewidth=3)
        if wi == f:
            ax.set_title(f'w = {wi} (= f)')
        else:
            ax.set_title(f'w = {wi}')
        ax.set_xlim(-1.1,1.1)
        ax.set_ylim(-1.1,1.1)
        ax.set_xlabel('Real')
        ax.set_ylabel('Imaginar')
        ax.plot([0,0], [-1.5,1.5],color='black')
        ax.plot([-1.5,1.5],[0,0],color='black')
        ax.plot(np.cos(th), np.sin(th), '--', color='gray')
        ax.grid(True)
        ax.set_aspect('equal')

plt.tight_layout()
fig.savefig(BASE / 'fig_2_b.pdf')
plt.show()
plt.close(fig)
