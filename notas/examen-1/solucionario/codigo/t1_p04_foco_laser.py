"""Problema 4: campos de un láser Nd:YAG enfocado en vidrio frente al campo atómico.

Convenciones:
  Saleh: E(t) = Re{E e^{jwt}},  I = |E|^2 / (2 eta),  eta = eta0 / n   (|E| = amplitud de pico)
  Boyd : E(t) = E e^{-iwt} + c.c.,  I = 2 n eps0 c |E|^2                 (|E| = mitad del pico)
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

c0 = 299_792_458.0
eps0 = 8.8541878128e-12
mu0 = 1.25663706212e-6
eta0 = np.sqrt(mu0 / eps0)
e = 1.602176634e-19
a0 = 5.29177210903e-11            # radio de Bohr (m)

lam0 = 1.064e-6                   # m
Ep = 10e-3                        # J, energía del pulso
tp = 10e-9                        # s, duración (potencia constante)
n = 1.50
W0 = 20e-6                        # m, cintura

# (a) potencia, intensidad y fluencia pico
P = Ep / tp
I0 = 2 * P / (np.pi * W0**2)      # Saleh (3.1-16) en rho = 0, z = 0
F0 = 2 * Ep / (np.pi * W0**2)     # fluencia pico = I0 * tp
print(f"(a) P = {P:.3e} W")
print(f"    I0 = {I0:.3e} W/m^2 = {I0*1e-4:.3e} W/cm^2")
print(f"    F0 = {F0:.3e} J/m^2 = {F0*1e-4:.3e} J/cm^2")

# (b) campo en las dos convenciones
eta = eta0 / n
ES = np.sqrt(2 * eta * I0)
EB = np.sqrt(I0 / (2 * n * eps0 * c0))
print(f"(b) eta = {eta:.2f} Ohm")
print(f"    |E|_Saleh = {ES:.3e} V/m,  |E|_Boyd = {EB:.3e} V/m,  cociente = {ES/EB:.4f}")
print(f"    comprobación: |E_S|^2/(2 eta) = {ES**2/(2*eta):.4e},  2 n eps0 c |E_B|^2 = {2*n*eps0*c0*EB**2:.4e} W/m^2")

# (c) campo atómico y razones de polarización (campo real de pico = |E|_Saleh = 2|E|_Boyd)
Eat = e / (4 * np.pi * eps0 * a0**2)
r2 = ES / Eat
r3 = (ES / Eat)**2
print(f"(c) E_at = {Eat:.4e} V/m")
print(f"    |P2|/|P1| ~ E/E_at = {r2:.3e};  |P3|/|P1| ~ (E/E_at)^2 = {r3:.3e}")

# (d) rango de Rayleigh dentro del vidrio (lambda = lambda0/n)
z0 = np.pi * W0**2 * n / lam0
theta0 = lam0 / (n * np.pi * W0)
print(f"(d) z0 = {z0:.4e} m = {z0*1e3:.3f} mm;  2 z0 = {2*z0*1e3:.3f} mm;  theta0 = {theta0*1e3:.2f} mrad")

# Figura: I(rho, z)/I0 en el foco, con W(z) y ±z0
z = np.linspace(-3 * z0, 3 * z0, 500)
rho = np.linspace(-4 * W0, 4 * W0, 400)
Zg, Rg = np.meshgrid(z, rho)
Wz = W0 * np.sqrt(1 + (Zg / z0)**2)
I = (W0 / Wz)**2 * np.exp(-2 * Rg**2 / Wz**2)
fig, ax = plt.subplots(figsize=(8, 3.8))
pc = ax.pcolormesh(Zg * 1e3, Rg * 1e6, I, cmap='inferno', shading='auto')
fig.colorbar(pc, ax=ax, label=r'$I(\rho,z)/I_0$')
Wl = W0 * np.sqrt(1 + (z / z0)**2)
ax.plot(z * 1e3, Wl * 1e6, 'c--', lw=1.2, label=r'$\pm W(z)$')
ax.plot(z * 1e3, -Wl * 1e6, 'c--', lw=1.2)
for s in (-1, 1):
    ax.axvline(s * z0 * 1e3, color='w', lw=0.8, ls=':')
ax.annotate('', xy=(z0 * 1e3, 60), xytext=(-z0 * 1e3, 60),
            arrowprops=dict(arrowstyle='<->', color='w'))
ax.text(0, 64, rf'$2z_0={2*z0*1e3:.2f}$ mm', color='w', ha='center')
ax.set_xlabel(r'$z$ (mm), dentro del vidrio ($n=1.50$)')
ax.set_ylabel(r'$\rho$ (µm)')
ax.set_title(rf'Foco: $W_0=20$ µm, $I_0={I0*1e-4/1e11:.2f}\times10^{{11}}$ W/cm$^2$')
ax.legend(loc='lower right')
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't1_p04_foco')
fig.savefig(base + '.png', dpi=200)
fig.savefig(base + '.pdf')
print("figura guardada:", os.path.normpath(base) + '.png/.pdf')
