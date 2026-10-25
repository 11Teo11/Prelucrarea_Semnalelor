import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).parent

N = 8
F = np.zeros((N,N), dtype=complex)

for i in range(N):
    for j in range(N):
        F[i][j] = np.exp(-2j*np.pi*i*j/N)


fig, axs = plt.subplots(N,1, figsize=(8, 2*N), sharex=True, sharey=True)
fig.suptitle(f"Matricea Fourier pentru N = {N}")
for k in range(N):
    axs[k].plot(F[k].real, 'o-', label='Re')
    axs[k].plot(F[k].imag, 's--', label='Im')
    axs[k].set_ylabel(f'k = {k}')
    axs[k].legend(loc='upper right')
    axs[k].grid(True)

axs[-1].set_xlabel('n')
plt.tight_layout()

fig.savefig(BASE / 'fig_1.pdf')
plt.show()
plt.close(fig)

FhF = (1/N)*(F.conj().T @ F)

I = np.zeros((N,N), dtype=complex)
for i in range(N):
    I[i][i] = 1

print(np.allclose(FhF, I))
print('norma: ',np.linalg.norm(FhF - I))


