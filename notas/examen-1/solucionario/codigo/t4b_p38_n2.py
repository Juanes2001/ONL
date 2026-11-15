"""Problema 38: del chi(3) al índice no lineal n2 (Boyd §1.2.8 y §4.1, convención SI de Boyd)."""
import numpy as np

c, eps0 = 2.998e8, 8.854e-12
e, m, a0 = 1.602e-19, 9.109e-31, 5.292e-11

# (a)-(b) Factor numérico de n2 = 3 chi3 / (4 n0^2 eps0 c)
K = 3/(4*eps0*c)
print(f"(b) 3/(4 eps0 c) = {K:.1f} V/A  (= 3 Z0/4, Z0 = {1/(eps0*c):.1f} ohm)")
print(f"    Si se usara (1.2.14b) impresa, 3/(2 eps0 c) = {2*K:.1f}: el doble")

n2_silice = K*1.8e-22/1.45**2
chi3_SiN = 2.4e-19*2.0**2/K
chi3_Si = 4.5e-18*3.48**2/K
print(f"    Sílice: n2 = {n2_silice:.3e} m^2/W = {n2_silice*1e4:.2e} cm^2/W")
print(f"    Si3N4 : chi3 = {chi3_SiN:.3e} m^2/V^2")
print(f"    Si    : chi3 = {chi3_Si:.3e} m^2/V^2")

E_at = e/(4*np.pi*eps0*a0**2)
chi3_at = 1/E_at**2
chi3_156 = 3.44e-22                      # (1.4.56)
print(f"    1/E_at^2 = {chi3_at:.3e} m^2/V^2;  estimación (1.4.56) = {chi3_156:.2e} m^2/V^2")
d = 3e-10
for nombre, chi3, n0 in (('sílice', 1.8e-22, 1.45), ('Si3N4', chi3_SiN, 2.0), ('Si', chi3_Si, 3.48)):
    chi1 = n0**2 - 1
    # modelo de Lorentz con N = 1/d^3: w0^2 = N e^2/(eps0 m chi1); luego (1.4.55)
    w0 = np.sqrt(e**2/(d**3*eps0*m*chi1))
    chi3_mod = e**4/(eps0*m**3*w0**6*d**5)
    print(f"    {nombre:6s}: chi3/(1/E_at^2) = {chi3/chi3_at:8.1f}, chi3/(1.4.56) = {chi3/chi3_156:7.2f};"
          f"  w0 deducido de n0 = {w0:.2e} rad/s (hbar w0 = {1.0546e-34*w0/e:.1f} eV),"
          f" chi3 del modelo = {chi3_mod:.2e} (real/modelo = {chi3/chi3_mod:.1f})")

# (c) Delta n y fase no lineal en sílice
I = 1e9*1e4                              # 1 GW/cm^2 en W/m^2
lam, L = 1.064e-6, 1e-2
dn = n2_silice*I
phi = 2*np.pi/lam*dn*L
print(f"(c) I = {I:.1e} W/m^2: Delta n = {dn:.3e};  phi_NL(1 cm) = {phi:.4f} rad")

# Comparación con el foco del Problema 4 (P = 1 MW, W0 = 20 um, n = 1.5)
P, W0, n = 1e6, 20e-6, 1.5
I0 = 2*P/(np.pi*W0**2)
z0 = np.pi*W0**2*n/lam
dn4 = n2_silice*I0
phi4 = 2*np.pi/lam*dn4*np.pi*z0          # int dz/(1+z^2/z0^2) = pi z0 (cristal largo)
Pcr = np.pi*0.61**2*lam**2/(8*1.45*n2_silice)    # Boyd (7.1.1)
print(f"    Prob. 4: I0 = {I0:.3e} W/m^2, z0 = {z0*1e3:.2f} mm, Delta n = {dn4:.2e},"
      f" phi_NL (foco entero, pi z0) = {phi4:.2f} rad")
print(f"    Potencia crítica de autoenfoque (7.1.1) en sílice: {Pcr:.2e} W;  P/Pcr = {P/Pcr:.2f}")
