import numpy as np
import matplotlib.pyplot as plt

BASE = ''

def sinus(t, f):
    return np.sin(2*np.pi*f*t)

fs = 1000
T = 0.05
ts = 1/fs
t = np.arange(0,T,ts)

f_a = fs/2
f_b = fs/4
f_c = 0

x_a = sinus(t,f_a)
x_b = sinus(t,f_b)
x_c = sinus(t,f_c)

fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

axs[0].plot(t, x_a)
axs[0].set_title(f'(a) f = fs/2 = {f_a:.0f} Hz')

axs[1].plot(t, x_b)
axs[1].set_title(f'(b) f = fs/4 = {f_b:.0f} Hz')

axs[2].plot(t, x_c)
axs[2].set_title(f'(c) f = 0 Hz')

plt.tight_layout()
fig.savefig(BASE + 'fig_6.pdf')
plt.show()
plt.close(fig)

## observatii: 
## pentru f = fs/2 x[n] = sin(pi*n) = 0 pentru orice n. valorile vor fi foarte aproape de 0 
## (pe plot observam scara de 1e-14 = foarte mica) dar nu exact 0 din cauza erorilor de rotunjire la reprezentarea in virgula mobila. 
## eroarea creste odata cu n
## pentru f = fs/4 x[n] = sin(pi*n/2) -> semnalul contine doar valorile 0, 1, 0, -1 -> in plot se unesc aceste puncte 
## pentru f = 0 toate valorile sunt in 0, plotul e o linie dreapta 