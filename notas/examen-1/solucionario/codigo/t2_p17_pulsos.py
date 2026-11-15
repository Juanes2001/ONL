# Problema 17: pulsos gaussianos en medios dispersivos (Saleh §5.6 y §22.3, Tabla 22.3-1).
# Convención de Saleh: U = A(t) exp(j 2 pi nu0 t), F{f}(nu) = int f(t) exp(-j 2 pi nu t) dt
# (la misma que numpy.fft.fft), función de transferencia de la envolvente
#   H_e(f) = exp(-j pi D_nu f^2 z)   [ec. 22.3-3 con b = D_nu z/pi, sin el retardo de grupo].
# tau es la constante de 1/e de la AMPLITUD: tau_FWHM = sqrt(2 ln 2) tau = 1.177 tau (22.1-8).
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from t2_p15_sellmeier import dispersion, SILICE

c0 = 2.998e8
K = np.sqrt(2 * np.log(2))               # tau_FWHM / tau
carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')

def fwhm(t, y):
    """Anchura total a media altura de y(t) con interpolación lineal en los flancos."""
    y = y / y.max(); i = np.where(y >= 0.5)[0]; i0, i1 = i[0], i[-1]
    tl = np.interp(0.5, [y[i0 - 1], y[i0]], [t[i0 - 1], t[i0]])
    tr = np.interp(0.5, [y[i1 + 1], y[i1]], [t[i1 + 1], t[i1]])
    return tr - tl

def propagar(A0, t, Dnu, z):
    """A(z,t) = F^-1{ exp(-j pi D_nu f^2 z) F{A(0,t)} } (marco que viaja a la velocidad de grupo)."""
    f = np.fft.fftfreq(t.size, t[1] - t[0])
    return np.fft.ifft(np.exp(-1j * np.pi * Dnu * f**2 * z) * np.fft.fft(A0))

# ---------------------------------------------------------------- (a) 800 nm, 1 cm de sílice
lam0 = 0.8
n, dn, N, d2n, Dl, b2 = dispersion(lam0, SILICE)
L = 1e-2                                   # m
beta2 = b2 * 1e-24 / 1e3                   # s^2/m  (b2 viene en ps^2/km)
Dnu = 2 * np.pi * beta2                    # (5.6-4)
print("(a) lambda = 0.8 um: n = %.5f, N = %.5f, retardo de grupo N L/c0 = %.3f ps"
      % (n, N, N * L / c0 * 1e12))
print("    beta'' = %.2f fs^2/mm, D_nu = 2 pi beta'' = %.4e s^2/m = %.1f fs^2/mm, D_lambda = %.1f ps/(km nm)"
      % (beta2 * 1e30 / 1e3, Dnu, Dnu * 1e30 / 1e3, Dl))
for TF in [100e-15, 20e-15]:
    tau0 = TF / K
    z0 = np.pi * tau0**2 / Dnu                       # (22.3-12)
    TFout = TF * np.sqrt(1 + (L / z0)**2)            # (22.3-10)
    # verificación por FFT (inciso d)
    t = np.linspace(-40 * TFout, 40 * TFout, 2**14)
    A = propagar(np.exp(-t**2 / tau0**2), t, Dnu, L)
    print("    FWHM_in = %.0f fs: tau0 = %.2f fs, z0 = %.3f mm, chirp a(L) = L/z0 = %.3f, "
          "FWHM_out analitico = %.2f fs, FFT = %.2f fs"
          % (TF * 1e15, tau0 * 1e15, z0 * 1e3, L / z0, TFout * 1e15, fwhm(t, abs(A)**2) * 1e15))

# figura: pulso de 20 fs antes y después, con frecuencia instantánea (inciso c)
TF = 20e-15; tau0 = TF / K
t = np.linspace(-400e-15, 400e-15, 2**14)
A0 = np.exp(-t**2 / tau0**2)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.4), sharex=True)
for Dsign, nombre, col in [(+1, r'normal ($D_\nu>0$)', 'C0'), (-1, r'anómala ($D_\nu<0$)', 'C3')]:
    A = propagar(A0, t, Dsign * Dnu, L)
    I = abs(A)**2
    fase = np.unwrap(np.angle(A))
    nui = np.gradient(fase, t) / (2 * np.pi)              # nu_i - nu0  (22.1-4)
    a1.plot(t * 1e15, I / I.max(), color=col, lw=1.4, label='tras 1 cm, dispersión ' + nombre)
    m = I > 0.02 * I.max()
    a2.plot(t[m] * 1e15, nui[m] / 1e12, color=col, lw=1.4, label=nombre)
