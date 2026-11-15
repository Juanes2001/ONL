"""Problema 35: d_eff en cristales 3m (BBO) y en GaAs (-43m).

Convención de Boyd (SI): P(2w) = 2 eps0 [d_il] (Ex^2, Ey^2, Ez^2, 2EyEz, 2ExEz, 2ExEy)^T  (ec. 1.5.26)
y P(2w) = 2 eps0 d_eff E(w)^2 (ec. 1.5.29).
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def columna_shg(E):
    """Vector columna de (1.5.26) para un campo E = (Ex, Ey, Ez)."""
    Ex, Ey, Ez = E
    return np.array([Ex**2, Ey**2, Ez**2, 2*Ey*Ez, 2*Ex*Ez, 2*Ex*Ey])

def columna_sfg(E1, E2):
    """Vector columna de (1.5.27) para dos campos distintos."""
    return np.array([E1[0]*E2[0], E1[1]*E2[1], E1[2]*E2[2],
                     E1[1]*E2[2] + E1[2]*E2[1],
                     E1[0]*E2[2] + E1[2]*E2[0],
                     E1[0]*E2[1] + E1[1]*E2[0]])

def matriz_3m(d22, d31, d33):
    """Matriz d_il de la clase 3m con Kleinman (Boyd, p. 46)."""
    return np.array([[0, 0, 0, 0, d31, -d22],
                     [-d22, d22, 0, d31, 0, 0],
                     [d31, d31, d33, 0, 0, 0]])

def vectores(theta, phi):
    """k, dirección ordinaria o y extraordinaria e (sin walk-off)."""
    k = np.array([np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)])
    o = np.array([-np.sin(phi), np.cos(phi), 0.0])
    # Elegimos e = -theta_hat, el signo que reproduce el signo global de (1.5.30a)
    e = np.array([-np.cos(theta)*np.cos(phi), -np.cos(theta)*np.sin(phi), np.sin(theta)])
    return k, o, e

# ---- (a) Verificación numérica de (1.5.30a) y (1.5.30b) para ángulos al azar ----
rng = np.random.default_rng(1)
d22, d31, d33 = 2.2, 0.7, 5.0          # pm/V, valores de prueba (d31 no nulo a propósito)
d = matriz_3m(d22, d31, d33)
err1 = err2 = 0.0
for _ in range(1000):
    th, ph = rng.uniform(0, np.pi), rng.uniform(0, 2*np.pi)
    k, o, e = vectores(th, ph)
    # Tipo I (o + o -> e): P = 2 eps0 d·col(o); d_eff = proyección sobre e (factor 2 eps0 E^2 fuera)
    deff1 = e @ (d @ columna_shg(o))
    f1 = d31*np.sin(th) - d22*np.cos(th)*np.sin(3*ph)
    # Tipo II (o + e -> e) con (1.5.27): P = 4 eps0 d·col(o,e) -> d_eff = e·(d col)
    deff2 = e @ (d @ columna_sfg(o, e))
    f2 = d22*np.cos(th)**2*np.cos(3*ph)
    # e aparece dos veces (campo y proyección): el resultado es -f2 con cualquier signo de e;
    # el signo global de d_eff es convencional, así que comparamos módulos
    deff2, f2 = abs(deff2), abs(f2)
    err1 = max(err1, abs(deff1 - f1)); err2 = max(err2, abs(deff2 - f2))
print(f"(a) error máximo tipo I  vs (1.5.30a): {err1:.2e} pm/V")
print(f"    error máximo tipo II vs (1.5.30b): {err2:.2e} pm/V  (en módulo: el signo global es convencional)")

# ---- (b) BBO: theta = 22.9 grados, d22 = 2.2 pm/V, d31 = 0 ----
th = np.deg2rad(22.9)
phi = np.linspace(-180, 180, 3601)
dbbo = matriz_3m(2.2, 0.0, 0.0)
deff = np.array([vectores(th, np.deg2rad(p))[2] @ (dbbo @ columna_shg(vectores(th, np.deg2rad(p))[1])) for p in phi])
imax = np.argmax(np.abs(deff))
print(f"(b) |d_eff|max = {np.abs(deff).max():.3f} pm/V  (d22 cos theta = {2.2*np.cos(th):.3f} pm/V)")
maximos = phi[np.isclose(np.abs(deff), np.abs(deff).max(), rtol=1e-6)]
print("    phi de los máximos (grados):", np.round(maximos, 1))
for p in (-30, 30, 90, 0):
    k, o, e = vectores(th, np.deg2rad(p))
    print(f"    phi = {p:4d} grados -> d_eff = {e @ (dbbo @ columna_shg(o)):+.3f} pm/V")

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(phi, deff, color='C0', label=r'$d_{\rm eff}=-d_{22}\cos\theta\,\sin3\phi$')
ax.axhline(0, color='k', lw=0.6)
for p in (-150, -90, -30, 30, 90, 150):
    ax.axvline(p, color='gray', lw=0.5, ls=':')
ax.set_xlabel(r'Ángulo azimutal $\phi$ (grados)')
ax.set_ylabel(r'$d_{\rm eff}$ (pm/V)')
ax.set_title(r'BBO, SHG tipo I, $\theta=22.9^\circ$, $d_{31}=0$')
ax.set_xlim(-180, 180); ax.set_xticks(np.arange(-180, 181, 30))
ax.legend(loc='upper right', fontsize=8); ax.grid(alpha=0.3)
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't4b_p35_deff_bbo')
fig.savefig(base + '.png', dpi=200); fig.savefig(base + '.pdf')

# ---- (c) GaAs: d14 = d25 = d36 = 370 pm/V ----
dg = 370.0
dGaAs = np.array([[0, 0, 0, dg, 0, 0], [0, 0, 0, 0, dg, 0], [0, 0, 0, 0, 0, dg]])
for nombre, u in (('[100]', [1, 0, 0]), ('[110]', [1, 1, 0]), ('[111]', [1, 1, 1])):
    u = np.array(u, float); u /= np.linalg.norm(u)
    P = dGaAs @ columna_shg(u)        # P/(2 eps0 E^2), en pm/V
    modulo = np.linalg.norm(P)
    proy = P @ u
    print(f"(c) E || {nombre}: P/(2 eps0 E^2) = {np.round(P, 2)} pm/V, |.| = {modulo:.1f} pm/V, "
          f"proyección sobre E = {proy:.1f} pm/V")
print(f"    2 d14/sqrt(3) = {2*dg/np.sqrt(3):.1f} pm/V")
