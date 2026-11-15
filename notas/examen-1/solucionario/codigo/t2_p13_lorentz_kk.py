# Problema 13: medio de Lorentz (Saleh §5.5C), Kramers-Kronig numérico (ec. 5.5-13) e índice
# de grupo (ec. 5.6-2). Convención de Saleh: chi = chi' + j chi'', chi'' < 0 = absorción.
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad

c0 = 2.998e8
chi0, nu0, dnu = 1e-4, 500.0, 5.0        # frecuencias en THz
n0 = 1.0
carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')

def chi(nu):                                     # (5.5-19)
    return chi0 * nu0**2 / (nu0**2 - nu**2 + 1j * nu * dnu)
def chi1(nu): return chi(nu).real                # (5.5-20)
def chi2(nu): return chi(nu).imag                # (5.5-21)

nu = np.linspace(400, 600, 4001)
X = chi(nu)
# índice y absorción "exactos" con (5.5-5) (huésped n0 = 1) y diluidos con (5.5-26), (5.5-27)
r = np.sqrt(1 + X)
n_ex = r.real
alpha_ex = -2 * (2 * np.pi * nu * 1e12 / c0) * r.imag      # 1/m
n_dil = n0 + X.real / (2 * n0)
alpha_dil = -(2 * np.pi * nu * 1e12 / (n0 * c0)) * X.imag

print("(b) Q = nu0/dnu = %.0f ; -chi''(nu0) = chi0 Q = %.3e" % (nu0 / dnu, -chi2(nu0)))
print("    alpha(nu0) exacto = %.4e 1/m, diluido = %.4e 1/m" % (alpha_ex[np.argmin(abs(nu - nu0))], alpha_dil[np.argmin(abs(nu - nu0))]))
print("    max(n-1) = %.4e en %.2f THz ; min(n-1) = %.4e en %.2f THz"
      % ((n_ex - 1).max(), nu[np.argmax(n_ex)], (n_ex - 1).min(), nu[np.argmin(n_ex)]))
print("    FWHM de alpha (numerico) = %.3f THz"
      % (np.ptp(nu[alpha_ex >= alpha_ex.max() / 2])))

fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.4), sharex=True)
a1.plot(nu, (n_ex - 1) * 1e3, lw=1.6, label='exacto, (5.5-5)')
a1.plot(nu, (n_dil - 1) * 1e3, '--', lw=1, label='diluido, (5.5-27)')
a1.set_ylabel(r'$n(\nu)-1$ ($\times10^{-3}$)')
a1.legend(fontsize=8); a1.grid(alpha=0.3)
a2.plot(nu, alpha_ex * 1e-2, lw=1.6, label='exacto, (5.5-5)')
a2.plot(nu, alpha_dil * 1e-2, '--', lw=1, label='diluido, (5.5-26)')
a2.set_ylabel(r'$\alpha(\nu)$ (cm$^{-1}$)')
a2.set_xlabel(r'frecuencia $\nu$ (THz)')
a2.legend(fontsize=8); a2.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(carpeta, 't2_p13_n_alpha.png'), dpi=200)
fig.savefig(os.path.join(carpeta, 't2_p13_n_alpha.pdf'))

# ---------------- (c) Kramers-Kronig: chi'(nu) = (2/pi) VP int_0^inf s chi''(s)/(s^2-nu^2) ds
def kk(v, s_min=0.0, s_max=np.inf, ancho=40.0, signo=-1):
    """chi'(v) por Kramers-Kronig. Con signo=+1 es (5.5-13) tal como está impresa; con
    signo=-1 es la forma correcta para la convención de Saleh (chi''<0 = absorción):
        chi'(v) = -(2/pi) VP int s chi''(s)/(s^2 - v^2) ds.
    El polo s = v se trata con quad(weight='cauchy'), que calcula VP int f(s)/(s-v) ds;
    para eso se escribe s chi''/(s^2-v^2) = [s chi''/(s+v)] / (s-v)."""
    f = lambda s: s * chi2(s) / (s + v)
    g = lambda s: s * chi2(s) / (s**2 - v**2)
    def tramo(lo, hi):                      # integral ordinaria de g, sin polo en (lo, hi)
        if hi <= lo:
            return 0.0
        if np.isinf(hi):
            corte = max(lo, 2 * nu0)
            return tramo(lo, corte) + quad(g, corte, np.inf, limit=500)[0]
        pts = [nu0] if lo < nu0 < hi else None
        return quad(g, lo, hi, points=pts, limit=500)[0]
    if s_min < v < s_max:                   # el polo está dentro del intervalo: valor principal
        a, b = max(s_min, v - ancho), min(s_max, v + ancho)
        tot = tramo(s_min, a) + quad(f, a, b, weight='cauchy', wvar=v, limit=500)[0] + tramo(b, s_max)
    else:
        tot = tramo(s_min, s_max)
    return signo * 2 / np.pi * tot

print("(c) (5.5-13) impresa (signo +) en nu = 495 THz: %+.4e ; chi' analitico = %+.4e"
      % (kk(495.0, signo=+1), chi1(495.0)))
