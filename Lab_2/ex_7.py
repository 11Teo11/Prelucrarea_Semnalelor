import numpy as np
import matplotlib.pyplot as plt

BASE = ''

def sinus(t, f):
    return np.sin(2*np.pi*f*t)

f = 50
T = 0.05

fs = 1000
ts = 1/fs
t = np.arange(0,T,ts)
x = sinus(t,f)

fs_nou = fs/4
t_nou = t[::4]
x_nou = x[::4]

## a)
fig, axs = plt.subplots(2,1, figsize=(10,6), sharex=True)
axs[0].plot(t, sinus(t,f))
axs[0].grid(True)
axs[0].set_title(f'Semnal original, fs = {fs} Hz ({len(x)} esantioane)')
axs[1].plot(t_nou, x_nou, '.-')
axs[1].grid(True)
axs[1].set_title(f'Semnal decimat la 1/4, fs = {fs_nou:.0f} Hz ({len(x_nou)} esantioane)')

plt.tight_layout()
fig.savefig(BASE + 'fig_7_a.pdf')
plt.show()
plt.close(fig)

## semnalul decimat pastreaza frecventa, amplitudinea si faza semnalului original dar are de 4 ori mai putine esantioane, iar noua 
## frecventa de esantionare va fi 1000/4 = 250 Hz -> destul de mare incat sa nu se piarda informatie
## dar al 2lea semnal va avea linii mai drepte, fata de primul care e mai curbat (neted)

## b)
x_nou_b = x[1::4]
t_nou_b = t[1::4]

fig, ax = plt.subplots(figsize=(10, 5))
ax.grid(True)
ax.plot(t, x, color='gray', alpha=0.5, label='original')
ax.plot(t_nou, x_nou, 'o-', color='blue', label='x[::4] (de la index 0)')
ax.plot(t_nou_b, x_nou_b, 's--', color='orange', label='x[1::4] (de la index 1)')
ax.legend()

plt.tight_layout()
fig.savefig(BASE + 'fig_7_b.pdf')
plt.show()
plt.close(fig)

## pornind de la al 2lea element din vector esantioanele sunt luate cu 1ms mai tarziu
## e acelasi semnal, cu aceeasi amplitudine si frecventa dar defazat