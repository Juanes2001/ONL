"""Problema 3: onda estacionaria transversal que viaja en z (convención de Saleh, e^{jwt}).

E = E0 cos(beta x) exp(-j kz z) y_hat en el vacío.
Se calcula H con Maxwell, el vector de Poynting complejo S = (1/2) E x H*, y se grafica:
  (a) una instantánea del campo real E_y(x, z, t=0) con las flechas de Re{S};
  (b) los perfiles transversales de Re{S_z} e Im{S_x}.
Ejemplo: lambda0 = 1 µm, ángulo de las ondas planas theta = 30° (beta = k0 sin theta).
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

c0 = 299_792_458.0
mu0 = 4e-7 * np.pi
eta0 = mu0 * c0                     # impedancia del vacío, aprox. 376.7 ohm

lam0 = 1.0e-6                       # m
k0 = 2 * np.pi / lam0
theta = np.deg2rad(30.0)            # ángulo de cada onda plana con el eje z
beta = k0 * np.sin(theta)           # número de onda transversal
kz = np.sqrt(k0**2 - beta**2)       # relación de dispersión beta^2 + kz^2 = k0^2
w = k0 * c0
E0 = 1.0                            # V/m (amplitud arbitraria)

print(f"k0 = {k0:.4e} 1/m, beta = {beta:.4e} 1/m, kz = {kz:.4e} 1/m")
print(f"beta^2 + kz^2 - k0^2 = {beta**2 + kz**2 - k0**2:.2e} (debe ser 0)")
print(f"periodo transversal de |E|^2: pi/beta = {np.pi/beta*1e6:.3f} µm; "
      f"longitud de onda axial 2pi/kz = {2*np.pi/kz*1e6:.3f} µm")

x = np.linspace(-2 * np.pi / beta, 2 * np.pi / beta, 400)
z = np.linspace(0, 3 * 2 * np.pi / kz, 400)
X, Z = np.meshgrid(x, z, indexing='xy')

# Amplitudes complejas
Ey = E0 * np.cos(beta * X) * np.exp(-1j * kz * Z)
Hx = -(kz / (w * mu0)) * E0 * np.cos(beta * X) * np.exp(-1j * kz * Z)
Hz = -1j * (beta / (w * mu0)) * E0 * np.sin(beta * X) * np.exp(-1j * kz * Z)

# S = (1/2) E x H*, con E = Ey y_hat:  y x x = -z,  y x z = +x
Sx = 0.5 * Ey * np.conj(Hz)
Sz = -0.5 * Ey * np.conj(Hx)

print(f"max |Re Sx| = {np.abs(Sx.real).max():.2e} W/m^2 (debe ser 0)")
print(f"max Im Sx = {Sx.imag.max():.4e} W/m^2;  beta|E0|^2/(4 w mu0) = {beta*E0**2/(4*w*mu0):.4e}")
print(f"max Re Sz = {Sz.real.max():.4e} W/m^2;  kz|E0|^2/(2 w mu0) = {kz*E0**2/(2*w*mu0):.4e}")
print(f"comparar: |E0|^2/(2 eta0) = {E0**2/(2*eta0):.4e};  cos(theta) = {np.cos(theta):.4f}")

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw={'width_ratios': [1.4, 1]})
im = a1.pcolormesh(Z * 1e6, X * 1e6, np.real(Ey), cmap='RdBu_r', shading='auto', vmin=-1, vmax=1)
fig.colorbar(im, ax=a1, label=r'$\mathcal{E}_y(x,z,t=0)/E_0$')
sl = (slice(20, None, 40), slice(20, None, 40))
a1.quiver(Z[sl] * 1e6, X[sl] * 1e6, np.real(Sz[sl]), np.real(Sx[sl]), color='k', width=0.004)
a1.set_xlabel(r'$z$ (µm)')
a1.set_ylabel(r'$x$ (µm)')
a1.set_title(r'Campo real y flechas de Re$\{\mathbf{S}\}$ ($\theta=30^\circ$)')

x1 = x
a2.plot(x1 * 1e6, 0.5 * kz / (w * mu0) * np.cos(beta * x1)**2 * 2 * eta0, label=r'Re$\{S_z\}$')
a2.plot(x1 * 1e6, beta / (4 * w * mu0) * np.sin(2 * beta * x1) * 2 * eta0, '--', label=r'Im$\{S_x\}$')
a2.axhline(0, color='gray', lw=0.6)
a2.set_xlabel(r'$x$ (µm)')
a2.set_ylabel(r'$S/(|E_0|^2/2\eta_0)$ (adim.)')
a2.set_title('Perfiles transversales')
a2.legend(loc='lower left', fontsize=8, framealpha=0.9)
fig.tight_layout()

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't1_p03_onda_estacionaria')
fig.savefig(base + '.png', dpi=200)
fig.savefig(base + '.pdf')
print("figura guardada:", os.path.normpath(base) + '.png/.pdf')
