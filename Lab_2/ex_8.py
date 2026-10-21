import numpy as np
import matplotlib.pyplot as plt

BASE = ''

t = np.linspace(-np.pi/2, np.pi/2, 1001)
s = np.sin(t)
aprx_taylor = t
aprx_pade =  (t - 7*(t**3)/60)/(1 + (t**2)/20)

fig, axs = plt.subplots(3,1, figsize=(10,7))
axs[0].plot(t, s, color='orange', label=r'$\sin(\alpha)$')
axs[0].plot(t, aprx_taylor, '--', color='red', label=r'$\alpha$ (Taylor)')
axs[0].plot(t, aprx_pade, ':', color='blue', linewidth=2, label='Pade')
axs[0].grid(True)
axs[0].legend()

eroare_taylor = np.abs(s - aprx_taylor)
eroare_pade = np.abs(s - aprx_pade)

axs[1].plot(t, eroare_taylor, color='red', label=r'$|\sin(\alpha)-\alpha|$')
axs[1].plot(t, eroare_pade, color='blue', label=r'$|\sin(\alpha) - Pade|$')
axs[1].set_title('Eroarea absoluta (scara liniara)')
axs[1].grid(True)
axs[1].legend()

eroare_taylor = np.where(eroare_taylor > 0, eroare_taylor, np.nan)
eroare_pade   = np.where(eroare_pade > 0, eroare_pade, np.nan)

axs[2].plot(t, eroare_taylor, color='red', label='Taylor')
axs[2].plot(t, eroare_pade, color='blue', label='Padé')
axs[2].set_title('Eroarea absolută (scară logaritmică)')
axs[2].set_yscale('log')
axs[2].grid(True)
axs[2].set_ylim(1e-17,1)
axs[2].legend()

fig.tight_layout()
fig.savefig(BASE + 'fig_8.pdf')
plt.show()
plt.close(fig)