a1.plot(t * 1e15, abs(A0)**2, 'k--', lw=1, label='entrada (20 fs FWHM)')
a1.set_ylabel(r'intensidad $|A|^2$ (norm.)'); a1.legend(fontsize=7); a1.grid(alpha=0.3)
a2.axhline(0, color='k', lw=0.6)
a2.set_ylabel(r'$\nu_i-\nu_0$ (THz)'); a2.set_xlabel(r'tiempo retardado $t-z/v$ (fs)')
a2.legend(fontsize=8); a2.grid(alpha=0.3); a2.set_xlim(-150, 150)
fig.tight_layout()
fig.savefig(os.path.join(carpeta, 't2_p17_chirp.png'), dpi=200)
fig.savefig(os.path.join(carpeta, 't2_p17_chirp.pdf'))

# ---------------------------------------------------------------- (b) fibra a 1.55 um
lam = 1.55e-6
Dl_f = 17e-6                                      # s/m^2  (17 ps/(km nm))
Dnu_f = -(lam**2 / c0) * Dl_f                     # D_nu = -(lambda^2/c0) D_lambda
TF = 10e-12; tau0 = TF / K
z0 = np.pi * tau0**2 / abs(Dnu_f)
print("(b) D_nu = %.4e s^2/m, beta2 = %.2f ps^2/km, tau0 = %.3f ps, |z0| = %.4f km"
      % (Dnu_f, Dnu_f / (2 * np.pi) * 1e24 * 1e3, tau0 * 1e12, z0 / 1e3))
for z in [10e3, 100e3]:
    print("    z = %.0f km: FWHM = %.2f ps" % (z / 1e3, TF * np.sqrt(1 + (z / z0)**2) * 1e12))

# ---------------------------------------------------------------- (d) pulso con chirp inicial
# Unidades adimensionales: tau0 = 1 (constante de la envolvente de entrada), |D_nu| tal que
# z0' = pi tau0^2/|D_nu| = 1 (longitud de dispersión calculada con el ancho de ENTRADA).
tau0 = 1.0; Dabs = np.pi
t = np.linspace(-60, 60, 2**14)
z = np.linspace(0, 1.0, 401)
def barrido(a_enun, Dnu):
    A0 = np.exp(-(1 + 1j * a_enun) * t**2 / tau0**2)       # forma del enunciado
    return np.array([fwhm(t, abs(propagar(A0, t, Dnu, zz))**2) for zz in z]) / (K * tau0)

casos = [(-3, +Dabs, r'enunciado literal $a=-3$ (up-chirp), dispersión normal', 'C0', '-'),
         (-3, -Dabs, r'enunciado literal $a=-3$ (up-chirp), dispersión anómala', 'C3', '--'),
         (+3, +Dabs, r'$a=+3$ en la forma del enunciado (down-chirp), normal', 'C2', ':')]
fig, ax = plt.subplots(figsize=(6.4, 4.0))
for a_en, D, lab, col, ls in casos:
    w = barrido(a_en, D)
    i = np.argmin(w)
    print("(d) a_enunciado = %+d, D_nu %s 0: ancho minimo = %.4f tau0 en z = %.4f z0'  (ancho en z=0: %.4f)"
          % (a_en, '>' if D > 0 else '<', w[i], z[i], w[0]))
    ax.plot(z, w, color=col, ls=ls, lw=1.6, label=lab)
a = 3
print("    analitico: tau_min = tau0/sqrt(1+a^2) = %.4f tau0 ; z_min = |a|/(1+a^2) z0' = %.4f z0'"
      % (1 / np.sqrt(1 + a**2), a / (1 + a**2)))
ax.axhline(1 / np.sqrt(10), color='gray', lw=0.6)
ax.set_xlabel(r"distancia $z/z_0'$, con $z_0'=\pi\tau_0^2/|D_\nu|$")
ax.set_ylabel(r'ancho $\tau(z)/\tau_0$ (FWHM/1.177$\tau_0$)')
ax.legend(fontsize=7); ax.grid(alpha=0.3); ax.set_ylim(0, 3.5)
fig.tight_layout()
fig.savefig(os.path.join(carpeta, 't2_p17_compresion.png'), dpi=200)
fig.savefig(os.path.join(carpeta, 't2_p17_compresion.pdf'))
