"""Figuras para la explicación «frecuencia instantánea y chirp» (problema 7 del taller de repaso).

Convención de Saleh (e^{+jωt}):  f(t) = exp(-t²/τ²) · exp[j(2πν₀t + b t²)],  E(z,t) = Re{f(t - z/c₀)}.
Parámetros del problema 7: τ = 20 fs, ν₀ = 375 THz, b = 5×10²⁷ s⁻²  ->  a = bτ² = 2.

Transformada: Ã(ν) = ∫ f(t) e^{-j2πνt} dt,  f(t) = ∫ Ã(ν) e^{+j2πνt} dν.
Para el gaussiano con chirp (α = (1 - ja)/τ²):
    Ã(ν) = √(π/α) · exp[-π²(ν-ν₀)²/α]
    |Ã|  ∝ exp[-π²τ²(ν-ν₀)²/(1+a²)],   fase ψ(ν) = -π²τ² a (ν-ν₀)²/(1+a²).

Se ejecuta con el Python de Windows (el que tiene numpy/matplotlib):  python figuras_chirp.py
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figuras")
os.makedirs(OUT, exist_ok=True)

# ── parámetros del problema 7 ────────────────────────────────────────────────
tau = 20e-15            # s
nu0 = 375e12            # Hz
b = 5e27                # s^-2
c0 = 299_792_458.0      # m/s
a = b * tau**2          # parámetro de chirp (=2)

FS, THZ, UM = 1e-15, 1e12, 1e-6

# colores: rojo = baja frecuencia / temprano, verde = centro, azul = alta frecuencia / tarde
C_LOW, C_MID, C_HIGH = "#d64545", "#1baf7a", "#2a78d6"
C_INK, C_MUTED, C_GRID, C_ORANGE = "#12171c", "#79848e", "#dfe5ea", "#eb6834"

plt.rcParams.update({
    "figure.facecolor": "white", "axes.facecolor": "white",
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.titlesize": 11, "axes.titleweight": "semibold", "axes.labelsize": 10.5,
    "axes.edgecolor": "#c8d0d7", "axes.linewidth": 0.9,
    "axes.grid": True, "grid.color": C_GRID, "grid.linewidth": 0.7,
    "xtick.color": C_MUTED, "ytick.color": C_MUTED,
    "legend.frameon": False, "legend.fontsize": 9.5,
})


def save(fig, stem):
    fig.savefig(os.path.join(OUT, stem + ".png"), dpi=200, bbox_inches="tight")
    fig.savefig(os.path.join(OUT, stem + ".pdf"), bbox_inches="tight")
    plt.close(fig)
    print("  figura:", stem)


def f(t, bb=b):
    """Campo complejo del problema 7 (con portadora)."""
    return np.exp(-t**2 / tau**2) * np.exp(1j * (2 * np.pi * nu0 * t + bb * t**2))


def nu_i(t):
    return nu0 + b * t / np.pi


def A_spec(nu):
    """Espectro analítico Ã(ν) del pulso del problema 7."""
    al = (1 - 1j * a) / tau**2
    return np.sqrt(np.pi / al) * np.exp(-np.pi**2 * (nu - nu0)**2 / al)


# ═════════════════════════════════════════════════════════════════════════════
# Fig. 1 — el campo, su frecuencia instantánea y tres ampliaciones
# ═════════════════════════════════════════════════════════════════════════════
def fig01():
    t = np.arange(-60 * FS, 60 * FS, 0.02 * FS)
    env = np.exp(-t**2 / tau**2)
    fig = plt.figure(figsize=(10, 7.6))
    gs = fig.add_gridspec(3, 3, height_ratios=[1.15, 1.0, 1.05], hspace=0.62, wspace=0.28)
    axA = fig.add_subplot(gs[0, :])
    axB = fig.add_subplot(gs[1, :], sharex=axA)
    tcs = [-25 * FS, 0.0, 25 * FS]
    cols = [C_LOW, C_MID, C_HIGH]

    axA.plot(t / FS, np.real(f(t)), color=C_INK, lw=0.7)
    axA.plot(t / FS, env, "--", color=C_MUTED, lw=1.1)
    axA.plot(t / FS, -env, "--", color=C_MUTED, lw=1.1, label="envolvente  ±e$^{-t^2/\\tau^2}$")
    for tc, c in zip(tcs, cols):
        axA.axvspan(tc / FS - 6, tc / FS + 6, color=c, alpha=0.18, lw=0)
    axA.set_ylabel("$\\mathrm{Re}\\{f(t)\\}$  (u. arb.)")
    axA.set_title("(a) El campo del pulso con chirp: la oscilación se acelera hacia la derecha")
    axA.legend(loc="upper left")
    plt.setp(axA.get_xticklabels(), visible=False)

    tt = np.linspace(-60 * FS, 60 * FS, 600)
    axB.plot(tt / FS, nu_i(tt) / THZ, color=C_ORANGE, lw=2)
    axB.axhline(nu0 / THZ, color=C_MUTED, ls="--", lw=1)
    axB.text(-58, nu0 / THZ + 5, "$\\nu_0$ = 375 THz", color=C_MUTED, fontsize=9)
    for tc, c in zip(tcs, cols):
        axB.plot(tc / FS, nu_i(tc) / THZ, "o", color=c, ms=8, zorder=5)
        axB.annotate(f"{nu_i(tc)/THZ:.0f} THz", (tc / FS, nu_i(tc) / THZ),
                     textcoords="offset points", xytext=(6, -14), color=c, fontsize=9.5)
    axB.set_xlabel("$t$ (fs)")
    axB.set_ylabel("$\\nu_i(t)$ (THz)")
    axB.set_title("(b) Frecuencia instantánea  $\\nu_i(t)=\\nu_0+bt/\\pi$  (up-chirp: sube linealmente)")
    axB.set_xlim(-60, 60)

    tz = np.linspace(-6 * FS, 6 * FS, 1500)
    for i, (tc, c) in enumerate(zip(tcs, cols)):
        ax = fig.add_subplot(gs[2, i])
        tw = tc + tz
        ax.plot(tw / FS, np.cos(2 * np.pi * nu0 * tw + b * tw**2), color=c, lw=1.6)
        ax.set_xlabel("$t$ (fs)")
        if i == 0:
            ax.set_ylabel("$\\cos\\,\\phi(t)$")
        ax.set_title(f"(c{i+1}) $t$ = {tc/FS:.0f} fs\n$\\nu_i$ = {nu_i(tc)/THZ:.0f} THz,  $T_i$ = {1e15/nu_i(tc):.2f} fs",
                     fontsize=9.5)
        ax.set_ylim(-1.25, 1.25)
    save(fig, "fig01_campo_y_frecuencia_instantanea")


# ═════════════════════════════════════════════════════════════════════════════
# Fig. 2 y 3 — un pulso como suma de ondas monocromáticas eternas
# ═════════════════════════════════════════════════════════════════════════════
DELTA = 2e12            # separación entre líneas espectrales (Hz): periodo 1/Δ = 500 fs
K = 40                  # líneas a cada lado
ks = np.arange(-K, K + 1)
nuk = nu0 + ks * DELTA
Ak = A_spec(nuk)        # amplitud compleja de cada componente (módulo y fase)


def suma(t, mask):
    """Σ_k Ã(ν_k) Δ e^{j2πν_k t} sobre las componentes seleccionadas."""
    ph = np.exp(1j * 2 * np.pi * np.outer(t, nuk[mask]))
    return ph @ (Ak[mask] * DELTA)


def fig02():
    fig = plt.figure(figsize=(10, 6.6))
    gs = fig.add_gridspec(4, 1, height_ratios=[1.25, 1, 1, 1], hspace=0.95)
    ax = fig.add_subplot(gs[0])
    ax.vlines(nuk / THZ, 0, np.abs(Ak) / np.abs(Ak).max(), color=C_INK, lw=1.4)
    sel = [-15, 0, 15]
    cols = [C_LOW, C_MID, C_HIGH]
    for k, c in zip(sel, cols):
        i = k + K
        ax.vlines(nuk[i] / THZ, 0, np.abs(Ak[i]) / np.abs(Ak).max(), color=c, lw=3.2)
    ax.set_xlabel("$\\nu$ (THz)")
    ax.set_ylabel("$|\\tilde A(\\nu)|$ / máx.")
    ax.set_title("(a) El espectro: cada línea es una onda monocromática (aquí 81 líneas separadas 2 THz)")
    t = np.arange(-40 * FS, 40 * FS, 0.03 * FS)
    for r, (k, c) in enumerate(zip(sel, cols)):
        axr = fig.add_subplot(gs[r + 1])
        axr.plot(t / FS, np.cos(2 * np.pi * nuk[k + K] * t), color=c, lw=0.9)
        axr.set_ylim(-1.3, 1.65)
        axr.set_ylabel("$\\cos(2\\pi\\nu t)$")
        axr.set_title(f"({'bcd'[r]}) Componente de {nuk[k+K]/THZ:.0f} THz: amplitud constante en todo $t$",
                      fontsize=10)
        axr.annotate("", xy=(-39.5, 1.38), xytext=(-33, 1.38), arrowprops=dict(arrowstyle="->", color=C_MUTED))
        axr.annotate("", xy=(39.5, 1.38), xytext=(33, 1.38), arrowprops=dict(arrowstyle="->", color=C_MUTED))
        axr.text(-32, 1.38, "sigue hasta $-\\infty$", color=C_MUTED, fontsize=9, va="center", ha="left")
        axr.text(32, 1.38, "sigue hasta $+\\infty$", color=C_MUTED, fontsize=9, va="center", ha="right")
        if r == 2:
            axr.set_xlabel("$t$ (fs)")
    save(fig, "fig02_componentes_eternas")


def fig03():
    t = np.arange(-100 * FS, 100 * FS, 0.05 * FS)
    casos = [("(a) 1 componente ($\\nu_0$)", np.abs(ks) <= 0, None),
             ("(b) 5 componentes ($\\pm 4$ THz)", np.abs(ks) <= 2, None),
             ("(c) 15 componentes ($\\pm 14$ THz)", np.abs(ks) <= 7, None),
             ("(d) 81 componentes ($\\pm 80$ THz), fases correctas", np.abs(ks) <= K, None),
             ("(e) 81 componentes, mismos módulos pero fases al azar", np.abs(ks) <= K, "rand")]
    fig, axs = plt.subplots(5, 1, figsize=(10, 9.2), sharex=True)
    rng = np.random.default_rng(7)
    for ax, (tit, mask, mode) in zip(axs, casos):
        if mode == "rand":
            ph = np.exp(1j * 2 * np.pi * np.outer(t, nuk[mask]))
            amps = np.abs(Ak[mask]) * np.exp(1j * rng.uniform(0, 2 * np.pi, mask.sum())) * DELTA
            s = ph @ amps
        else:
            s = suma(t, mask)
        ax.plot(t / FS, np.real(s), color=C_INK, lw=0.6)
        ax.plot(t / FS, np.exp(-t**2 / tau**2), "--", color=C_ORANGE, lw=1.0)
        ax.plot(t / FS, -np.exp(-t**2 / tau**2), "--", color=C_ORANGE, lw=1.0)
        ax.set_ylim(-1.2, 1.2)
        ax.set_title(tit, fontsize=10, loc="left")
        ax.set_ylabel("$E(t)$ (u. arb.)")
    axs[-1].set_xlabel("$t$ (fs)")
    axs[0].plot([], [], "--", color=C_ORANGE, label="envolvente del pulso real")
    axs[0].legend(loc="upper right")
    fig.tight_layout()
    save(fig, "fig03_suma_y_localizacion")
    # verificación: con todas las componentes se recupera f(t) en la ventana
    tt = np.linspace(-60 * FS, 60 * FS, 2001)
    err = np.max(np.abs(suma(tt, np.abs(ks) <= K) - f(tt)))
    print(f"  verificación: max|Σ - f(t)| en ±60 fs = {err:.2e} (f(0)=1)")


# ═════════════════════════════════════════════════════════════════════════════
# Fig. 4 — espectro local (espectrograma) y qué significa «domina»
# ═════════════════════════════════════════════════════════════════════════════
def stft(sigma_w):
    """|STFT|² del envolvente en banda base g(t)=exp(-t²/τ²)e^{jbt²} (ventana gaussiana σ_w)."""
    dt = 0.5 * FS
    tg = np.arange(-150 * FS, 150 * FS, dt)
    g = np.exp(-tg**2 / tau**2) * np.exp(1j * b * tg**2)
    nfft = 8192
    dnu = np.fft.fftshift(np.fft.fftfreq(nfft, dt))
    tcs = np.arange(-70 * FS, 70 * FS + 1e-18, 1.0 * FS)
    S = np.empty((len(tcs), nfft))
    for i, tc in enumerate(tcs):
        w = np.exp(-(tg - tc)**2 / (2 * sigma_w**2))
        S[i] = np.abs(np.fft.fftshift(np.fft.fft(g * w, nfft)))**2
    return tcs, dnu, S / S.max()


def fig04():
    wins = [4 * FS, 12 * FS]
    fig = plt.figure(figsize=(10.5, 7.8))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.3, 1], hspace=0.38, wspace=0.22)
    t_mark = [-25 * FS, 0.0, 25 * FS]
    cols = [C_LOW, C_MID, C_HIGH]
    for j, sw in enumerate(wins):
        tcs, dnu, S = stft(sw)
        ax = fig.add_subplot(gs[0, j])
        nu_abs = (nu0 + dnu) / THZ
        ax.grid(False)
        im = ax.pcolormesh(tcs / FS, nu_abs, S.T, cmap="Greys", shading="auto", vmin=0, vmax=1)
        tt = np.linspace(-70 * FS, 70 * FS, 300)
        ax.plot(tt / FS, nu_i(tt) / THZ, color=C_ORANGE, lw=2, label="$\\nu_i(t)=\\nu_0+bt/\\pi$")
        for tm, c in zip(t_mark, cols):
            ax.axvline(tm / FS, color=c, lw=1.2, ls=":")
        ax.set_ylim(255, 495)
        ax.set_xlim(-70, 70)
        ax.set_xlabel("$t$ (fs)")
        if j == 0:
            ax.set_ylabel("$\\nu$ (THz)")
        ax.set_title(f"Espectrograma, ventana $\\sigma_w$ = {sw/FS:.0f} fs", fontsize=10.5)
        ax.legend(loc="upper left")
        axs = fig.add_subplot(gs[1, j])
        for tm, c in zip(t_mark, cols):
            i = int(np.argmin(np.abs(tcs - tm)))
            axs.plot(nu_abs, S[i] / S[i].max(), color=c, lw=1.8, label=f"$t$ = {tm/FS:+.0f} fs")
            axs.axvline(nu_i(tm) / THZ, color=c, ls="--", lw=1)
        axs.set_xlim(255, 495)
        axs.set_xlabel("$\\nu$ (THz)")
        if j == 0:
            axs.set_ylabel("espectro local (norm.)")
        axs.set_title("Espectro de lo que se ve por la ventana (rayas: $\\nu_i$)", fontsize=10)
        axs.legend(loc="upper right", fontsize=8.5)
    save(fig, "fig04_espectro_local")


# ═════════════════════════════════════════════════════════════════════════════
# Fig. 5 — dispersión: pulso sin chirp ensanchado; prueba del filtro pasa-banda
# ═════════════════════════════════════════════════════════════════════════════
def propaga(s, N=2**15, dt=0.25 * FS):
    """Envolvente A(z,t) tras z = s·z₀ en dispersión normal (convención de Saleh):
    Ã(z,ν) = Ã(0,ν) exp(-jπ² τ₀² s ν²)  (ν medida desde ν₀), con z₀ = πτ₀²/|D_ν|."""
    t = (np.arange(N) - N // 2) * dt
    A0 = np.exp(-t**2 / tau**2)
    nu = np.fft.fftfreq(N, dt)
    spec = np.fft.fft(A0) * np.exp(-1j * np.pi**2 * tau**2 * s * nu**2)
    return t, nu, spec, np.fft.ifft(spec)


def fig05():
    s = 4.0
    t, nu, spec, A = propaga(s)
    centros = [-15e12, 0.0, 15e12]
    cols = [C_LOW, C_MID, C_HIGH]
    sig_f = 4e12
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7.4), gridspec_kw=dict(height_ratios=[1, 1.5], hspace=0.42))
    nus = np.linspace(-60e12, 60e12, 800)
    esp = np.exp(-2 * np.pi**2 * tau**2 * nus**2)
    ax1.plot((nu0 + nus) / THZ, esp, color=C_INK, lw=2, label="espectro del pulso $|\\tilde A(\\nu)|^2$")
    for c0_, c in zip(centros, cols):
        ax1.fill_between((nu0 + nus) / THZ, 0, np.exp(-(nus - c0_)**2 / (2 * sig_f**2)), color=c, alpha=0.35, lw=0)
    ax1.set_xlabel("$\\nu$ (THz)")
    ax1.set_ylabel("norm.")
    ax1.set_title("(a) Tres filtros pasa-banda angostos (ancho ~4 THz) sobre el espectro")
    ax1.legend(loc="upper right")

    I_tot = np.abs(A)**2
    ax2.fill_between(t / FS, 0, I_tot / I_tot.max(), color="#c8d0d7", alpha=0.7, label="pulso completo (a $z=4z_0$)")
    for c0_, c in zip(centros, cols):
        H = np.exp(-(nu - c0_)**2 / (2 * sig_f**2) * 1.0)
        out = np.fft.ifft(spec * H)
        I = np.abs(out)**2
        ax2.plot(t / FS, I / I.max(), color=c, lw=2.2,
                 label=f"banda $\\nu_0{c0_/THZ:+.0f}$ THz")
        # centro efectivo de la banda: producto de dos gaussianas (espectro del pulso × filtro)
        sa2 = 1 / (2 * np.pi**2 * tau**2)                 # varianza de |Ã(ν)| (amplitud)
        c_ef = c0_ * sa2 / (sa2 + sig_f**2)
        tg = np.pi * tau**2 * s * c_ef                    # retardo de grupo t_g = π τ₀² s (ν-ν₀)
        ax2.axvline(tg / FS, color=c, ls="--", lw=1.1)
        tpk = t[np.argmax(I)]
        print(f"  filtro {c0_/THZ:+.0f} THz: pico en {tpk/FS:+.1f} fs, t_g predicho {tg/FS:+.1f} fs")
    ax2.set_xlim(-250, 250)
    ax2.set_xlabel("$t$ (fs)")
    ax2.set_ylabel("intensidad (cada curva normalizada a su máx.)")
    ax2.set_title("(b) Intensidad que sale de cada filtro: las bandas bajas salen antes, las altas después")
    ax2.plot([], [], "k--", lw=1.1, label="$t_g$ predicho en el centro efectivo de la banda")
    ax2.legend(loc="upper left")
    save(fig, "fig05_prueba_del_filtro")


# ═════════════════════════════════════════════════════════════════════════════
# Fig. 6 — distribución tiempo-frecuencia exacta (Wigner) del pulso del problema 7
# ═════════════════════════════════════════════════════════════════════════════
def fig06():
    tt = np.linspace(-70 * FS, 70 * FS, 500)
    dn = np.linspace(-110e12, 110e12, 500)
    T, N = np.meshgrid(tt, dn)
    W = np.exp(-2 * T**2 / tau**2) * np.exp(-2 * np.pi**2 * tau**2 * (N - b * T / np.pi)**2)
    W0 = np.exp(-2 * T**2 / tau**2) * np.exp(-2 * np.pi**2 * tau**2 * N**2)     # sin chirp (b=0)
    fig = plt.figure(figsize=(8.8, 7.4))
    gs = fig.add_gridspec(2, 2, width_ratios=[4, 1], height_ratios=[1, 4], hspace=0.05, wspace=0.05)
    ax = fig.add_subplot(gs[1, 0])
    axt = fig.add_subplot(gs[0, 0], sharex=ax)
    axf = fig.add_subplot(gs[1, 1], sharey=ax)
    ax.contourf(T / FS, (nu0 + N) / THZ, W, levels=[0.05, 0.2, 0.4, 0.6, 0.8, 1.0], cmap="Blues")
    ax.contour(T / FS, (nu0 + N) / THZ, W0, levels=[0.5], colors=[C_MUTED], linestyles="--", linewidths=1.5)
    ax.plot([], [], "--", color=C_MUTED, label="mismo pulso sin chirp ($b=0$), nivel 1/2")
    ax.plot(tt / FS, nu_i(tt) / THZ, color=C_ORANGE, lw=2.2, label="$\\nu_i(t)$: frecuencia media dado $t$")
    nu_tg = nu0 + (1 + a**2) / (np.pi * tau**2 * a) * tt
    ax.plot(tt / FS, nu_tg / THZ, color=C_INK, lw=1.6, ls="-.", label="$t_g(\\nu)$: tiempo medio dado $\\nu$")
    ax.set_xlabel("$t$ (fs)")
    ax.set_ylabel("$\\nu$ (THz)")
    ax.set_xlim(-70, 70)
    ax.set_ylim(255, 495)
    ax.legend(loc="upper left", fontsize=8.5)
    axt.plot(tt / FS, np.exp(-2 * tt**2 / tau**2), color=C_INK, lw=1.8)
    axt.set_ylabel("$I(t)$")
    plt.setp(axt.get_xticklabels(), visible=False)
    axt.set_title("Distribución tiempo-frecuencia del pulso del problema 7 ($a=2$)", fontsize=11)
    nus = np.linspace(-110e12, 110e12, 500)
    axf.plot(np.exp(-2 * np.pi**2 * tau**2 * nus**2 / (1 + a**2)), (nu0 + nus) / THZ, color=C_INK, lw=1.8)
    axf.set_xlabel("$|\\tilde A(\\nu)|^2$")
    plt.setp(axf.get_yticklabels(), visible=False)
    save(fig, "fig06_distribucion_tiempo_frecuencia")


# ═════════════════════════════════════════════════════════════════════════════
# Fig. 7 — la misma señal en el tiempo (z fijo) y en el espacio (t fijo)
# ═════════════════════════════════════════════════════════════════════════════
def fig07():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.6), gridspec_kw=dict(hspace=0.55))
    t = np.arange(-50 * FS, 50 * FS, 0.02 * FS)
    ax1.plot(t / FS, np.real(f(t)), color=C_INK, lw=0.7)
    ax1.plot(t / FS, np.exp(-t**2 / tau**2), "--", color=C_MUTED, lw=1)
    ax1.plot(t / FS, -np.exp(-t**2 / tau**2), "--", color=C_MUTED, lw=1)
    ax1.set_xlabel("$t$ (fs)")
    ax1.set_ylabel("$E(z_d,t)$ (u. arb.)")
    ax1.set_title("(a) Un detector fijo en $z_d$ ve pasar el pulso: lo primero que llega es el frente (rojo)")
    ax1.annotate("llega primero\n(frente, $\\nu$ baja)", (-46, 0.62), color=C_LOW, fontsize=10, ha="left")
    ax1.annotate("llega después\n(cola, $\\nu$ alta)", (33, 0.62), color=C_HIGH, fontsize=10, ha="left")
    z = np.arange(-15 * UM, 15 * UM, 0.004 * UM)
    t0 = 0.0
    ax2.plot(z / UM, np.real(f(t0 - z / c0)), color=C_INK, lw=0.7)
    ax2.plot(z / UM, np.exp(-(t0 - z / c0)**2 / tau**2), "--", color=C_MUTED, lw=1)
    ax2.plot(z / UM, -np.exp(-(t0 - z / c0)**2 / tau**2), "--", color=C_MUTED, lw=1)
    ax2.set_xlabel("$z$ ($\\mu$m)")
    ax2.set_ylabel("$E(z,t_0=0)$ (u. arb.)")
    ax2.set_title("(b) Una «foto» del pulso en el espacio ($t_0=0$): el frente está a la derecha y tiene $\\lambda$ larga")
    for zz, c, txt in [(-6 * UM, C_HIGH, "cola: $\\lambda\\approx$ 0.74 $\\mu$m"), (6 * UM, C_LOW, "frente: $\\lambda\\approx$ 0.87 $\\mu$m")]:
        ax2.annotate(txt, (zz / UM * 1.5, 1.12), color=c, fontsize=10, ha="center")
    ax2.annotate("", xy=(14.5, -0.95), xytext=(9, -0.95), arrowprops=dict(arrowstyle="->", color=C_ORANGE, lw=1.8))
    ax2.text(8.7, -0.95, "dirección de propagación", color=C_ORANGE, fontsize=9.5, ha="right", va="center")
    ax2.set_xlim(-15, 15)
    ax2.set_ylim(-1.15, 1.4)
    for zz in (-6e-6, 6e-6):
        tl = t0 - zz / c0
        print(f"  z = {zz/UM:+.0f} µm  <->  t = {tl/FS:+.1f} fs: ν_i = {nu_i(tl)/THZ:.1f} THz, λ = {c0/nu_i(tl)*1e6:.3f} µm")
    save(fig, "fig07_tiempo_y_espacio")


# ═════════════════════════════════════════════════════════════════════════════
# Fig. 8 — la dispersión solo cambia las fases: espectro idéntico, pulso distinto
# ═════════════════════════════════════════════════════════════════════════════
def fig08():
    svals = [0.0, 1.0, 4.0]
    fig, axs = plt.subplots(3, 3, figsize=(10.5, 8.6), gridspec_kw=dict(hspace=0.55, wspace=0.3))
    nus = np.linspace(-70e12, 70e12, 600)
    for j, s in enumerate(svals):
        t, nu, spec, A = propaga(s)
        I = np.abs(A)**2
        ph = np.unwrap(np.angle(A))
        dt = t[1] - t[0]
        nui = np.gradient(ph, dt) / (2 * np.pi)       # desvío respecto a ν0
        mask = I > 0.02 * I.max()
        tau_s = tau * np.sqrt(1 + s**2)
        ax = axs[0, j]
        ax.plot((nu0 + nus) / THZ, np.exp(-2 * np.pi**2 * tau**2 * nus**2), color=C_INK, lw=2)
        ax.set_xlabel("$\\nu$ (THz)")
        ax.set_ylabel("$|\\tilde A(\\nu)|^2$")
        ax.set_title(f"$z={s:g}\\,z_0$" + ("  (entrada)" if s == 0 else ""), fontsize=11)
        ax.text(0.96, 0.88, "idéntico", transform=ax.transAxes, fontsize=9, color=C_MUTED, ha="right")
        ax = axs[1, j]
        ax.plot(t / FS, I / np.abs(propaga(0.0)[3]).max()**2, color=C_ORANGE, lw=2)
        ax.set_xlim(-250, 250)
        ax.set_ylim(0, 1.05)
        ax.set_xlabel("$t$ (fs)")
        ax.set_ylabel("$I(t)/I_{\\rm entrada,máx}$")
        ax.text(0.04, 0.88, f"$\\tau$ = {tau_s/FS:.0f} fs", transform=ax.transAxes, fontsize=9.5, color=C_INK)
        ax = axs[2, j]
        ax.plot(t[mask] / FS, (nu0 + nui[mask]) / THZ, color=C_ORANGE, lw=2, label="numérico")
        m_an = s / (np.pi * tau**2 * (1 + s**2))
        tp = t[mask]
        ax.plot(tp / FS, (nu0 + m_an * tp) / THZ, "k--", lw=1, label="analítico")
        ax.axhline(nu0 / THZ, color=C_MUTED, ls=":", lw=1)
        ax.set_xlim(-250, 250)
        ax.set_ylim(335, 415)
        ax.set_xlabel("$t$ (fs)")
        ax.set_ylabel("$\\nu_i(t)$ (THz)")
        if j == 2:
            ax.legend(loc="upper left", fontsize=8.5)
        if mask.sum() > 5:
            err = np.max(np.abs(nui[mask] - m_an * t[mask])) / THZ
            print(f"  z = {s:g} z0: pendiente analítica {m_an*FS/THZ*1e3:.1f} GHz/fs; "
                  f"max|ν_i num - analítica| = {err:.2f} THz (donde I>2%)")
    save(fig, "fig08_dispersion_solo_fases")


if __name__ == "__main__":
    print(f"a = bτ² = {a:.2f};  ν_i(±τ) = {nu_i(-tau)/THZ:.1f}, {nu_i(tau)/THZ:.1f} THz;  "
          f"pendiente b/π = {b/np.pi/THZ*FS:.3f} THz/fs")
    fig01(); fig02(); fig03(); fig04(); fig05(); fig06(); fig07(); fig08()