nu_kk = np.linspace(400, 600, 401)
chi1_kk = np.array([kk(v) for v in nu_kk])
chi1_tr = np.array([kk(v, nu0 - 3 * dnu, nu0 + 3 * dnu) for v in nu_kk])   # truncada en +-3 dnu
chi1_an = chi1(nu_kk)
err = np.max(np.abs(chi1_kk - chi1_an)) / np.max(np.abs(chi1_an))
print("    KK completa (signo corregido): error maximo relativo (a max|chi'|) = %.2e" % err)
i400 = 0; i500 = np.argmin(abs(nu_kk - 500)); i495 = np.argmin(abs(nu_kk - 495)); i600 = -1
for i in [i400, i495, i500, i600]:
    print("    nu = %.1f THz: chi' analitico = %+.4e, KK completa = %+.4e, KK truncada +-3dnu = %+.4e"
          % (nu_kk[i], chi1_an[i], chi1_kk[i], chi1_tr[i]))
lejos = np.abs(np.abs(nu_kk - nu0) - 3 * dnu) > 1.0      # se excluyen los bordes de truncación
print("    truncada: en los bordes nu0 +- 3dnu la integral diverge (logaritmo), chi'(485) = %s"
      % chi1_tr[np.argmin(abs(nu_kk - 485))])
print("    truncada: error maximo relativo (lejos de los bordes) = %.3f ; fraccion del area de chi'' dentro de +-3dnu = %.3f"
      % (np.max(np.abs(chi1_tr - chi1_an)[lejos]) / np.max(np.abs(chi1_an)), 2 / np.pi * np.arctan(6)))
print("    limite de baja frecuencia: KK completa chi'(1 THz) = %.4e (chi0 = %.1e), truncada = %.4e"
      % (kk(1.0), chi0, kk(1.0, nu0 - 3 * dnu, nu0 + 3 * dnu)))

fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.4), sharex=True, gridspec_kw={'height_ratios': [2, 1]})
a1.plot(nu_kk, chi1_an * 1e3, lw=2.2, color='0.7', label=r"$\chi'$ analítica (5.5-20)")
a1.plot(nu_kk, chi1_kk * 1e3, '--', lw=1.2, color='C0', label=r"KK numérica, $0<s<\infty$")
a1.plot(nu_kk[lejos], chi1_tr[lejos] * 1e3, ':', lw=1.4, color='C3', label=r"KK truncada, $|s-\nu_0|<3\Delta\nu$")
a1.plot(nu_kk, -chi2(nu_kk) * 1e3 / 2, lw=0.8, color='C2', label=r"$-\chi''/2$ (referencia)")
a1.set_ylabel(r"$\chi'(\nu)$ ($\times10^{-3}$)")
a1.legend(fontsize=8); a1.grid(alpha=0.3)
a2.semilogy(nu_kk, np.abs(chi1_kk - chi1_an), lw=1.2, label='completa')
a2.semilogy(nu_kk[lejos], np.abs(chi1_tr - chi1_an)[lejos], lw=1.2, color='C3', label='truncada')
a2.set_ylabel(r"$|\chi'_{KK}-\chi'|$")
a2.set_xlabel(r'frecuencia $\nu$ (THz)')
a2.legend(fontsize=8); a2.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(carpeta, 't2_p13_kk.png'), dpi=200)
fig.savefig(os.path.join(carpeta, 't2_p13_kk.pdf'))

# ---------------- (d) índice de grupo N = n - lambda dn/dlambda = n + nu dn/dnu
dn_dnu = np.gradient(n_ex, nu)
N = n_ex + nu * dn_dnu
print("(d) N(nu0) = %.4f ; N min = %.4f en %.2f THz ; N max = %.4f en %.2f THz"
      % (N[np.argmin(abs(nu - nu0))], N.min(), nu[np.argmin(N)], N.max(), nu[np.argmax(N)]))
rap = nu[N < 1]
print("    N < 1 (luz rapida) entre %.2f y %.2f THz ; N < 0 entre %s" %
      (rap.min(), rap.max(), ("%.2f y %.2f THz" % (nu[N < 0].min(), nu[N < 0].max())) if np.any(N < 0) else "ninguna"))
print("    alpha en el borde de la zona rapida: alpha(%.2f THz) = %.3e 1/m -> 1/alpha = %.1f um"
      % (rap.min(), alpha_ex[nu == rap.min()][0], 1e6 / alpha_ex[nu == rap.min()][0]))

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(nu, N, lw=1.6, label=r'$N(\nu)=n+\nu\,dn/d\nu$')
ax.axhline(1, color='k', lw=0.6); ax.axhline(0, color='gray', lw=0.6, ls='--')
ax.fill_between(nu, N.min() - 0.1, N.max() + 0.1, where=N < 1, color='C3', alpha=0.12, label=r'luz rápida ($N<1$)')
ax.set_ylim(N.min() - 0.1, N.max() + 0.1)
ax.set_xlim(470, 530)
ax.set_xlabel(r'frecuencia $\nu$ (THz)'); ax.set_ylabel(r'índice de grupo $N$ (adim.)')
ax.legend(fontsize=8); ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(carpeta, 't2_p13_grupo.png'), dpi=200)
fig.savefig(os.path.join(carpeta, 't2_p13_grupo.pdf'))
