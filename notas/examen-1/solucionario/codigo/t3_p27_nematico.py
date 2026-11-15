"""Problema 27: nemático torcido 90° por matrices de Jones (Saleh §6.5, ec. 6.5-6).

Celda de espesor d dividida en N = 200 capas; capa m = retardador con eje lento (eje óptico)
a theta_m = m*alpha*dz.  Torsión total alpha*d = pi/2.  Entrada LP en x.
Se grafica la fracción de potencia que sale LP en y contra beta/alpha y se compara con
Gooch-Tarry: 1 - sin^2((pi/2) sqrt(1+u^2)) / (1+u^2), u = beta d / pi.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

N = 200
alpha_d = np.pi / 2                         # torsión total


def R(t):
    """Cambio de coordenadas (6.1-22)."""
    return np.array([[np.cos(t), np.sin(t)], [-np.sin(t), np.cos(t)]])


def fraccion_y(beta_sobre_alpha):
    beta_d = beta_sobre_alpha * alpha_d     # beta d = (beta/alpha)(alpha d)
    dz = 1.0 / N                            # en unidades de d
    Tr = np.diag([np.exp(-1j * beta_d * dz / 2), np.exp(1j * beta_d * dz / 2)])   # (6.5-5)
    T = np.eye(2, dtype=complex)
    for m in range(1, N + 1):               # producto (6.5-6): la capa 1 actúa primero
        th = m * alpha_d * dz
        T = R(-th) @ Tr @ R(th) @ T         # (6.5-3)
    Eout = T @ np.array([1.0, 0.0])
    return abs(Eout[1])**2 / np.sum(abs(Eout)**2)


def gooch_tarry(u):
    return 1 - np.sin(np.pi / 2 * np.sqrt(1 + u**2))**2 / (1 + u**2)


ba = np.logspace(-1, np.log10(50), 400)
num = np.array([fraccion_y(b) for b in ba])
u = ba * alpha_d / np.pi                     # u = beta d/pi = (beta/alpha)/2
gt = gooch_tarry(u)
print(f"max |Jones(N=200) - Gooch-Tarry| = {np.max(abs(num - gt)):.2e}")
for uu in (0.05, 0.5, 1.0, np.sqrt(3), np.sqrt(15), 10, 25):
    b = 2 * uu
    print(f"u = {uu:6.3f} (beta/alpha = {b:6.3f}): Jones = {fraccion_y(b):.4f}, "
          f"Gooch-Tarry = {gooch_tarry(uu):.4f}")

fig, ax = plt.subplots(figsize=(6.4, 4))
ax.semilogx(ba, num, 'C0', lw=2, label='Jones, $N=200$ capas (6.5-6)')
ax.semilogx(ba, gt, 'k--', lw=1, label='Gooch–Tarry')
for k, nombre in ((1, r'$u=\sqrt{3}$'), (2, r'$\sqrt{15}$'), (3, r'$\sqrt{35}$')):
    uu = np.sqrt((2 * k)**2 - 1)
    ax.axvline(2 * uu, color='0.6', ls=':', lw=1)
    ax.text(2 * uu, 0.05, nombre, rotation=90, fontsize=8, ha='right')
ax.set_xlabel(r'$\beta/\alpha$ (retardo por unidad de longitud / torsión)')
ax.set_ylabel(r'Fracción de potencia LP en $y$')
ax.set_title(r'Nemático torcido $90^\circ$, entrada LP en $x$')
ax.set_xlim(0.1, 50); ax.set_ylim(0, 1.05)
ax.legend(fontsize=8, loc='center right')
ax.grid(alpha=0.3, which='both')
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(base, f't3_p27_nematico.{ext}'), dpi=200)
print("figura guardada")
