# -*- coding: utf-8 -*-
"""Problema 30: oscilador anarmónico no centrosimétrico (Boyd §1.4.1-1.4.2, pp. 22-28).

(c)-(d) estimación no resonante de chi2 y de la constante de Miller;
(e) |chi2(2w; w, w)| frente a w/w0 con gamma = 0.02 w0 (Boyd, ec. 1.4.20).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.stdout.reconfigure(encoding='utf-8')
eps0 = 8.8541878128e-12
e = 1.602176634e-19
m = 9.1093837015e-31

# ---------- (d) estimación no resonante ----------
w0 = 1e16          # rad/s
d = 3e-10          # m
N = 1/d**3         # m^-3
a = w0**2/d        # (1.4.30)
chi1 = N*e**2/(eps0*m*w0**2)               # (1.4.17) con D -> w0^2
chi2 = N*e**3*a/(eps0*m**2*w0**6)          # (1.4.24) con D -> w0^2
chi2_cerrada = e**3/(eps0*m**2*w0**4*d**4) # (1.4.31)
miller = m*a*eps0**2/(N**2*e**3)           # (1.4.29)
print(f'N = {N:.3e} m^-3,  a = {a:.3e} m^-1 s^-2')
print(f'chi1 (no resonante) = {chi1:.3f}  -> n = {np.sqrt(1+chi1):.3f}')
print(f'chi2 = {chi2:.3e} m/V  (forma cerrada 1.4.31: {chi2_cerrada:.3e} m/V)')
print(f'd = chi2/2 = {chi2/2*1e12:.2f} pm/V')
print(f'constante de Miller m a eps0^2/(N^2 e^3) = {miller:.3e} m/V;'
      f'  x chi1^3 = {miller*chi1**3:.3e} m/V')

# ---------- (e) |chi2(2w)| normalizada ----------
g = 0.02                                   # gamma/w0
D = lambda x: 1 - x**2 - 2j*x*g            # D(w)/w0^2 con x = w/w0
x = np.linspace(0.01, 1.6, 20001)
r = 1/np.abs(D(2*x)*D(x)**2)               # |chi2(2w)| / chi2(no resonante)
# picos
for lo, hi in [(0.3, 0.7), (0.8, 1.2)]:
    sel = (x > lo) & (x < hi)
    k = np.argmax(r[sel])
    print(f'pico en w/w0 = {x[sel][k]:.4f}: |chi2|/chi2(0) = {r[sel][k]:.1f}')
print(f'valores en w0/2: {1/abs(D(1.0)*D(0.5)**2):.1f};  en w0: {1/abs(D(2.0)*D(1.0)**2):.1f}')

fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.semilogy(x, r, color='C0', lw=1.4)
ax.axvline(0.5, color='gray', ls='--', lw=0.8)
ax.axvline(1.0, color='gray', ls='--', lw=0.8)
ax.text(0.53, 60, r'$2\omega=\omega_0$' + '\n' + r'(dos fotones, $D(2\omega)$)', fontsize=8)
ax.text(1.05, 60, r'$\omega=\omega_0$' + '\n' + r'(un fotón, $D^2(\omega)$)', fontsize=8)
ax.set_xlabel(r'Frecuencia normalizada $\omega/\omega_0$ (adim.)')
ax.set_ylabel(r'$|\chi^{(2)}(2\omega;\omega,\omega)|\,/\,\chi^{(2)}_{\rm no\ res}$ (adim.)')
ax.set_title(r'Oscilador anarmónico, $\gamma=0.02\,\omega_0$', fontsize=10)
ax.set_xlim(0, 1.6)
ax.set_ylim(3e-2, 1e3)
ax.grid(True, which='both', alpha=0.3)
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't4a_p30_chi2_resonancias')
fig.savefig(base + '.png', dpi=200)
fig.savefig(base + '.pdf')
print('figura guardada:', os.path.normpath(base) + '.png/.pdf')
