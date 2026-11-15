# Problema 15 (Saleh Prob. 5.6-1): n, N y D_lambda a partir de la ecuación de Sellmeier (5.5-28)
# con las expresiones analíticas del inciso (a):
#   n^2 = 1 + sum B_i L^2/(L^2 - L_i^2)
#   dn/dL   = -(L/n) sum B_i L_i^2/(L^2-L_i^2)^2
#   N       = n - L dn/dL = n + (L^2/n) sum B_i L_i^2/(L^2-L_i^2)^2              (5.6-2)
#   d2n/dL2 = [ (n^2)'' - 2 (n')^2 ] / (2n),  (n^2)'' = sum B_i L_i^2 (6L^2+2L_i^2)/(L^2-L_i^2)^3
#   D_lambda = -(L/c0) d2n/dL2                                                   (5.6-7)
#   beta2 = beta'' = D_nu/(2 pi) = -(L^2/(2 pi c0)) D_lambda                     (5.6-4)
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq

c0 = 2.998e8
SILICE = dict(L=[0.06840, 0.1162, 9.8962], B=[0.6962, 0.4079, 0.8975])   # Ej. 5.6-1, um
GAAS = dict(L=[0.0, 0.4082, 37.17], B=[3.5, 7.4969, 1.9347])               # Tabla 5.5-1, um

def dispersion(lam_um, mat):
    """Devuelve n, dn/dL [1/um], N, d2n/dL2 [1/um^2], D_lambda [ps/(km nm)] y beta2 [ps^2/km]."""
    L = np.asarray(lam_um, float)
    n2 = 1.0 + sum(B * L**2 / (L**2 - Li**2) for B, Li in zip(mat['B'], mat['L']))
    n = np.sqrt(n2)
    S2 = sum(B * Li**2 / (L**2 - Li**2)**2 for B, Li in zip(mat['B'], mat['L']))
    dn = -(L / n) * S2
    N = n - L * dn
    n2pp = sum(B * Li**2 * (6 * L**2 + 2 * Li**2) / (L**2 - Li**2)**3 for B, Li in zip(mat['B'], mat['L']))
    d2n = (n2pp - 2 * dn**2) / (2 * n)                         # 1/um^2
    # D_lambda = -(L/c0) d2n/dL2  en s/m^2 ; 1 ps/(km nm) = 1e-6 s/m^2
    Dl = -(L * 1e-6 / c0) * (d2n * 1e12) / 1e-6
    beta2 = -((L * 1e-6)**2 / (2 * np.pi * c0)) * (Dl * 1e-6)   # s^2/m
    return n, dn, N, d2n, Dl, beta2 * 1e24 * 1e3                # beta2 en ps^2/km

if __name__ == '__main__':
    # comprobación de las derivadas analíticas con diferencias finitas
    h = 1e-4
    for L0 in [0.8, 1.55]:
        n_p, n_0, n_m = (dispersion(L0 + s * h, SILICE)[0] for s in (1, 0, -1))
        _, dn, _, d2n, _, _ = dispersion(L0, SILICE)
        print("verificacion L=%.2f um: dn/dL analit %.6e vs dif. finitas %.6e ; d2n %.6e vs %.6e"
              % (L0, dn, (n_p - n_m) / (2 * h), d2n, (n_p - 2 * n_0 + n_m) / h**2))

    print("\nSILICE FUNDIDA")
    for L0 in [0.6, 0.8, 1.0, 1.3, 1.55]:
        n, dn, N, d2n, Dl, b2 = dispersion(L0, SILICE)
        print("  L = %.2f um: n = %.5f, N = %.5f, D_lambda = %+8.2f ps/(km nm), beta2 = %+8.2f ps^2/km = %+7.2f fs^2/mm"
              % (L0, n, N, Dl, b2, b2))
    Lzd = brentq(lambda L: dispersion(L, SILICE)[4], 1.1, 1.5)
    print("  cero de dispersion: L_ZD = %.4f um ; N minimo ahi = %.5f" % (Lzd, dispersion(Lzd, SILICE)[2]))

    print("\nGaAs")
    for L0 in [1.5, 2.0, 4.0, 6.0, 10.0]:
        n, dn, N, d2n, Dl, b2 = dispersion(L0, GAAS)
        print("  L = %.2f um: n = %.4f, N = %.4f, D_lambda = %+8.2f ps/(km nm), beta2 = %+9.1f ps^2/km" % (L0, n, N, Dl, b2))
    Lzd_g = brentq(lambda L: dispersion(L, GAAS)[4], 3, 10)
    print("  cero de dispersion: L_ZD = %.3f um ; N ahi = %.4f" % (Lzd_g, dispersion(Lzd_g, GAAS)[2]))

    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')
    for mat, nombre, rango, Lz, archivo in [(SILICE, 'sílice fundida', (0.25, 3.5), Lzd, 't2_p15_silice'),
                                            (GAAS, 'GaAs', (1.5, 10.5), Lzd_g, 't2_p15_gaas')]:
        L = np.linspace(*rango, 2000)
        n, dn, N, d2n, Dl, b2 = dispersion(L, mat)
        fig, ax = plt.subplots(3, 1, figsize=(6.4, 7.0), sharex=True)
        ax[0].plot(L, n, lw=1.6); ax[0].set_ylabel(r'índice $n$')
        ax[1].plot(L, N, lw=1.6, color='C1'); ax[1].set_ylabel(r'índice de grupo $N$')
        ax[2].plot(L, Dl, lw=1.6, color='C2'); ax[2].axhline(0, color='k', lw=0.6)
        ax[2].set_ylabel(r'$D_\lambda$ (ps/(km$\cdot$nm))')
        ax[2].set_xlabel(r'longitud de onda $\lambda_0$ ($\mu$m)')
        if mat is SILICE:
            ax[2].set_ylim(-400, 150)
        else:
            ax[2].set_ylim(-1500, 200)
        for a in ax:
            a.axvline(Lz, color='gray', ls='--', lw=0.8); a.grid(alpha=0.3)
        ax[2].annotate(r'$\lambda_{ZD}=%.3f$ $\mu$m' % Lz, (Lz, 0), xytext=(10, 15), textcoords='offset points', fontsize=8)
        ax[0].set_title(nombre, fontsize=10)
        fig.tight_layout()
        fig.savefig(os.path.join(carpeta, archivo + '.png'), dpi=200)
        fig.savefig(os.path.join(carpeta, archivo + '.pdf'))
