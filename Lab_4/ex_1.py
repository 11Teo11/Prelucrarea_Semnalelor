import numpy as np
import matplotlib.pyplot as plt
import time
from pathlib import Path

BASE = Path(__file__).parent

N = [128, 256, 512, 1024, 2048, 4096, 8192]

def dft(N,x):
    n = np.arange(N)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        X[k] = np.sum(x * np.exp(-2j * np.pi * k*n/N))

    return X


def fft(N,x):
    if N == 1:
        return x

    par = fft(N//2, x[0::2])
    impar = fft(N//2, x[1::2])

    w = np.exp(-2j * np.pi * np.arange(N//2)/N)

    return np.concatenate((par + w*impar, par - w*impar))

t_dft = []
t_fft = []
t_np = []

f = 3

dft(8, np.zeros(8))
fft(8, np.zeros(8))
np.fft.fft(np.zeros(8))

for n in N:
    t = np.arange(n) / n
    x = np.cos(2*np.pi*f*t)

    start = time.perf_counter()
    X_dft = dft(n,x)
    t_dft.append(time.perf_counter() - start)

    start = time.perf_counter()
    X_fft = fft(n,x)
    t_fft.append(time.perf_counter() - start)

    start = time.perf_counter()
    X_np = np.fft.fft(x)
    t_np.append(time.perf_counter() - start)

    print(f'N={n:5d}  '
    f'DFT={t_dft[-1]:.4f}s  '
    f'FFT={t_fft[-1]:.4f}s  '
    f'numpy={t_np[-1]:.6f}s')

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(N, t_dft, 'o-', label='DFT implementată')
ax.plot(N, t_fft, 'o-', label='FFT implementată')
ax.plot(N, t_np, 'o-', label='numpy.fft')

ax.set_xscale('log', base=2)
ax.set_yscale('log')
ax.set_xticks(N)
ax.set_xticklabels([str(n) for n in N])
ax.set_xlabel('N')
ax.set_ylabel('timp de execuție [s]')
ax.set_title('DFT vs FFT vs numpy.fft')
ax.grid(True, which='both', ls='--', alpha=0.5)
ax.legend()

fig.tight_layout()
fig.savefig(BASE / 'fig_1.pdf')
plt.show()

