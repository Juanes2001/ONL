"""Problema 25: cristal biaxial KTP a 1064 nm (Saleh §6.3C-D).

Propagación en el plano x-z a un ángulo theta de z: índices n_y y n_xz(theta);
ángulo V_z de los ejes ópticos con el eje z.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

nx, ny, nz = 1.7377, 1.7453, 1.8297
n_xz = lambda t: 1 / np.sqrt(np.cos(t)**2 / nx**2 + np.sin(t)**2 / nz**2)

sV = nz / ny * np.sqrt((ny**2 - nx**2) / (nz**2 - nx**2))
V = np.arcsin(sV)
print(f"sin V_z = {sV:.5f} -> V_z = {np.degrees(V):.2f}°; comprobación n_xz(V) = {n_xz(V):.5f} = n_y = {ny}")
print(f"ángulo entre los dos ejes ópticos 2V_z = {2*np.degrees(V):.2f}°")

t = np.linspace(0, np.pi / 2, 500)
fig, ax = plt.subplots(figsize=(6.4, 4))
ax.plot(np.degrees(t), ny + 0 * t, 'C0', label=r'$\mathbf{D}\parallel\hat{y}$: $n_a=n_y$')
ax.plot(np.degrees(t), n_xz(t), 'C3', label=r'$\mathbf{D}$ en el plano $x$-$z$: $n_b(\theta)$')
ax.plot(np.degrees(V), ny, 'ko')
ax.annotate(rf'eje óptico, $V_z={np.degrees(V):.1f}^\circ$', (np.degrees(V), ny),
            (np.degrees(V) + 12, ny + 0.025), arrowprops=dict(arrowstyle='->'))
ax.set_xlabel(r'Ángulo $\theta$ entre $\mathbf{k}$ y el eje $z$ (grados), $\mathbf{k}$ en el plano $x$-$z$')
ax.set_ylabel('Índice del modo normal')
ax.set_title('KTP a 1064 nm')
ax.set_xlim(0, 90)
ax.legend(fontsize=8, loc='upper left')
ax.grid(alpha=0.3)
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(base, f't3_p25_ktp.{ext}'), dpi=200)
print("figura guardada")
