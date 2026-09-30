"""Cintura w0 de un haz gaussiano dado su ancho w1 y radio de curvatura R1 en un punto.

Se resuelve para w0 la ecuación
    w1^2 = w0^2 [1 + (z1 λ / (π w0^2))^2],   con  z1 = R1 [1 - (w0/w1)^2].

Solo usa la biblioteca estándar (el python3 del sistema no tiene numpy/scipy).
"""
import math

# Parámetros (SI)
w1 = 1e-3     # ancho del haz en el punto 1 [m]
lam = 1e-6    # longitud de onda [m]
R1 = 1.0      # radio de curvatura en el punto 1 [m]


def z1(w0):
    return R1 * (1 - (w0 / w1) ** 2)


def f(w0):
    """Residuo de la ecuación: w0^2 [1 + (z1 λ/(π w0^2))^2] - w1^2."""
    return w0**2 * (1 + (z1(w0) * lam / (math.pi * w0**2)) ** 2) - w1**2


def biseccion(g, a, b, tol=1e-15, max_iter=200):
    fa = g(a)
    for _ in range(max_iter):
        m = 0.5 * (a + b)
        fm = g(m)
        if fa * fm <= 0:
            b = m
        else:
            a, fa = m, fm
        if b - a < tol:
            break
    return 0.5 * (a + b)


# 1) Barrido de w0 en (0, w1) para ubicar cambios de signo del residuo
N = 100_000
raices = []
prev_w, prev_f = None, None
for k in range(1, N):
    w = w1 * k / N
    fw = f(w)
    if prev_f is not None and prev_f * fw < 0:
        raices.append(biseccion(f, prev_w, w))
    prev_w, prev_f = w, fw

# 2) Solución analítica: con u = (w0/w1)^2 y b = λR1/(π w1^2) la ecuación queda
#    u(1 - u) = b^2 (1 - u)^2  ->  u = 1 (trivial, z1 = 0, R1 -> ∞)  o  u = b^2/(1 + b^2)
b = lam * R1 / (math.pi * w1**2)
w0_analitico = w1 * math.sqrt(b**2 / (1 + b**2))

print("Raíces numéricas no triviales (0 < w0 < w1):")
for w0 in raices:
    zR = math.pi * w0**2 / lam
    z = z1(w0)
    R_chk = z * (1 + (zR / z) ** 2)
    w_chk = w0 * math.sqrt(1 + (z / zR) ** 2)
    print(f"  w0      = {w0*1e3:.6f} mm")
    print(f"  z1      = {z:.6f} m")
    print(f"  z_R     = {zR:.6f} m")
    print(f"  residuo = {f(w0):.3e} m^2")
    print(f"  verificación: w(z1) = {w_chk*1e3:.6f} mm, R(z1) = {R_chk:.6f} m")
print(f"\nSolución analítica: w0 = {w0_analitico*1e3:.6f} mm  (b = {b:.6f})")
print("Raíz trivial w0 = w1 = 1 mm descartada: da z1 = 0 (plano de la cintura, R = ∞ ≠ 1 m).")
