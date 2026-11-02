import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.io import wavfile

BASE = Path(__file__).parent

## a)
fs , x = wavfile.read(BASE / 'vocale.wav')
# x = x/np.max(np.abs(x))
N = len(x)

## b)
frame_lg = int(0.01 * N)
pas = frame_lg//2
nr_frame = (N - frame_lg)//pas + 1

## c)
ffts = []

for i in range(0, N - frame_lg+1, pas):
    frame = x[i: i + frame_lg]
    frame = frame * np.hanning(frame_lg)
    X = np.fft.fft(frame)

    ffts.append(np.abs(X[:frame_lg //2 + 1]))

spect = np.array(ffts).T

## trecem la dB
spect_db = 20*np.log10(spect + 1e-12)
spect_db -= spect_db.max()

f_max = 10000
frecv = np.fft.rfftfreq(frame_lg, 1/fs)
mask = frecv <= f_max

fig, ax = plt.subplots(figsize=(12,5))

im = ax.imshow(
    spect_db[mask, :],
    origin='lower',
    aspect='auto',
    extent=[0, N / fs, 0, f_max],
    cmap='magma',
    vmin=-80,
    vmax=0
)

ax.set_xlabel('timp [s]')
ax.set_ylabel('frecventa [Hz]')
ax.set_title('Spectrograma vocalelor')

fig.colorbar(im, ax=ax, label='putere [dB]')

fig.tight_layout()
fig.savefig(BASE / 'fig_6.pdf')

plt.show()


