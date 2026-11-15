"""Problema 22: Goos-Hänchen y penetración de la onda evanescente (Saleh, Probs. 6.2-7, 6.2-8).

Vidrio n1 = 1.5 -> aire n2 = 1, theta = 1.2 theta_c, lambda0 = 633 nm.
xi = d(phi_TE)/d(theta) = 2 sin(theta) / sqrt(sin^2 theta - sin^2 theta_c)  (derivado en el texto).
"""
import numpy as np

n1, n2, lam0 = 1.5, 1.0, 633e-9
k0 = 2 * np.pi / lam0
thc = np.arcsin(n2 / n1)
th = 1.2 * thc

# fase TE en RTI (6.2-11) y su derivada numérica, para comparar con la fórmula analítica
phi = lambda t: 2 * np.arctan(np.sqrt(np.cos(thc)**2 / np.cos(t)**2 - 1))
h = 1e-6
xi_num = (phi(th + h) - phi(th - h)) / (2 * h)
xi = 2 * np.sin(th) / np.sqrt(np.sin(th)**2 - np.sin(thc)**2)
print(f"theta = {np.degrees(th):.3f}°: xi analítico = {xi:.4f}, xi numérico = {xi_num:.4f} (rad/rad)")

gamma = k0 * np.sqrt(n1**2 * np.sin(th)**2 - n2**2)     # decaimiento del campo en el aire
print(f"gamma = {gamma:.4e} 1/m -> 1/gamma = {1e9/gamma:.1f} nm (campo); "
      f"1/(2 gamma) = {1e9/(2*gamma):.1f} nm (intensidad)")

k1 = n1 * k0
Dy = xi / (k1 * np.cos(th))         # corrimiento a lo largo de la frontera
D = Dy * np.cos(th)                 # desplazamiento perpendicular al haz = xi/k1
print(f"corrimiento sobre la frontera Dy = xi/(k1 cos th) = 2 tan(th)/gamma = {Dy*1e9:.0f} nm "
      f"(= {2*np.tan(th)/gamma*1e9:.0f} nm)")
print(f"desplazamiento lateral del haz D = Dy cos th = {D*1e9:.0f} nm = {D/lam0:.2f} lambda0")
