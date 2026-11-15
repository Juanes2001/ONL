# -*- coding: utf-8 -*-
"""Problema 31: chi3 del oscilador NO centrosimétrico (cascada a^2) frente al centrosimétrico (b).

No resonante (todos los D -> w0^2), a = w0^2/d, b = w0^2/d^2, N = 1/d^3.
  chi3_a = (2 N a^2 e^4 / 3 eps0 m^3) * [3/w0^2] / w0^8 = 2 N a^2 e^4/(eps0 m^3 w0^10)
  chi3_b = N b e^4/(eps0 m^3 w0^8)               (Boyd 1.4.52 con i=j=k=l=1)
"""
import sys
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')
eps0 = 8.8541878128e-12
e = 1.602176634e-19
m = 9.1093837015e-31
d = 3e-10
N = 1/d**3
for w0 in (1e16, 7e15):
    a, b = w0**2/d, w0**2/d**2
    chi3_a = 2*N*a**2*e**4/(eps0*m**3*w0**10)
    chi3_b = N*b*e**4/(eps0*m**3*w0**8)
    print(f'w0 = {w0:.0e} rad/s: chi3_a = {chi3_a:.3e} m^2/V^2, chi3_b = {chi3_b:.3e} m^2/V^2,'
          f' razón a/b = {chi3_a/chi3_b:.2f}')

# Caso del índice no lineal chi3(w; w, w, -w), gamma -> 0: las tres sumas de pares son
# w+w = 2w, w-w = 0 y -w+w = 0, así que el corchete es 1/D(2w) + 2/D(0).
D = lambda x: 1 - x**2               # D/w0^2 sin amortiguamiento
for w in (0.0, 0.3, 0.45):
    suma = 1/D(2*w) + 2/D(0.0)
    print(f'w = {w:.2f} w0: [1/D(2w)+2/D(0)] w0^2 = {suma:.3f}  (límite no resonante: 3)')
