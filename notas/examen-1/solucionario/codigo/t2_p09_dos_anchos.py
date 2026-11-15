# Problema 9 (Saleh Prob. 3.1-7): identificar un haz gaussiano a partir de dos anchos.
# Incógnitas: z1 (posición del primer plano medida desde la cintura) y W0.
#   W1^2 = W0^2 [1 + (z1/z0)^2],  W2^2 = W0^2 [1 + ((z1+d)/z0)^2],  z0 = pi W0^2 / lambda
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

lam = 10.6e-6          # m
W1, W2 = 1.699e-3, 3.380e-3   # m
d = 0.10               # m
b = (lam / np.pi)**2   # (lambda/pi)^2, m^2

# --- Solución analítica: cuadrática en a = W0^2 ---
Delta = W2**2 - W1**2
A = 1 + Delta**2 / (4 * b * d**2)
B = W1**2 + Delta / 2
C = b * d**2 / 4
disc = B**2 - 4 * A * C
raices = [(B + s * np.sqrt(disc)) / (2 * A) for s in (+1, -1)]
print("Cuadratica  A a^2 - B a + C = 0:  A=%.4f  B=%.4e m^2  C=%.4e m^4" % (A, B, C))
sols = []
for a in raices:
    W0 = np.sqrt(a)
    z1 = (a * Delta / b - d**2) / (2 * d)
    z0 = np.pi * a / lam
    W = lambda z: W0 * np.sqrt(1 + (z / z0)**2)
    sols.append((W0, z1, z0))
    print("W0 = %.4f mm, z0 = %.4f cm, z1 = %+.3f cm, z2 = z1+d = %+.3f cm | "
          "comprobacion W(z1) = %.4f mm, W(z2) = %.4f mm"
          % (W0 * 1e3, z0 * 1e2, z1 * 1e2, (z1 + d) * 1e2, W(z1) * 1e3, W(z1 + d) * 1e3))

# --- Solución numérica con fsolve desde varios puntos de partida ---
def residuo(x):
    W0, z1 = x[0] * 1e-3, x[1] * 1e-2          # mm, cm -> m
    z0 = np.pi * W0**2 / lam
    return [W0 * np.sqrt(1 + (z1 / z0)**2) / W1 - 1,
            W0 * np.sqrt(1 + ((z1 + d) / z0)**2) / W2 - 1]

encontradas = set()
for W0g in [0.03, 0.05, 0.1, 0.2, 0.4, 1.0]:
    for z1g in [-8, -4, 0, 4, 8, 15]:
        x, info, ier, msg = fsolve(residuo, [W0g, z1g], full_output=True)
        if ier == 1 and np.max(np.abs(residuo(x))) < 1e-10 and x[0] > 0:
            encontradas.add((round(abs(x[0]), 4), round(x[1], 3)))
print("fsolve (W0 [mm], z1 [cm]) distintas encontradas:", sorted(encontradas))

# --- Figura: W(z) de las dos soluciones y los dos planos de medida ---
fig, ax = plt.subplots(figsize=(6.4, 3.8))
z = np.linspace(-0.15, 0.25, 800)
estilos = ['-', '--']
for (W0, z1, z0), ls in zip(sols, estilos):
    zz = z - z1               # coordenada medida desde la cintura; plano 1 en z=0 del eje del dibujo
    Wz = W0 * np.sqrt(1 + (zz / z0)**2)
    ax.plot(z * 1e2, Wz * 1e3, ls, lw=1.6,
            label=r'$W_0=%.3f$ mm, cintura en $%.2f$ cm' % (W0 * 1e3, -z1 * 1e2))
ax.plot([0, d * 1e2], [W1 * 1e3, W2 * 1e3], 'ko', label='anchos medidos')
ax.axvline(0, color='gray', lw=0.6); ax.axvline(d * 1e2, color='gray', lw=0.6)
ax.set_xlabel(r'posición axial $z$ (cm), plano 1 en $z=0$')
ax.set_ylabel(r'radio del haz $W(z)$ (mm)')
ax.set_ylim(0, 6)
ax.legend(fontsize=8, loc='upper left')
ax.grid(alpha=0.3)
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't2_p09_dos_anchos')
fig.savefig(base + '.png', dpi=200); fig.savefig(base + '.pdf')
