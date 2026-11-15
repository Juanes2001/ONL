"""Problema 23: cristales uniaxiales (Saleh, Probs. 6.3-1, 6.3-3, 6.3-5; §6.3C-E).

(a) cuarzo: retardo máximo por mm y espesores de lambda/4 a 633 nm.
(b) doble refracción en cuarzo a 30°, eje óptico en el plano de incidencia y perpendicular
    a la onda incidente: direcciones de k y de los rayos.
(c) lámina de LiNbO3 de 1 cm con el eje a 45° de la normal: walk-off, desplazamiento, retardo.
"""
import os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

lam0 = 633e-9
k0 = 2 * np.pi / lam0


def n_e(theta, no, ne):
    """Índice extraordinario (6.3-15); theta = ángulo entre k y el eje óptico."""
    return 1 / np.sqrt(np.cos(theta)**2 / no**2 + np.sin(theta)**2 / ne**2)


# ---------------- (a) ----------------
no, ne = 1.544, 1.553
G = 2 * np.pi * (ne - no) / lam0           # rad/m, con k perpendicular al eje óptico
print(f"(a) Gamma/d = {G:.4e} rad/m = {G*1e-3:.2f} rad/mm = {G*1e-3/(2*np.pi):.2f} ondas/mm")
d1 = lam0 / (4 * (ne - no))
dL = lam0 / (ne - no)
print(f"    d(lambda/4) = {d1*1e6:.2f} µm; periodo (2pi) = {dL*1e6:.2f} µm")
print("    Gamma = pi/2 + 2pi m :", ", ".join(f"{(d1 + m*dL)*1e6:.1f}" for m in range(3)), "µm")
print("    Gamma = 3pi/2 + 2pi m:", ", ".join(f"{(3*d1 + m*dL)*1e6:.1f}" for m in range(3)), "µm")

# ---------------- (b) ----------------
th1 = np.radians(30.0)
c_hat = np.array([np.cos(th1), -np.sin(th1)])     # eje óptico (x' tangente, z' normal)
p_hat = np.array([np.sin(th1), np.cos(th1)])      # dirección incidente (perpendicular al eje)
tho = np.arcsin(np.sin(th1) / no)                 # (6.3-24)
print(f"\n(b) onda o: theta_o = {np.degrees(tho):.3f}° (rayo paralelo a k)")


def psi_de(t):
    """Ángulo entre k (a t de la normal) y el eje óptico."""
    k = np.array([np.sin(t), np.cos(t)])
    return np.arccos(np.clip(k @ c_hat, -1, 1))


f = lambda t: n_e(psi_de(t), no, ne) * np.sin(t) - np.sin(th1)     # (6.3-23)
the = brentq(f, np.radians(10), np.radians(25))
psi = psi_de(the)
ne_th = n_e(psi, no, ne)
k = ne_th * np.array([np.sin(the), np.cos(the)])
kc, kp = k @ c_hat, k @ p_hat
S = (kc / no**2) * c_hat + (kp / ne**2) * p_hat   # normal a la superficie k (6.3-21)
ths = np.arctan2(S[0], S[1])
print(f"    onda e: theta_e(k) = {np.degrees(the):.3f}°, ángulo k-eje = {np.degrees(psi):.2f}°, "
      f"n = {ne_th:.5f}")
print(f"    rayo e a {np.degrees(ths):.3f}° de la normal (walk-off {np.degrees(the-ths):.3f}°)")

# ---------------- (c) ----------------
no, ne, L = 2.20, 2.29, 1e-2
th = np.radians(45.0)
n45 = n_e(th, no, ne)
ths = np.arctan(no**2 / ne**2 * np.tan(th))       # ángulo del rayo con el eje
rho = th - ths
print(f"\n(c) n(45°) = {n45:.5f}; rayo a {np.degrees(ths):.3f}° del eje; "
      f"walk-off rho = {np.degrees(rho):.3f}° = {rho*1e3:.2f} mrad")
print(f"    desplazamiento = L tan(rho) = {L*np.tan(rho)*1e3:.3f} mm")
ret = (n45 - no) * k0 * L
print(f"    retardo = (n(45°)-no) k0 L = {ret:.4e} rad = {ret/(2*np.pi):.2f} ondas; "
      f"mod 2pi = {np.degrees(ret % (2*np.pi)):.1f}°")

# Figura (c): superficie k en el plano (eje óptico, normal) con Delta n exagerado
fac = 5.0
ne_x = no + fac * (ne - no)
t = np.linspace(0, 2 * np.pi, 600)
fig, ax = plt.subplots(figsize=(5.6, 5.2))
# coordenadas: eje vertical = normal a la lámina; eje óptico a 45°
ca = np.array([np.sin(th), np.cos(th)])           # eje óptico (horizontal, vertical)
pa = np.array([np.cos(th), -np.sin(th)])
r_e = n_e(t, no, ne_x)
pts = np.outer(r_e * np.cos(t), ca) + np.outer(r_e * np.sin(t), pa)
ax.plot(no * np.cos(t), no * np.sin(t), 'C0', label=r'onda o: $k=n_ok_0$')
ax.plot(pts[:, 0], pts[:, 1], 'C3', label=r'onda e: elipse (6.3-21)')
ax.plot([-2.6 * ca[0], 2.6 * ca[0]], [-2.6 * ca[1], 2.6 * ca[1]], 'k--', lw=0.8)
ax.text(2.0 * ca[0], 2.15 * ca[1], 'eje óptico', rotation=45)
n45x = n_e(th, no, ne_x)
ax.annotate('', xy=(0, n45x), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color='k', lw=1.5))
ax.text(0.05, 1.2, r'$\mathbf{k}$ (normal a la lámina)', fontsize=8)
thsx = np.arctan(no**2 / ne_x**2 * np.tan(th))
dirS = np.cos(thsx) * ca - np.sin(thsx) * pa      # k = cos(th) ca - sin(th) pa
ax.annotate('', xy=tuple(2.3 * dirS), xytext=(0, 0),
            arrowprops=dict(arrowstyle='-|>', color='C3', lw=1.5))
ax.text(*(2.0 * dirS + np.array([0.1, 0.0])), r'$\mathbf{S}$ (rayo e)', color='C3', fontsize=8)
ax.axhline(0, color='0.6', lw=0.6)
ax.set_aspect('equal')
ax.set_xlim(-2.8, 2.8); ax.set_ylim(-2.8, 2.8)
ax.set_xlabel(r'$k_{\parallel}/k_0$ (a lo largo de la cara)')
ax.set_ylabel(r'$k_{\perp}/k_0$ (normal a la cara)')
ax.set_title(r'LiNbO$_3$, eje a 45°: $n_e-n_o$ exagerado $\times5$')
ax.legend(fontsize=8, loc='lower left')
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(base, f't3_p23_superficie_k.{ext}'), dpi=200)
print("figura guardada")
