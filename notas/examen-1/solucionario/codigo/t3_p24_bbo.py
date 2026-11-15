"""Problema 24: ajuste de fase tipo I (ooe) en BBO a 1064/532 nm con n(theta) (Saleh 6.3-15).

(b) theta tal que n_e(532, theta) = n_o(1064).  (c) walk-off y separación en 5 mm.
(d) desajuste Delta k y longitud de coherencia para theta = 0.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

no1, ne1 = 1.6551, 1.5425        # 1064 nm
no2, ne2 = 1.6749, 1.5555        # 532 nm
lam1, lam2 = 1064e-9, 532e-9
L = 5e-3


def n_e(theta, no, ne):
    return 1 / np.sqrt(np.cos(theta)**2 / no**2 + np.sin(theta)**2 / ne**2)   # (6.3-15)


s2 = (1 / no1**2 - 1 / no2**2) / (1 / ne2**2 - 1 / no2**2)
th = np.arcsin(np.sqrt(s2))
print(f"(b) sin^2(theta) = {s2:.5f} -> theta_pm = {np.degrees(th):.3f}°; "
      f"comprobación n_e(532, theta) = {n_e(th, no2, ne2):.5f} vs n_o(1064) = {no1}")
ths = np.arctan(no2**2 / ne2**2 * np.tan(th))       # dirección del rayo e respecto al eje
rho = ths - th
print(f"(c) rayo e a {np.degrees(ths):.3f}° del eje: walk-off rho = {np.degrees(rho):.3f}° "
      f"= {rho*1e3:.1f} mrad (se aleja del eje: uniaxial negativo)")
tan_rho = 0.5 * n_e(th, no2, ne2)**2 * (1 / ne2**2 - 1 / no2**2) * np.sin(2 * th)
print(f"    fórmula tan(rho) = (n^2/2)(1/ne^2 - 1/no^2) sin(2theta) = {np.degrees(np.arctan(tan_rho)):.3f}°")
print(f"    separación tras {L*1e3:.0f} mm: {L*np.tan(rho)*1e6:.0f} µm")
dk = 2 * np.pi * no2 / lam2 - 2 * (2 * np.pi * no1 / lam1)
print(f"(d) theta = 0: Delta k = {dk:.4e} 1/m; L_c = pi/|Dk| = {np.pi/abs(dk)*1e6:.2f} µm")

t = np.linspace(0, np.pi / 2, 500)
fig, ax = plt.subplots(figsize=(6.4, 4))
ax.plot(np.degrees(t), no1 + 0 * t, 'C0', label=r'$n_o(1064)$ (fundamental, onda o)')
ax.plot(np.degrees(t), n_e(t, no1, ne1), 'C0--', label=r'$n_e(1064,\theta)$')
ax.plot(np.degrees(t), no2 + 0 * t, 'C2', label=r'$n_o(532)$')
ax.plot(np.degrees(t), n_e(t, no2, ne2), 'C2--', label=r'$n_e(532,\theta)$ (armónico, onda e)')
ax.plot(np.degrees(th), no1, 'ko')
ax.annotate(rf'$\theta_{{pm}}={np.degrees(th):.1f}^\circ$', (np.degrees(th), no1),
            (np.degrees(th) + 10, no1 + 0.012), arrowprops=dict(arrowstyle='->'))
ax.set_xlabel(r'Ángulo $\theta$ entre $\mathbf{k}$ y el eje óptico (grados)')
ax.set_ylabel('Índice de refracción')
ax.set_title('BBO: ajuste de fase tipo I (ooe)')
ax.set_xlim(0, 90)
ax.legend(fontsize=8, loc='lower left')
ax.grid(alpha=0.3)
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(base, f't3_p24_bbo.{ext}'), dpi=200)
print("figura guardada")
