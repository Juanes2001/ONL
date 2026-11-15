# Problema 11: fase de Gouy del haz gaussiano (Saleh §3.1B, ec. 3.1-10 y 3.1-24) y
# frecuencias de un resonador con modos Hermite-Gauss (Saleh Prob. 3.3-4, ec. 10.2-33).
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

u = np.linspace(-5, 5, 1001)        # z/z0
zeta = np.arctan(u)                 # (3.1-10)
# fase en el eje phi(0,z) = kz - zeta(z)  (3.1-24); menos la onda plana kz queda -zeta(z)
dphi = -zeta

print("zeta(-5z0) = %+.4f rad, zeta(+5z0) = %+.4f rad, salto en [-5z0,5z0] = %.4f rad = %.3f pi"
      % (zeta[0], zeta[-1], zeta[-1] - zeta[0], (zeta[-1] - zeta[0]) / np.pi))
print("zeta(z0) = %.4f rad = pi/4 ; salto total (-inf,+inf) = pi" % np.arctan(1))

fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot(u, zeta / np.pi, lw=1.6, label=r'$\zeta(z)=\tan^{-1}(z/z_0)$')
ax.plot(u, dphi / np.pi, '--', lw=1.6, label=r'$\varphi(0,z)-kz=-\zeta(z)$')
for l, m_ in [(1, 0), (1, 1)]:
    ax.plot(u, -(l + m_ + 1) * zeta / np.pi, ':', lw=1.2,
            label=r'HG$_{%d%d}$: $-(l+m+1)\zeta$' % (l, m_))
ax.axhline(0.5, color='gray', lw=0.5); ax.axhline(-0.5, color='gray', lw=0.5)
ax.set_xlabel(r'posición axial $z/z_0$ (adimensional)')
ax.set_ylabel(r'fase / $\pi$ (rad/$\pi$)')
ax.legend(fontsize=8, loc='lower left'); ax.grid(alpha=0.3)
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't2_p11_gouy')
fig.savefig(base + '.png', dpi=200); fig.savefig(base + '.pdf')

# --- (c) Prob. 3.3-4: espejos en z = +-z0, z0 = 30 cm, banda 1e14 +- 2e9 Hz ---
c0 = 2.998e8
z0 = 0.30
d = 2 * z0
nuF = c0 / (2 * d)
dzeta = np.arctan(1) - np.arctan(-1)       # = pi/2
print("nu_F = c/2d = %.2f MHz, Delta zeta = %.4f rad = pi/2" % (nuF / 1e6, dzeta))
# condición: k*2z0 - (l+m+1)*dzeta = q*pi  ->  nu = (nuF)(q + (l+m+1)/2)  -> multiplos de nuF/2
paso = nuF / 2
p_min = int(np.ceil((1e14 - 2e9) / paso)); p_max = int(np.floor((1e14 + 2e9) / paso))
print("frecuencias permitidas: p*nuF/2 con p = %d ... %d -> %d frecuencias, separadas %.2f MHz"
      % (p_min, p_max, p_max - p_min + 1, paso / 1e6))
print("(con c0 = 2.998e8 m/s, 1e14 Hz no es multiplo exacto de nuF/2; primera = %.6f GHz)"
      % (p_min * paso / 1e9))
