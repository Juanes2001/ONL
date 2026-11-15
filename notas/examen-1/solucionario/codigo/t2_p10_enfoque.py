# Problema 10(c) (Saleh Prob. 3.2-7): cintura enfocada W0' y posición z' de la nueva cintura
# en función de la distancia z de la cintura original a la lente (ecs. 3.2-5, 3.2-6, 3.2-9).
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

lam = 488e-9      # m
z0 = 0.50         # m, rango de Rayleigh del haz incidente
f = 0.05          # m, focal de la lente
W0 = np.sqrt(lam * z0 / np.pi)
print("W0 = %.4f mm" % (W0 * 1e3))

z = np.linspace(0, 3.0, 3001)             # m
# (3.2-9) y (3.2-9a): M = Mr/sqrt(1+r^2) = |f|/sqrt((z-f)^2 + z0^2)  (forma sin división por cero en z=f)
M = np.abs(f) / np.sqrt((z - f)**2 + z0**2)
with np.errstate(divide='ignore'):
    Mr = np.abs(f / (z - f))              # aumento de óptica de rayos (3.2-9a)
W0p = M * W0                              # (3.2-5)
zp = f + M**2 * (z - f)                   # (3.2-6)

# límites
W0p_rayos = Mr * W0                       # (3.2-10)/(3.2-12), válido si z-f >> z0
with np.errstate(divide='ignore'):
    zp_rayos = 1 / (1 / f - 1 / z)            # (3.2-11)
W0p_cintura = W0 / np.sqrt(1 + (z0 / f)**2)   # (3.2-13), lente en la cintura
for zz in [0, 0.05, 0.5, 1.0, 3.0]:
    i = np.argmin(np.abs(z - zz))
    print("z = %.2f m: W0' = %.3f um, z' = %.4f cm, M = %.4f" % (z[i], W0p[i] * 1e6, zp[i] * 1e2, M[i]))
print("W0' maximo = %.3f um en z = %.3f m (M_max = f/z0 = %.3f)" % (W0p.max() * 1e6, z[np.argmax(W0p)], f / z0))
print("(3.2-13) con la lente en la cintura: W0' = %.3f um, z' = %.4f cm"
      % (W0p_cintura * 1e6, f / (1 + (f / z0)**2) * 1e2))

fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.6), sharex=True)
a1.plot(z, W0p * 1e6, lw=1.6, label="gaussiano, ec. (3.2-5)")
m = z > 1.2
a1.plot(z[m], W0p_rayos[m] * 1e6, 'k--', lw=1, label='óptica de rayos, (3.2-10)')
a1.axhline(W0p_cintura * 1e6, color='C2', ls=':', label='lente en la cintura, (3.2-13)')
a1.set_ylabel(r"cintura enfocada $W_0'$ ($\mu$m)")
a1.legend(fontsize=8); a1.grid(alpha=0.3)
a2.plot(z, zp * 1e2, lw=1.6, label="gaussiano, ec. (3.2-6)")
a2.plot(z[m], zp_rayos[m] * 1e2, 'k--', lw=1, label='óptica de rayos, (3.2-11)')
a2.axhline(f * 1e2, color='gray', lw=0.6)
a2.set_ylabel(r"distancia lente–cintura $z'$ (cm)")
a2.set_xlabel(r'distancia cintura–lente $z$ (m)')
a2.set_ylim(4.9, 5.5)
a2.legend(fontsize=8); a2.grid(alpha=0.3)
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't2_p10_enfoque')
fig.savefig(base + '.png', dpi=200); fig.savefig(base + '.pdf')
