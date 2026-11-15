# Problema 12: n y alpha a partir de chi (Saleh ec. 5.5-5) en régimen débil y fuerte,
# y medios conductores con el modelo de Drude (ecs. 5.5-38 a 5.5-40). Convención e^{jwt}:
# chi'' < 0 significa absorción.
import numpy as np

c0, eps0, e, me = 2.998e8, 8.854e-12, 1.602e-19, 9.109e-31

def n_alpha_exacto(chi, lam0):
    k0 = 2 * np.pi / lam0
    r = np.sqrt(1 + chi + 0j)
    if r.real < 0:            # raíz del cuarto cuadrante (n>0, alpha>0), Saleh p. 172
        r = -r
    return r.real, -2 * k0 * r.imag

lam0 = 1e-6
k0 = 2 * np.pi / lam0
# (a) absorción débil
chi = 1.25 - 0.01j
n, a = n_alpha_exacto(chi, lam0)
n_d = np.sqrt(1 + chi.real); a_d = -k0 / n_d * chi.imag          # (5.5-7), (5.5-8)
print("(a) exacto: n = %.6f, alpha = %.4e 1/m = %.2f 1/cm = %.1f dB/cm" % (n, a, a / 100, 10 * np.log10(np.e) * a / 100))
print("    debil : n = %.6f, alpha = %.4e 1/m" % (n_d, a_d))
# (b) absorción fuerte
chi = -0.5 - 40j
n, a = n_alpha_exacto(chi, lam0)
n_f = np.sqrt(-chi.imag / 2); a_f = 2 * k0 * np.sqrt(-chi.imag / 2)  # (5.5-11), (5.5-12)
print("(b) exacto: n = %.4f, alpha = %.4e 1/m ; fuerte: n = %.4f, alpha = %.4e 1/m" % (n, a, n_f, a_f))
print("    longitud de penetracion 1/alpha = %.2f nm" % (1e9 / a))

# (c) aluminio, Drude con fondo eps = eps0
N, tau = 1.8e29, 8e-15
wp = np.sqrt(N * e**2 / (eps0 * me))
print("(c) wp = %.4e rad/s, lambda_p = %.2f nm, sigma0 = %.3e S/m" % (wp, 2 * np.pi * c0 / wp * 1e9, eps0 * wp**2 * tau))
for lam in [1.55e-6, 550e-9]:
    w = 2 * np.pi * c0 / lam
    er = 1 + wp**2 * tau / (1j * w * (1 + 1j * w * tau))          # (5.5-38)/eps0 con sigma0 = eps0 wp^2 tau
    n, a = n_alpha_exacto(er - 1, lam)
    print("    lambda = %.0f nm: eps_e/eps0 = %.1f %+.2fj ; n = %.3f, alpha = %.3e 1/m (1/alpha = %.1f nm), wtau = %.1f"
          % (lam * 1e9, er.real, er.imag, n, a, 1e9 / a, w * tau))
    nc = np.sqrt(er + 0j); nc = nc if nc.real >= 0 else -nc
    R = abs((1 - nc) / (1 + nc))**2
    print("      reflectancia normal desde aire R = %.3f" % R)

# (d) Si tipo n: Re eps_e = 0  ->  11.7 = wp^2/w^2 (w tau >> 1)
N = 1e20 * 1e6
wp = np.sqrt(N * e**2 / (eps0 * 0.26 * me))
w = wp / np.sqrt(11.7)
print("(d) wp = %.4e rad/s, w(Re eps=0) = %.4e rad/s, lambda = %.3f um" % (wp, w, 2 * np.pi * c0 / w * 1e6))
