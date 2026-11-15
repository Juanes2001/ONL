# -*- coding: utf-8 -*-
"""Problema 32: simulación numérica del oscilador anarmónico (Boyd §1.4; análogo a la Tarea 1, punto 2).

Unidades normalizadas (w0 = 1, e/m = 1):
    x'' + 2 g x' + x + a x^2 = -F [cos(w1 t) + cos(w2 t)]      (no centrosimétrico, Boyd 1.4.1)
    x'' + 2 g x' + x - b x^3 = -F [cos(w1 t) + cos(w2 t)]      (centrosimétrico, Boyd 1.4.36 en 1D)
Con E~ = E1 e^{-i w1 t} + c.c. = F cos(w1 t)  =>  E1 = E2 = F/2.

Amplitud real de una línea: x~ = x(W) e^{-iWt} + c.c. = 2|x(W)| cos(Wt + fase)  (W != 0);
la línea de DC es x(0) (sin factor 2).
"""
import os
import sys
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.stdout.reconfigure(encoding='utf-8')
CARPETA_FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')

g, w1, w2 = 0.05, 0.3, 0.42
W0 = 0.06                      # w1 = 5 W0, w2 = 7 W0: todas las líneas son múltiplos de W0
T0 = 2*np.pi/W0                # periodo común de la señal (104.72)
N_TRANS = 20                   # periodos T0 de transitorio: e^{-g*20*T0} ~ 1e-45
N_VENT = 10                    # periodos T0 en la ventana de la FFT (número entero)
M_POR_T0 = 1024                # muestras por periodo T0  (dt = 0.102; Nyquist = 30.7 rad)


def D(w):
    """D(w) = w0^2 - w^2 - 2 i g w, con w0 = 1 (Boyd 1.4.10)."""
    return 1 - w**2 - 2j*g*w


def simular(F, a=0.0, b=0.0):
    """Integra el oscilador y devuelve (frecuencias, amplitudes reales, DC con signo) o None si escapa."""
    def rhs(t, y):
        x, v = y
        return [v, -2*g*v - x - a*x**2 + b*x**3 - F*(np.cos(w1*t) + np.cos(w2*t))]

    def escape(t, y):           # el potencial cúbico/cuártico tiene una barrera finita
        return abs(y[0]) - 20.0
    escape.terminal = True

    Nm = N_VENT*M_POR_T0
    t_ini = N_TRANS*T0
    t_eval = t_ini + np.arange(Nm)*(N_VENT*T0/Nm)
    sol = solve_ivp(rhs, (0, t_eval[-1]), [0.0, 0.0], method='DOP853', t_eval=t_eval,
                    rtol=1e-12, atol=1e-16, events=escape)
    if sol.status == 1 or sol.y.shape[1] < Nm:
        return None
    x = sol.y[0]
    X = np.fft.rfft(x)/Nm
    amp = 2*np.abs(X)
    amp[0] = X[0].real          # DC con signo
    frec = np.arange(len(X))*2*np.pi/(N_VENT*T0)   # rad (unidades de w0)
    return frec, amp


def linea(frec, amp, W):
    k = int(round(W/(2*np.pi/(N_VENT*T0))))
    assert abs(frec[k] - W) < 1e-9
    return amp[k]


def teoria_segundo_orden(F, a):
    """Amplitudes reales de (1.4.9), (1.4.13)-(1.4.14) con E1 = E2 = F/2 y e/m = 1."""
    E = F/2
    t = {}
    t['w1'] = 2*abs(E/D(w1))
    t['w2'] = 2*abs(E/D(w2))
    t['2w1'] = 2*abs(a*E**2/(D(2*w1)*D(w1)**2))
    t['w1+w2'] = 2*abs(2*a*E**2/(D(w1+w2)*D(w1)*D(w2)))
    t['w2-w1'] = 2*abs(2*a*E**2/(D(w2-w1)*D(w2)*D(-w1)))
    t['DC'] = (-2*a*E**2/(D(0)*abs(D(w1))**2) - 2*a*E**2/(D(0)*abs(D(w2))**2)).real
    return t


lineas = {'w1': w1, 'w2': w2, '2w1': 2*w1, 'w1+w2': w1+w2, 'w2-w1': w2-w1, 'DC': 0.0}

