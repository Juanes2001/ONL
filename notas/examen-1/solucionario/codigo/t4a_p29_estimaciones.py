# -*- coding: utf-8 -*-
"""Problema 29: estimaciones numéricas y unidades (Boyd §1.1, Probs. 1.1 y 1.2, apéndice C)."""
import sys
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

eps0 = 8.8541878128e-12      # F/m
c = 2.99792458e8             # m/s
e = 1.602176634e-19          # C
a0 = 5.29177210903e-11       # m (radio de Bohr)
hbar = 1.054571817e-34
m = 9.1093837015e-31

# (a) gaussiano -> SI: chi2(SI) = 4*pi/(3e4) * chi2(gauss)   (Boyd, ec. C.11, p. 602)
chi2_G = 1.3e-7               # cm/statvolt
chi2_SI = 4*np.pi/3e4 * chi2_G
print(f'(a) factor 4pi/3e4 = {4*np.pi/3e4:.4e};  chi2 = {chi2_SI:.3e} m/V')

# (b) haz de 1 W enfocado a 30 um de diámetro, n = 2, chi2 = 4e-11 m/V
P_haz, diam, n, chi2, N = 1.0, 30e-6, 2.0, 4e-11, 1e28
area = np.pi*(diam/2)**2
I = P_haz/area
E = np.sqrt(I/(2*n*eps0*c))   # I = 2 n eps0 c |E|^2  (Boyd, ec. 2.2.16)
P2w = eps0*chi2*E**2          # P(2w) = eps0 chi2 E^2 (Boyd, ec. 1.2.7)
mu2w = P2w/N
chi1 = n**2 - 1
Pw = eps0*chi1*E
muw = Pw/N
ea0 = e*a0
print(f'(b) area = {area:.4e} m^2, I = {I:.4e} W/m^2 = {I*1e-4:.4e} W/cm^2')
print(f'    |E(w)| = {E:.4e} V/m  (campo real de pico 2|E| = {2*E:.4e} V/m)')
print(f'    P(2w) = {P2w:.4e} C/m^2,  mu(2w) = {mu2w:.4e} C m = {mu2w/ea0:.3e} e a0')
print(f'    P(w)  = {Pw:.4e} C/m^2,  mu(w)  = {muw:.4e} C m = {muw/ea0:.3e} e a0')
print(f'    e a0 = {ea0:.4e} C m;  razón mu(2w)/mu(w) = {mu2w/muw:.3e}'
      f'  (= chi2 E/chi1 = {chi2*E/chi1:.3e})')

# (c) campo atómico y estimaciones
Eat = e/(4*np.pi*eps0*a0**2)
Iat = 0.5*eps0*c*Eat**2
print(f'(c) E_at = {Eat:.4e} V/m; chi2 ~ 1/E_at = {1/Eat:.3e} m/V; '
      f'chi3 ~ 1/E_at^2 = {1/Eat**2:.3e} m^2/V^2')
print(f'    I_at = {Iat:.3e} W/m^2 = {Iat*1e-4:.3e} W/cm^2')

# (d) d de Saleh (C/V^2) -> d de Boyd (m/V)
dS = 3e-23
print(f'(d) d_Boyd = d_Saleh/eps0 = {dS/eps0:.4e} m/V = {dS/eps0*1e12:.3f} pm/V;'
      f'  chi2_Boyd = 2 d_Boyd = {2*dS/eps0*1e12:.2f} pm/V')
chi3S = 1e-33   # ejemplo, C m/V^3 (Saleh da 1e-34 a 1e-29, p. 877)
print(f'    ejemplo chi3_Saleh = {chi3S:.0e} C m/V^3 -> chi3_Boyd = 4 chi3_S/eps0 = '
      f'{4*chi3S/eps0:.3e} m^2/V^2')
