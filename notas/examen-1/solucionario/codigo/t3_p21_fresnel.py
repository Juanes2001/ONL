"""Problema 21: ecuaciones de Fresnel (Saleh 6.2-8, 6.2-9; convención e^{jwt}).

(b) aire -> vidrio n = 1.5 a 45°.
(c) RTI vidrio (1.5) -> aire a 1.2 theta_c: fases directas y comparación con (6.2-11), (6.2-13).
(d) Rombo de Fresnel, n = 1.51: retardo vs. ángulo y ángulos de 45° por reflexión.
(e) R_TE y R_TM vs. theta para aire -> Si (3.48) y aire -> Si3N4 (1.99) a 1.55 µm.
"""
import os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')


def cos_t2(n1, n2, th1):
    """cos(theta_2) con la rama de Saleh: -j sqrt(...) en reflexión total (p. 212)."""
    s2 = (n1 / n2 * np.sin(th1))**2
    return np.where(s2 <= 1, np.sqrt(np.abs(1 - s2)), -1j * np.sqrt(np.abs(s2 - 1)))


def fresnel(n1, n2, th1):
    """r_x (TE, 6.2-8) y r_y (TM, 6.2-9) de Saleh."""
    c1 = np.cos(th1)
    c2 = cos_t2(n1, n2, th1)
    rx = (n1 * c1 - n2 * c2) / (n1 * c1 + n2 * c2)
    ry = (n1 / c1 - n2 / c2) / (n1 / c1 + n2 / c2)
    return rx, ry


# ---------------- (b) ----------------
th = np.radians(45.0)
rx, ry = fresnel(1.0, 1.5, th)
print("(b) aire->vidrio, 45°:")
print(f"   cos(theta2) = {cos_t2(1.0, 1.5, th):.4f}")
print(f"   r_TE = {rx.real:.4f}, R_TE = {abs(rx)**2:.4f}")
print(f"   r_TM = {ry.real:.4f}, R_TM = {abs(ry)**2:.4f}")
print(f"   promedio (no polarizada) = {(abs(rx)**2 + abs(ry)**2)/2:.4f}")
print(f"   comprobación r_TM = r_TE^2 a 45°: {rx.real**2:.4f}")

# ---------------- (c) ----------------
n1, n2 = 1.5, 1.0
thc = np.arcsin(n2 / n1)
th1 = 1.2 * thc
rx, ry = fresnel(n1, n2, th1)
fx, fy = np.degrees(np.angle(rx)), np.degrees(np.angle(ry))
print("\n(c) RTI vidrio->aire:")
print(f"   theta_c = {np.degrees(thc):.3f}°, theta1 = 1.2 theta_c = {np.degrees(th1):.3f}°")
print(f"   cos(theta2) = {cos_t2(n1, n2, th1):.4f}")
print(f"   |r_TE| = {abs(rx):.6f}, phi_TE = {fx:.2f}°;  |r_TM| = {abs(ry):.6f}, phi_TM = {fy:.2f}°")
print(f"   phi_TE - phi_TM = {fx - fy:.2f}° ; convención B&W (r_TM -> -r_TM): "
      f"{fx - (fy + 180):.2f}°")
X = np.sqrt(np.cos(thc)**2 / np.cos(th1)**2 - 1)
print(f"   (6.2-11): 2 atan(X) = {np.degrees(2*np.arctan(X)):.2f}°  (X = {X:.4f})")
print(f"   (6.2-13) impresa a 1.2 theta_c: {np.degrees(2*np.arctan(-X/np.sin(thc)**2)):.2f}°")
print(f"   forma correcta -2 atan(sin^2 thc / X) = "
      f"{np.degrees(-2*np.arctan(np.sin(thc)**2/X)):.2f}°")
eps = 1e-9
_, ryc = fresnel(n1, n2, thc + eps)
print(f"   en theta_c(+): phi_TM directo = {np.degrees(np.angle(ryc)):.2f}°, "
      f"(6.2-13) impresa = 0°")

# ---------------- (d) Rombo de Fresnel ----------------
n = 1.51
thc = np.arcsin(1 / n)


def retardo_bw(t):
    """delta = phi_TE - phi_TM - 180° (convención B&W), en grados, para t > theta_c."""
    rx, ry = fresnel(n, 1.0, t)
    d = np.degrees(np.angle(rx) - np.angle(ry)) - 180.0
    return d