# ---------------- (a) F = 1e-3, a = 0.3 ----------------
a, F = 0.3, 1e-3
frec, amp = simular(F, a=a)
teo = teoria_segundo_orden(F, a)
print(f'(a) F = {F:g}, a = {a}: comparación simulación vs. perturbación')
print(f'{"línea":>7s} {"W":>6s} {"simulación":>13s} {"teoría":>13s} {"error rel.":>11s}')
for nombre, W in lineas.items():
    s, t = linea(frec, amp, W), teo[nombre]
    print(f'{nombre:>7s} {W:6.2f} {s:13.5e} {t:13.5e} {abs(s/t-1):11.2e}')
fondo = np.median(np.abs(amp[1:]))
print(f'    piso numérico (mediana de |amp|): {fondo:.1e}')

fig, ax = plt.subplots(figsize=(6.6, 3.8))
sel = frec <= 1.6
ax.semilogy(frec[sel], np.abs(amp[sel]) + 1e-20, color='C0', lw=0.8)
for nombre, W in lineas.items():
    ax.plot(W, abs(teo[nombre]), 'o', mfc='none', mec='C3', ms=7)
    ax.annotate(nombre.replace('w', r'$\omega_') .replace('$\\omega_1', '$\\omega_1$')
                .replace('$\\omega_2', '$\\omega_2$') if nombre != 'DC' else 'DC',
                (W, abs(teo[nombre])), textcoords='offset points', xytext=(3, 6), fontsize=8)
ax.plot([], [], 'o', mfc='none', mec='C3', label='teoría de perturbaciones (1.4.13)–(1.4.14)')
ax.plot([], [], color='C0', label='FFT de la simulación')
ax.set_ylim(1e-18, 1e-2)
ax.set_xlabel(r'Frecuencia angular $\Omega/\omega_0$ (adim.)')
ax.set_ylabel(r'Amplitud de $x(t)$ (unid. normalizadas)')
ax.set_title(r'$F=10^{-3}$, $a=0.3$, $\gamma=0.05$, $\omega_1=0.3$, $\omega_2=0.42$', fontsize=10)
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, which='both', alpha=0.3)
fig.tight_layout()
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(CARPETA_FIG, f't4a_p32a_espectro.{ext}'), dpi=200)
plt.close(fig)

# ---------------- (b) barrido en F ----------------
# malla logarítmica hasta 0.3 y fina (paso 0.0025) cerca del umbral de escape
Fs = np.concatenate([np.logspace(-3, np.log10(0.3), 26), np.arange(0.3025, 0.46, 0.0025)])
sfg_sim, sfg_teo, Fs_ok = [], [], []
for Fi in Fs:
    r = simular(Fi, a=a)
    if r is None:
        print(f'(b) F = {Fi:.3f}: el oscilador escapa por encima de la barrera del potencial')
        break
    Fs_ok.append(Fi)
    sfg_sim.append(linea(*r, w1+w2))
    sfg_teo.append(teoria_segundo_orden(Fi, a)['w1+w2'])
Fs_ok, sfg_sim, sfg_teo = map(np.array, (Fs_ok, sfg_sim, sfg_teo))
razon = sfg_sim/sfg_teo
pend = np.polyfit(np.log10(Fs_ok[:8]), np.log10(sfg_sim[:8]), 1)[0]
print(f'(b) pendiente log-log de la línea w1+w2 para F <= {Fs_ok[7]:.4f}: {pend:.4f}')
desv = np.abs(razon - 1)
# corrección relativa de orden siguiente: sim/teo ~ 1 - c F^2 (la amplitud corrige como F^4)
pq = Fs_ok <= 0.11
c = -np.polyfit(Fs_ok[pq]**2, razon[pq] - 1, 1)[0]
print(f'    ajuste sim/teo = 1 - c F^2 para F <= 0.11: c = {c:.3f}')
kmin = np.argmin(razon)
print(f'    máxima desviación antes del escape: sim/teo = {razon[kmin]:.4f} en F = {Fs_ok[kmin]:.4f}')
k = int(np.argmax(desv > 0.10)) if np.any(desv > 0.10) else None
if k:
    F10 = 10**np.interp(0.10, desv[k-1:k+1], np.log10(Fs_ok[k-1:k+1]))
    print(f'    desviación > 10 % a partir de F = {F10:.4f} (sim/teo en F = {Fs_ok[k]:.4f}: {razon[k]:.3f})')
else:
    F10 = Fs_ok[-1]
    print('    la desviación nunca supera el 10 % antes del escape')
