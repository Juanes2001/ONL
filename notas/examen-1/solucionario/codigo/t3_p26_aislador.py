"""Problema 26: actividad óptica y aislador de Faraday con matrices de Jones (Saleh §6.4, §6.6D).

Todo se escribe en ejes FIJOS del laboratorio (x, y), iguales para ida y vuelta.
Regla: elemento recíproco -> matriz de vuelta = transpuesta de la de ida;
       rotador de Faraday -> la misma matriz (el sentido lo fija B, no k).
"""
import numpy as np

rot = lambda a: np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])     # (6.1-20)
pol = lambda a: np.array([[np.cos(a)**2, np.sin(a)*np.cos(a)],
                          [np.sin(a)*np.cos(a), np.sin(a)**2]])                  # (6.1-25)
ret = lambda G, a: rot(a) @ np.diag([1, np.exp(-1j*G)]) @ rot(-a)               # (6.1-24)

# (a) cuarzo
rho = 31.0                                   # °/mm a 500 nm
print(f"(a) d(90°) = {90/rho:.3f} mm; ida y vuelta: R(-90°)R(90°) = \n{np.round(rot(-np.pi/2) @ rot(np.pi/2), 12).real}")

# (b) TGG
V, B = -40.0, 1.0                            # rad/(T m), T
L = (np.pi / 4) / (abs(V) * B)
print(f"(b) L(45°) = {L*1e3:.2f} mm")
A, Bp, F = pol(0), pol(np.pi/4), rot(np.pi/4)
ida = Bp @ F @ A
vuelta = A @ F @ Bp                          # Faraday: misma matriz en ejes del laboratorio
for nombre, J in (("x", [1, 0]), ("y", [0, 1]), ("45°", [1, 1]), ("R", [1, 1j])):
    J = np.array(J, complex) / np.linalg.norm(J)
    print(f"    entrada {nombre:>3}: T_ida = {np.linalg.norm(ida@J)**2:.3f}, "
          f"T_vuelta = {np.linalg.norm(vuelta@J)**2:.3f}")

# (c) rotador recíproco y lámina lambda/2 a 22.5°
Fr = rot(np.pi/4)
vuelta_rec = A @ Fr.T @ Bp
H = ret(np.pi, np.pi/8)
vuelta_H = A @ H.T @ Bp
J45 = np.array([1, 1]) / np.sqrt(2)
print(f"(c) vuelta con rotador recíproco: T = {np.linalg.norm(vuelta_rec@J45)**2:.3f}; "
      f"con lámina lambda/2 a 22.5°: T = {np.linalg.norm(vuelta_H@J45)**2:.3f}")
