import numpy as np
import matplotlib.pyplot as plt
import csv
from pathlib import Path

BASE = Path(__file__).parent

## a)
# observam in Train.csv ca avem valori din ora in ora 
# o ora = 3600 secunde
# => fs = 1/3600 Hz

## b)
# primul esantion  -> 25-08-2012 00:00
# ultimul esantion -> 25-09-2014 23:00
# interval de timp = 18288 ore
# (sunt 18288 de esantioane la diferenta de o ora unul de altul)


## c)
# fs/2 = 1/7200 Hz -> perioada minima de 2 ore


## d)

x = np.genfromtxt('archive/Train.csv', delimiter=',', skip_header=1, usecols=2)

fs = 1/3600
N = len(x)
X = np.fft.fft(x)
X = abs(X / N)
X = X[:N//2]
f = fs*np.linspace(0,N//2,N//2)/N
# f = np.arange(N//2) * fs / N # (fara capatul din dreapta)

fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(f, X)
ax.set_xlabel('frecventa [Hz]')
ax.set_ylabel('|X(w)|')
ax.set_title('Modulul transformatei Fourier')
ax.grid(True, alpha=0.4)

fig.tight_layout()
fig.savefig(BASE / 'fig_1_d.pdf')
plt.show()


## e)

fs = 1/3600
x2 = x - np.mean(x)
X2 = np.fft.fft(x2)
X2 = abs(X2 / N)
X2 = X2[:N//2]
f = fs*np.linspace(0,N//2,N//2)/N
# f = np.arange(N//2) * fs / N # (fara capatul din dreapta)

fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(f, X2)
ax.set_xlabel('frecventa [Hz]')
ax.set_ylabel('|X(w)|')
ax.set_title('Modulul transformatei Fourier fara componenta continua')
ax.grid(True, alpha=0.4)

fig.tight_layout()
fig.savefig(BASE / 'fig_1_e.pdf')
plt.show()


## f)
cresc = np.argsort(X2)
desc = cresc[::-1]
indici_max = desc[:5]
valori_max = np.round(X2[indici_max],2)
frecvente_max = indici_max * fs / N
perioade = 1/frecvente_max
print("Cele mai mari valori:      ",valori_max)
print("Indicii frecventelor maxime",indici_max)
print("Frecventele maxime:        ",frecvente_max)
print("Perioadele in secunde:     ",perioade)
print("Perioadele in ore:         ",perioade/3600)
print("Perioadele in zile:        ",perioade/3600/24)

# rezultate: 
# 1. 762 de zile -> toata inregistrarea               -> tendinta de crestere
# 2. 381 de zile -> 1/2 din inregistrare              -> tendinta de crestere
# 3. 1 zi        -> perioada de o zi din inregistrare -> se repeta in fiecare zi
# 4. 254 de zile -> 1/3 din inregistrare              -> tendinta de crestere
# 5. 7 zile      -> o saptamana                       -> se repeta in fiecare saptamana


## g)
# primul esantion -> 25-08-2012 00:00 -> o zi de sambata
# => primul esantion intr-o zi de luni este la 27-08-2012 00:00 
# -> esantionul cu numarul 48
# o saptamana are 7*24 = 168 de ore 
# => prima zi de luni de la un esantion > 1000 este la al 1056-lea esantion
# -> 08-10-2012 00:00

# o luna ~ 30 zile = 720 de ore -> 720 de esantioane 

luna = 30 * 24
start = 1056



x_luna = x[start: start+luna]

t = np.arange(len(x_luna)) / 24

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(t, x_luna)
ax.set_xlabel('zile')
ax.set_ylabel('numar masini')
ax.set_title('O luna de trafic (incepand de luni, 08-10-2012)')
ax.grid(True, alpha=0.4)
ax.set_xticks(np.arange(0, 31, 1))
ax.tick_params(axis='x', labelsize=8)

fig.tight_layout()
fig.savefig(BASE / 'fig_1_g.pdf')
plt.show()


## h)
### Metoda de obtinere a zilei in care s-a inceput masurarea semnalului:

## putem sa grupam esantioanele ( care sunt de cate o ora ) pe faze ale ciclului de 24 de ore = o zi ( avand perioada de o zi gasita la punctul f)
## astfel obtinem profilul zilnic mediu -> cu minime noaptea si maxime dupa amiaza - seara
## -> obtinem la ce ora a zilei a inceput masurarea semnalului

## apoi grupam esantioanele pe faze ale ciclului de 168 de ore = o saptamana (tot gasita la punctul f)
## astfel obtinem profilul saptamanal mediu -> 5 zile trafic mare si 2 zile consecutive ( weekend ) mai mic
## -> obtinem in ce zi a saptamanii a inceput masurarea 

## pentru a obtine data efectiva am putea cauta o bucata specifica din semnal ce reprezinta o sarbatoare fixa (probabil cu un trafic mai mic)
## iar apoi sa vedem diferenta de esantioane (ore) dintre aceasta si inceputul masurarii semnalului pentru a obtine data exacta
## ex: 25 decembrie, desi cade intr-o zi lucratoare, are trafic asemanator cu weekendul
## ziua saptamanii unei date fixe difera de la an la an => sarbatoarea poate fixa si anul in care a inceput inregistrarea 

## de asemenea, cunoscand lungimea semnalului putem vedea exact cate zile au fost inregistrate pentru o comparare intre ani, in cazul in care avem un an bisect ( in acelasi stil, cu sarbatoarea )
## astfel numarul de zile ar creste cu 1 -> de luat in considerare cand calculam diferenta de ore 
## trebuie luata in considerare si posibila schimbare de ora , avand in acele 2 zile specifice o ora in plus, respectiv in minus, de esantionare


### Neajunsurile metodei:
## periodicitatea ne poate da doar faza relativa, nu exact ziua si ora
## din profilul de 24 de ore stim unde este minimul dar nu ce ora reprezinta acesta, iar, la fel pentru profilul de o saptamana, stim ca sunt 2 zile cu mai putin trafic, dar presupunem ca acestea sunt in weekend


## in cazul in care traficul nu se schimba intr-un mod evident pentru o zi de sarbatoare nu putem obtine data, neavand un reper

## tendinta de crestere poate depasi diferentele de sezon ( vara iarna ) astfel nu putem obtine luna exacta

## zgomot si valori atipice ( varfuri izolate ) ne deformeaza mediile -> nu obtinem profilele potrivite

## sarbatorile pot arata ca un weekend ( ex 2 zile libere in mijlocul saptamanii ) 


## i)

## pastram doar componentele cu perioada >= 6 ore
## dispare zgomotul si varfurile izolate, ciclul zilnic ramane intact

N = len(x)

k = np.arange(N)
f = k * fs / N

f[f > fs/2] = fs - f[f > fs/2]
f_taiere = 1 / (12 * 3600)

X = np.fft.fft(x)
X[f > f_taiere] = 0

x_neted = np.real(np.fft.ifft(X))



start = 1056
stop = start + 30 * 24
t = np.arange(stop - start) / 24

fig, ax = plt.subplots(2, figsize=(12, 7))

ax[0].plot(t, x[start:stop], color='gold', label='semnal brut', alpha=0.8)
ax[0].plot(t, x_neted[start:stop], color='r', lw=1.5, label='semnal filtrat')
ax[0].set_title('30 zile de trafic: brut vs filtrat')
ax[0].set_xlabel('zile')
ax[0].set_ylabel('numar masini')
ax[0].legend()
ax[0].grid(True, alpha=0.4)

t2 = np.arange(N) / 24

ax[1].plot(t2, x, color='gold', label='semnal brut', alpha=0.5, lw=0.7)
ax[1].plot(t2, x_neted, color='r', lw=1, label='semnal filtrat')
ax[1].set_title('Tot semnalul: 762 de zile')
ax[1].set_xlabel('zile')
ax[1].set_ylabel('numar masini')
ax[1].legend()
ax[1].grid(True, alpha=0.4)

fig.tight_layout()
fig.savefig(BASE / 'fig_1_i.pdf')
plt.show()
