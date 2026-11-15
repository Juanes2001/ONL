"""Problema 7: pulso gaussiano con chirp lineal en el vacío (convención de Saleh, e^{jwt}).

f(t) = exp(-t^2/tau^2) exp(j 2 pi nu0 t + j b t^2),   E(z,t) = Re{f(t - z/c0)} x_hat.
Fase total phi(t) = 2 pi nu0 t + b t^2  ->  nu_i(t) = nu0 + b t / pi.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

tau = 20e-15          # s
nu0 = 375e12          # Hz
b = 5e27              # s^-2
c0 = 299_792_458.0

nu_i = lambda t: nu0 + b * t / np.pi
dnu = nu_i(tau) - nu_i(-tau)
print(f"lambda0 = c0/nu0 = {c0/nu0*1e9:.1f} nm;  periodo óptico = {1/nu0*1e15:.3f} fs")
print(f"nu_i(-tau) = {nu_i(-tau)*1e-12:.2f} THz, nu_i(+tau) = {nu_i(tau)*1e-12:.2f} THz")
print(f"Delta nu = 2 b tau / pi = {dnu*1e-12:.2f} THz  ({dnu/nu0*100:.1f} % de nu0)")
print(f"lambda_i(-tau) = {c0/nu_i(-tau)*1e9:.1f} nm, lambda_i(+tau) = {c0/nu_i(tau)*1e9:.1f} nm")
a = b * tau**2        # parámetro de chirp de Saleh (22.1-5): a = phi'' tau^2 / 2
print(f"parámetro de chirp a = b tau^2 = {a:.2f}")
# ancho espectral (FWHM de |F(nu)|^2) del pulso gaussiano con y sin chirp
dnu_tl = np.sqrt(2 * np.log(2)) / (np.pi * tau)
print(f"FWHM espectral sin chirp = {dnu_tl*1e-12:.2f} THz;  con chirp = {dnu_tl*np.sqrt(1+a**2)*1e-12:.2f} THz")

t = np.linspace(-2.5 * tau, 2.5 * tau, 4000)
f = np.exp(-t**2 / tau**2) * np.exp(1j * (2 * np.pi * nu0 * t + b * t**2))

fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
a1.plot(t * 1e15, f.real, lw=0.8, label=r'$\mathcal{E}_x(0,t)/E_0$')
a1.plot(t * 1e15, np.abs(f), 'k--', lw=1, label=r'$\pm e^{-t^2/\tau^2}$')
a1.plot(t * 1e15, -np.abs(f), 'k--', lw=1)
a1.plot(t * 1e15, np.abs(f)**2, color='C3', lw=1.5, label=r'$I(0,t)/I_{\rm max}=e^{-2t^2/\tau^2}$')
a1.set_ylabel('Campo e intensidad (normalizados)')
a1.legend(loc='upper right', fontsize=8)
a1.set_title(r'Pulso con chirp: $\tau=20$ fs, $\nu_0=375$ THz, $b=5\times10^{27}$ s$^{-2}$')

a2.plot(t * 1e15, nu_i(t) * 1e-12, 'C0')
for s in (-1, 1):
    a2.axvline(s * tau * 1e15, color='gray', ls=':')
    a2.plot(s * tau * 1e15, nu_i(s * tau) * 1e-12, 'ko')
a2.annotate(rf'$\Delta\nu={dnu*1e-12:.1f}$ THz', xy=(tau * 1e15, nu_i(tau) * 1e-12),
            xytext=(5, nu0 * 1e-12 + 40), arrowprops=dict(arrowstyle='->'))
a2.set_xlabel(r'$t - z/c_0$ (fs)')
a2.set_ylabel(r'$\nu_i$ (THz)')
a2.set_title(r'Frecuencia instantánea $\nu_i=\nu_0+bt/\pi$ (up-chirp)')
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't1_p07_pulso_chirp')
fig.savefig(base + '.png', dpi=200)
fig.savefig(base + '.pdf')
print("figura guardada:", os.path.normpath(base) + '.png/.pdf')
