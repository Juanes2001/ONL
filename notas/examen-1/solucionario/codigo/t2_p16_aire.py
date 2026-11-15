# Problema 16(a) (Saleh Prob. 5.6-2): índice del aire. Ajuste parabólico de n-1 en lambda,
# índice de grupo N = n - lambda dn/dlambda (5.6-2), velocidad de grupo v = c0/N y
# D_lambda = -(lambda/c0) d2n/dlambda2 (5.6-7).
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

c0 = 2.998e8
lam = np.array([0.76, 0.81, 0.86])                 # um
dn = np.array([2.672, 2.669, 2.665]) * 1e-4       # n - 1
# parábola exacta por los tres puntos, centrada en 0.81 um: n-1 = a0 + a1 x + a2 x^2, x = lam - 0.81
x = lam - 0.81
a2, a1, a0 = np.polyfit(x, dn, 2)
print("ajuste: n-1 = %.4e %+.4e x %+.4e x^2  (x = lambda - 0.81 um, en um)" % (a0, a1, a2))
print("dn/dlambda(0.81) = %.3e 1/um ; d2n/dlambda2 = %.3e 1/um^2" % (a1, 2 * a2))

def N_de(L):
    xx = L - 0.81
    n = 1 + a0 + a1 * xx + a2 * xx**2
    dndl = a1 + 2 * a2 * xx
    return n, n - L * dndl

for L in [0.76, 0.81, 0.86]:
    n, N = N_de(L)
    Dl = -(L * 1e-6 / c0) * (2 * a2 * 1e12) / 1e-6       # ps/(km nm)
    print("lambda = %.2f um: n = %.7f, N = %.7f, N-n = %.2e, v = c0/N = %.6e m/s, D_lambda = %+.4f ps/(km nm)"
          % (L, n, N, N - n, c0 / N, Dl))
print("razon |D_fibra(1.55 um)|/D_aire = %.0f (D_fibra = 21.9 ps/(km nm))"
      % (21.9 / (-(0.81e-6 / c0) * (2 * a2 * 1e12) / 1e-6)))

L = np.linspace(0.74, 0.88, 200)
n, N = N_de(L)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(L, (n - 1) * 1e4, lw=1.6, label=r'$n-1$ (ajuste)')
ax.plot(lam, dn * 1e4, 'ko', label='datos medidos')
ax.plot(L, (N - 1) * 1e4, '--', lw=1.6, label=r'$N-1$')
ax.set_xlabel(r'longitud de onda $\lambda_0$ ($\mu$m)')
ax.set_ylabel(r'$(n-1)$, $(N-1)$ ($\times10^{-4}$)')
ax.legend(fontsize=8); ax.grid(alpha=0.3)
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't2_p16_aire')
fig.savefig(base + '.png', dpi=200); fig.savefig(base + '.pdf')
