import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path

BASE = Path(__file__).parent

f = 3
fs = 5000
t = np.arange(0, 1, 1/fs)
x = np.cos(2*np.pi*f*t)
N = len(t)

STEP = 25       ## un cadru la fiecare 50 de esantioane
FPS = 25        ## viteza animatiei
th = np.linspace(0, 2*np.pi, 300)


def z(w):
    return x * np.exp(-2j*np.pi*w*t)


def cadre():
    ## indicii esantioanelor la care desenam un cadru
    frames = list(range(0, N, STEP))
    if frames[-1] != N - 1:
        frames.append(N - 1)
    return frames


## animatie fig 1
def anima_figura_a():
    zw = z(1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

    text1 = ax1.text(0.02, 0.98, '', transform=ax1.transAxes,
                 va='top', ha='left', fontsize=9, family='monospace',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    text2 = ax2.text(0.02, 0.98, '', transform=ax2.transAxes,
                 va='top', ha='left', fontsize=9, family='monospace',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ## semnalul complet in fundal
    ax1.plot(t, x, color='lightgray', linewidth=0.8)
    ax1.set_xlim(0, 1.)
    ax1.set_ylim(-1.1, 1.1)
    ax1.set_xlabel('timp [s]')
    ax1.set_ylabel('x(t)')
    ax1.grid(True)

    ## planul complex
    ax2.axhline(0, color='gray', lw=0.8)
    ax2.axvline(0, color='gray', lw=0.8)
    ax2.plot(np.cos(th), np.sin(th), '--', color='gray')
    ax2.set_aspect('equal')
    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(-1.1, 1.1)
    ax2.set_xlabel('Real')
    ax2.set_ylabel('Imaginar')
    ax2.grid(True)


    linie1, = ax1.plot([], [], color='green', lw=1.2)
    sc = ax2.scatter(zw.real[:1], zw.imag[:1], s=5, c=np.abs(zw[:1]), cmap='tab20b', vmin=0, vmax=1)
    traseu, = ax2.plot([], [], color='gray', lw=0.6, alpha=0.6)
    punct1, = ax1.plot([], [], 'o', color='red', ms=8, zorder=5)
    punct2, = ax2.plot([], [], 'o', color='red', ms=8, zorder=5)

    def update(i):
        text1.set_text(f't = {t[i]:.2f} s\nx = {x[i]:+.2f}')
        text2.set_text(f'Re = {zw[i].real:+.2f}\n'
               f'Im = {zw[i].imag:+.2f}\n'
               f'|z| = {abs(zw[i]):.2f}')
        linie1.set_data(t[:i + 1], x[:i + 1])
        punct1.set_data([t[i]], [x[i]])

        sc.set_offsets(np.column_stack([zw.real[:i + 1], zw.imag[:i + 1]]))
        sc.set_array(np.abs(zw[:i + 1]))
        traseu.set_data(zw.real[:i + 1], zw.imag[:i + 1])
        punct2.set_data([zw.real[i]], [zw.imag[i]])

        return linie1, punct1, sc, traseu, punct2, text1, text2

    anim = FuncAnimation(fig, update, frames=cadre(), interval=1000 / FPS, blit=False)
    anim.save(BASE / 'fig_2_a_animat.gif', writer='pillow', fps=FPS)
    plt.close(fig)



## animatie fig 2
def anima_figura_b():
    w = [[1, 2], [f, 7]]

    fig, axs = plt.subplots(2, 2, figsize=(10, 9), sharex=True, sharey=True)
    art = []

    for i in range(2):
        for j in range(2):
            ax = axs[i][j]
            wi = w[i][j]
            zw = z(wi)

            ax.axhline(0, color='gray', lw=0.8, zorder=0)
            ax.axvline(0, color='gray', lw=0.8, zorder=0)
            ax.plot(np.cos(th), np.sin(th), '--', color='gray', zorder=1)
            ax.set_aspect('equal')
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)
            ax.set_xlabel('Real')
            ax.set_ylabel('Imaginar')
            ax.grid(True)
            if wi == f:
                ax.set_title(f'w = {wi} (= f)')
            else:
                ax.set_title(f'w = {wi}')

            sc = ax.scatter(zw.real[:1], zw.imag[:1], s=5, c=np.abs(zw[:1]), cmap='RdYlGn', vmin=0, vmax=1, zorder=2)
            traseu, = ax.plot([], [], color='gray', lw=0.6, alpha=0.6, zorder=2)
            punct, = ax.plot([], [], 'o', color='red', ms=7, zorder=5)

            art.append((zw, sc, traseu, punct))

    def update(i):
        for zw, sc, traseu, punct in art:
            sc.set_offsets(np.column_stack([zw.real[:i + 1], zw.imag[:i + 1]]))
            sc.set_array(np.abs(zw[:i + 1]))
            traseu.set_data(zw.real[:i + 1], zw.imag[:i + 1])
            punct.set_data([zw.real[i]], [zw.imag[i]])

        return [artist for a in art for artist in a[1:]]

    anim = FuncAnimation(fig, update, frames=cadre(), interval=1000 / FPS, blit=False)
    anim.save(BASE / 'fig_2_b_animat.gif', writer='pillow', fps=FPS)
    plt.close(fig)


anima_figura_a()
anima_figura_b()