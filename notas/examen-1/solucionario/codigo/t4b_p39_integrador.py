"""Problema 39: cristal uniaxial 'modelo' (oscilador de Lorentz y anarmónico, convención de Boyd)."""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

c, eps0, e, m = 2.998e8, 8.854e-12, 1.602e-19, 9.109e-31
w0, N, d = 1.2e16, 5e28, 3.5e-10

wp2 = N*e**2/(eps0*m)                    # "frecuencia de plasma" al cuadrado
print(f"wp^2 = {wp2:.4e} rad^2/s^2, w0^2 = {w0**2:.4e}, chi(0) = {wp2/w0**2:.4f}")

def n_lorentz(lam):
    w = 2*np.pi*c/lam
    chi = wp2/(w0**2 - w**2)
    return np.sqrt(1 + chi), chi, w

# (a)
n1, chi1, w1 = n_lorentz(1064e-9)
n2, chi2, w2 = n_lorentz(532e-9)
print(f"(a) 1064 nm: w = {w1:.4e} rad/s, chi1 = {chi1:.4f}, n = {n1:.4f}")
print(f"    532 nm : w = {w2:.4e} rad/s, chi1 = {chi2:.4f}, n = {n2:.4f};  n(532)-n(1064) = {n2-n1:.4f}")

# (b) chi2(2w;w,w) = N e^3 a / (eps0 m^2 D(2w) D(w)^2), a = w0^2/d, sin amortiguamiento
a = w0**2/d
pref = N*e**3*a/(eps0*m**2)
D = lambda w: w0**2 - w**2
chi2_full = pref/(D(2*w1)*D(w1)**2)
chi2_nr = pref/w0**6
print(f"(b) a = {a:.4e} m^-1 s^-2;  chi2 completa = {chi2_full:.3e} m/V;  no resonante = {chi2_nr:.3e} m/V;"
      f"  razón = {chi2_full/chi2_nr:.4f}")
# Miller: misma cantidad con chi1
miller = eps0**2*m*a/(N**2*e**3)*chi2*chi1**2
print(f"    Comprobación con (1.4.21): {miller:.3e} m/V")

# (c) Ajuste de fase tipo I (ooe): n_e(2w, theta) = n_o(w); Boyd (2.3.11)
no1, no2 = n1, n2
B_min = no2 - no1
print(f"(c) birrefringencia mínima a 532 nm: n_o(532) - n_e(532) >= {B_min:.4f}")
def theta_pm(B):
    ne2 = no2 - B
    s2 = (1/no1**2 - 1/no2**2)/(1/ne2**2 - 1/no2**2)
    return np.degrees(np.arcsin(np.sqrt(s2))) if s2 <= 1 else np.nan
for B in (B_min, 0.03, 0.05, 0.08, 0.12):
    print(f"    B = {B:.4f} (n_e(532) = {no2-B:.4f}): theta_pm = {theta_pm(B):.2f} grados")
# resonancia extraordinaria que daría ajuste a 90 grados (no crítico)
chi_z = no1**2 - 1
w0z = np.sqrt(wp2/chi_z + w2**2)
print(f"    Para theta = 90 grados haría falta w0z = {w0z:.4e} rad/s ({(w0z/w0-1)*100:.1f} % mayor que w0)")

Bs = np.linspace(B_min*1.0001, 0.15, 400)
fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(Bs, [theta_pm(B) for B in Bs], 'C0')
ax.axvline(B_min, color='gray', ls=':', lw=0.8)
ax.annotate(r'$B_{\rm min}=n_o(2\omega)-n_o(\omega)$', xy=(B_min, 85), xytext=(0.05, 80), fontsize=8,
            arrowprops=dict(arrowstyle='->', lw=0.6))
ax.set_xlabel(r'Birrefringencia a 532 nm, $B=n_o(532)-n_e(532)$')
ax.set_ylabel(r'Ángulo de ajuste $\theta_{pm}$ (grados)')
ax.set_title('Cristal modelo, SHG tipo I (ooe) 1064 nm $\\to$ 532 nm', fontsize=10)
ax.grid(alpha=0.3); ax.set_ylim(0, 92)
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't4b_p39_theta_pm')
fig.savefig(base + '.png', dpi=200); fig.savefig(base + '.pdf')

# (d) Haz del Prob. 1.2 de Boyd: 1 W en 30 um de diámetro
Pw, D30 = 1.0, 30e-6
I = Pw/(np.pi*(D30/2)**2)
for n, etiqueta in ((n1, 'n = n(1064) del modelo'), (2.0, 'n = 2 del Prob. 1.2')):
    E = np.sqrt(I/(2*n*eps0*c))
    for chi, nom in ((chi2_full, 'completa'), (chi2_nr, 'no resonante')):
        deff = chi/2
        P2 = 2*eps0*deff*E**2
        print(f"(d) {etiqueta}: I = {I:.4e} W/m^2, |E| = {E:.3e} V/m; chi2 {nom}: d_eff = {deff*1e12:.2f} pm/V,"
              f" P(2w) = {P2:.2e} C/m^2")
# Con el factor angular de 3m tipo I si toda la no linealidad fuera d22 (cos theta), ejemplo B=0.08
th = np.radians(theta_pm(0.08))
print(f"    Ejemplo: con B = 0.08, theta_pm = {np.degrees(th):.1f} grados, cos(theta) = {np.cos(th):.3f}")