for j, (Fi, ri) in enumerate(zip(Fs_ok, razon)):
    if Fi > 0.009 and j % 2 == 0:
        print(f'    F = {Fi:8.4f}: sim/teo = {ri:.4f}')
print(f'    último F sin escape: {Fs_ok[-1]:.4f}')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 5.6), sharex=True,
                               gridspec_kw={'height_ratios': [2, 1]})
ax1.loglog(Fs_ok, sfg_sim, 'o', ms=4, label='simulación (FFT)')
ax1.loglog(Fs_ok, sfg_teo, '-', color='C3', lw=1, label=r'segundo orden: $aF^2/|D(\omega_1+\omega_2)D(\omega_1)D(\omega_2)|$')
ax1.set_ylabel(r'Amplitud en $\omega_1+\omega_2$ (unid. norm.)')
ax1.legend(fontsize=8)
ax1.grid(True, which='both', alpha=0.3)
ax1.set_title(f'Pendiente ajustada (F pequeño): {pend:.3f}', fontsize=10)
ax2.semilogx(Fs_ok, razon, 'o-', ms=3)
ax2.axhspan(0.9, 1.1, color='gray', alpha=0.2, label=r'$\pm10$ %')
ax2.axvline(F10, color='C3', ls='--', lw=0.8, label=f'10 % en $F={F10:.3f}$')
ax2.set_xlabel(r'Amplitud de la fuerza $F$ (unid. normalizadas)')
ax2.set_ylabel('simulación / teoría')
ax2.legend(fontsize=8, loc='lower left')
ax2.grid(True, which='both', alpha=0.3)
fig.tight_layout()
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(CARPETA_FIG, f't4a_p32b_barrido_F.{ext}'), dpi=200)
plt.close(fig)

# ---------------- (c) centrosimétrico: -b x^3 en lugar de +a x^2 ----------------
F = 0.1
fa, aa = simular(F, a=0.3)
fb, ab = simular(F, b=0.3)
print(f'(c) F = {F}: amplitudes (no centrosimétrico a=0.3 | centrosimétrico b=0.3)')
lineas_c = {'DC': 0.0, 'w2-w1': w2-w1, 'w1': w1, 'w2': w2, '2w1': 2*w1, 'w1+w2': w1+w2,
            '2w2': 2*w2, '2w1-w2': 2*w1-w2, '2w2-w1': 2*w2-w1, '3w1': 3*w1,
            '2w1+w2': 2*w1+w2, '3w2': 3*w2}
for nombre, W in lineas_c.items():
    print(f'{nombre:>8s} {W:5.2f}  {abs(linea(fa, aa, W)):11.3e} | {abs(linea(fb, ab, W)):11.3e}')
# THG de tercer orden (Boyd 1.4.48 en 1D): x3(3w1) = -b E1^3/(D(3w1) D(w1)^3), amplitud real 2|x3|
b, E = 0.3, F/2
thg_teo = 2*abs(b*E**3/(D(3*w1)*D(w1)**3))
print(f'    3w1: simulación {linea(fb, ab, 3*w1):.4e}, teoría de tercer orden {thg_teo:.4e}')
pares = [0.0, w2-w1, 2*w1, w1+w2, 2*w2]
print(f'    máximo de las líneas pares en el caso centrosimétrico: '
      f'{max(abs(linea(fb, ab, W)) for W in pares):.1e}')

fig, axs = plt.subplots(2, 1, figsize=(6.6, 5.6), sharex=True)
for ax, (fr, am), tit in zip(axs, [(fa, aa), (fb, ab)],
                             [r'No centrosimétrico: $+a x^2$, $a=0.3$',
                              r'Centrosimétrico: $-b x^3$, $b=0.3$']):
    sel = fr <= 1.6
    ax.semilogy(fr[sel], np.abs(am[sel]) + 1e-20, lw=0.8)
    for nombre, W in lineas_c.items():
        ax.axvline(W, color='gray', lw=0.4, ls=':')
    ax.set_ylim(1e-17, 1)
    ax.set_title(tit + f',  $F={F}$', fontsize=10)
    ax.set_ylabel('Amplitud de $x(t)$ (unid. norm.)')
    ax.grid(True, which='major', alpha=0.3)
axs[1].set_xlabel(r'Frecuencia angular $\Omega/\omega_0$ (adim.)')
fig.tight_layout()
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(CARPETA_FIG, f't4a_p32c_centrosimetrico.{ext}'), dpi=200)
plt.close(fig)
print('figuras guardadas en', os.path.normpath(CARPETA_FIG))