def retardo_formula(t):
    """Born & Wolf: tan(delta/2) = cos t sqrt(sin^2 t - 1/n^2) / sin^2 t."""
    return np.degrees(2 * np.arctan(np.cos(t) * np.sqrt(np.sin(t)**2 - 1 / n**2) / np.sin(t)**2))


t = np.linspace(thc + 1e-6, np.pi / 2 - 1e-6, 4000)
d = -retardo_bw(t)                            # signo + para graficar
print(f"\n(d) n = {n}: theta_c = {np.degrees(thc):.2f}°; "
      f"max|dif. con la fórmula B&W| = {np.max(np.abs(d - retardo_formula(t))):.1e}°")
im = np.argmax(d)
tm = t[im]                                    # ángulo del retardo máximo (malla fina)
print(f"   retardo máximo = {d[im]:.2f}° en theta = {np.degrees(tm):.2f}°")
a1 = brentq(lambda x: retardo_formula(x) - 45, thc + 1e-6, tm)
a2 = brentq(lambda x: retardo_formula(x) - 45, tm, np.pi / 2 - 1e-6)
print(f"   45° por reflexión en theta = {np.degrees(a1):.2f}° y {np.degrees(a2):.2f}°")
print(f"   en Saleh: phi_TE - phi_TM = {retardo_bw(a1)+180:.2f}° por reflexión; "
      f"dos reflexiones: {2*(retardo_bw(a1)+180):.2f}° = 270° = -90° (mod 360°)")

fig, ax = plt.subplots(figsize=(6.4, 4))
ax.plot(np.degrees(t), d, 'C0', label=r'$|\varphi_{TE}-\varphi_{TM}-180^\circ|$ (B&W)')
ax.axhline(45, color='C3', ls='--', lw=1, label=r'$45^\circ$ (2 reflexiones = $\lambda/4$)')
for a in (a1, a2):
    ax.axvline(np.degrees(a), color='0.5', ls=':', lw=1)
    ax.text(np.degrees(a), 2, f'{np.degrees(a):.1f}°', ha='center', fontsize=8,
            bbox=dict(fc='w', ec='none'))
ax.set_xlabel(r'Ángulo de incidencia interno $\theta_1$ (grados)')
ax.set_ylabel(r'Retardo por reflexión $\delta$ (grados)')
ax.set_title(f'Rombo de Fresnel, $n={n}$')
ax.set_xlim(np.degrees(thc), 90); ax.set_ylim(0, 50)
ax.legend(fontsize=8, loc='lower center')
ax.grid(alpha=0.3)
fig.tight_layout()
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(base, f't3_p21_rombo_fresnel.{ext}'), dpi=200)

# ---------------- (e) Reflectancias Si y Si3N4 ----------------
fig, ax = plt.subplots(figsize=(6.4, 4))
tt = np.linspace(0, np.pi / 2, 1000)
for nn, col, nom in ((3.48, 'C0', 'Si'), (1.99, 'C2', r'Si$_3$N$_4$')):
    rx, ry = fresnel(1.0, nn, tt)
    tb = np.degrees(np.arctan(nn))                # (6.2-12)
    print(f"(e) n = {nn}: theta_B = {tb:.2f}°, R(0) = {((nn-1)/(nn+1))**2:.4f}")
    ax.plot(np.degrees(tt), abs(rx)**2, col, label=f'{nom} TE')
    ax.plot(np.degrees(tt), abs(ry)**2, col, ls='--', label=f'{nom} TM')
    ax.axvline(tb, color=col, ls=':', lw=1)
    xt, ha = (tb + 1, 'left') if nn > 3 else (tb - 1, 'right')
    ax.text(xt, 0.92, rf'$\theta_B={tb:.1f}^\circ$', color=col, ha=ha, fontsize=8)
ax.set_xlabel(r'Ángulo de incidencia $\theta$ (grados)')
ax.set_ylabel(r'Reflectancia de potencia $\mathcal{R}$')
ax.set_title(r'Aire $\to$ medio, $\lambda_0=1.55\ \mu$m')
ax.set_xlim(0, 90); ax.set_ylim(0, 1)
ax.legend(fontsize=8, loc='upper left')
ax.grid(alpha=0.3)
fig.tight_layout()
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(base, f't3_p21_reflectancias.{ext}'), dpi=200)
print("figuras guardadas")
