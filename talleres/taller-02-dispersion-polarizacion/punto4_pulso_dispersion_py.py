"""Réplica en Python de punto4_pulso_dispersion.m (mismo algoritmo, mismos nombres de figura).

Sirve para generar las figuras cuando MATLAB no está disponible (licencia) y como control
cruzado del script de MATLAB, que es el entregable del punto 4.
  python punto4_pulso_dispersion_py.py      (requiere numpy y matplotlib)
Sobrescribe las figuras de MATLAB si se ejecuta: el documento usa las del .m.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

c0 = 299792458.0
AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(AQUI, "figuras")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": 0.3})


def guardar(fig, nombre):
    fig.savefig(os.path.join(OUT, nombre + ".png"), dpi=170, bbox_inches="tight")
    fig.savefig(os.path.join(OUT, nombre + ".pdf"), bbox_inches="tight")
    plt.close(fig)


def dispersion_silice(lam):
    """n, N, D_lambda [s/m^2], D_nu [s^2/m] de la sílice fundida (Sellmeier, tabla 5.5-1). lam en m."""
    B = np.array([0.6962, 0.4079, 0.8975]); L = np.array([0.06840, 0.1162, 9.8962]) * 1e-6
    nf = lambda l: np.sqrt(1 + sum(b * l**2 / (l**2 - li**2) for b, li in zip(B, L)))
    h = 1e-10
    n = nf(lam); dn = (nf(lam + h) - nf(lam - h)) / (2 * h); d2 = (nf(lam + h) - 2 * n + nf(lam - h)) / h**2
    N = n - lam * dn
    Dlam = -(lam / c0) * d2
    Dnu = -Dlam * lam**2 / c0
    return n, N, Dlam, Dnu


def semianchura_1e(t, a):
    a = a / a.max(); i0 = np.where(a >= np.exp(-1))[0][-1]
    tc = np.interp(np.exp(-1), [a[i0 + 1], a[i0]], [t[i0 + 1], t[i0]])
    return tc - t[np.argmax(a)]


# ------------------------------------------------------------------ Fig. 5.6-5
lam = np.linspace(0.6, 1.6, 601) * 1e-6
n, N, Dlam, _ = dispersion_silice(lam)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(7, 6.2), sharex=True)
a1.plot(lam * 1e6, n, "k", label="$n = c_0/c$"); a1.plot(lam * 1e6, N, "b", label="$N = c_0/v$ (índice de grupo)")
a1.set_ylabel("Índice de refracción"); a1.legend(loc="upper right")
a1.set_title("Sílice fundida: Sellmeier (tabla 5.5-1 de Saleh y Teich)")
a2.plot(lam * 1e6, Dlam * 1e6, "r"); a2.axhline(0, color="k", ls=":")
for l in [0.8, 1.312, 1.55]:
    _, _, D, _ = dispersion_silice(l * 1e-6)
    a2.plot(l, D * 1e6, "ko")
    if l > 1.5:
        a2.text(l - 0.02, D * 1e6, f"{l:g} µm: {D*1e6:.1f}", fontsize=9, ha="right", va="bottom")
    else:
        a2.text(l + 0.02, D * 1e6, f"{l:g} µm: {D*1e6:.1f}", fontsize=9, va="top")
a2.set_xlabel("Longitud de onda $\\lambda_0$ (µm)"); a2.set_ylabel("$D_\\lambda$ (ps/(km·nm))")
a2.text(0.65, 15, "dispersión anómala ($D_\\lambda>0$)", color="0.3"); a2.text(1.0, -100, "dispersión normal ($D_\\lambda<0$)", color="0.3")
fig.tight_layout(); guardar(fig, "punto3_fig_5_6_5")

print(f"{'lam(um)':<8}{'n':<10}{'N':<10}{'Dlam(ps/km/nm)':<17}{'Dnu(s^2/m)':<14}")
for l in [0.8, 1.312, 1.55]:
    n1, N1, D1, Dnu1 = dispersion_silice(l * 1e-6)
    print(f"{l:<8.3f}{n1:<10.5f}{N1:<10.5f}{D1*1e6:<17.2f}{Dnu1:<14.3e}")

# --------------------------------------------------------------- punto 4
casos = [("a", 10e-12, 0.8e-6), ("b", 10e-12, 1.55e-6), ("c", 1e-12, 0.8e-6), ("d", 1e-12, 1.55e-6)]
zs = np.array([0, 0.2, 0.4, 0.6, 1.0]) * 1e3
col = ["k", "C0", "C1", "C2", "C4"]
figA, axA = plt.subplots(figsize=(7.6, 5.2))
print(f"\n{'caso':<5}{'tau0(ps)':<10}{'lam(um)':<9}{'Dnu(s^2/m)':<13}{'z0(km)':<9}| tau(z) numérico / analítico (ps)")
for k, (etq, tau0, lam0) in enumerate(casos):
    _, _, Dl0, Dnu = dispersion_silice(lam0)
    z0 = np.pi * tau0**2 / abs(Dnu)
    tau_an = tau0 * np.sqrt(1 + (zs / z0) ** 2)
    T = 24 * tau_an[-1]; Nt = 2**16; dt = T / Nt
    t = (np.arange(Nt) - Nt // 2) * dt
    nu = (np.arange(Nt) - Nt // 2) / (Nt * dt)
    A0 = np.exp(-t**2 / tau0**2)
    A0f = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(A0)))
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    tau_num = np.zeros_like(zs)
    for m, z in enumerate(zs):
        H = np.exp(-1j * np.pi * Dnu * nu**2 * z)
        A = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(H * A0f)))
        s = slice(0, Nt, 4)
        ax.plot(t[s] * 1e12, np.abs(A[s]), color=col[m], lw=1.4, label=f"z = {z/1e3:.1f} km")
        tau_num[m] = semianchura_1e(t, np.abs(A))
    ax.set_xlim(-3.2 * tau_an[-1] * 1e12, 3.2 * tau_an[-1] * 1e12)
    ax.set_xlabel("t (ps)"); ax.set_ylabel("|A(z,t)| (u.a.)")
    ax.set_title(f"({etq})  $\\tau_0$ = {tau0*1e12:g} ps,  $\\lambda_0$ = {lam0*1e6:.2f} µm,  "
                 f"$D_\\lambda$ = {Dl0*1e6:.1f} ps/(km·nm),  $z_0$ = {z0/1e3:.3g} km", fontsize=9)
    ax.legend(loc="upper right"); fig.tight_layout(); guardar(fig, f"punto4_caso_{etq}")
    print(f"{etq:<5}{tau0*1e12:<10g}{lam0*1e6:<9.2f}{Dnu:<13.3e}{z0/1e3:<9.3f}| "
          + "  ".join(f"{a*1e12:.2f}/{b*1e12:.2f}" for a, b in zip(tau_num, tau_an)))
    zz = np.linspace(0, 1e3, 200)
    axA.plot(zz / 1e3, tau0 * np.sqrt(1 + (zz / z0) ** 2) * 1e12, "-", color=f"C{k}", lw=1.3,
             label=f"({etq}) analítico: $\\tau_0[1+(z/z_0)^2]^{{1/2}}$")
    axA.plot(zs / 1e3, tau_num * 1e12, "o", color=f"C{k}", label=f"({etq}) numérico (FFT)")
axA.set_yscale("log"); axA.set_xlabel("z (km)"); axA.set_ylabel("$\\tau(z)$: semianchura a 1/e de |A| (ps)")
axA.set_title("Ensanchamiento del pulso gaussiano: método FFT frente a la solución analítica")
axA.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=8)
figA.tight_layout(); guardar(figA, "punto4_anchos")
print("figuras escritas en", OUT)
