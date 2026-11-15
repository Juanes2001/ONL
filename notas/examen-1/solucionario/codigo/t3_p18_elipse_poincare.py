"""Problema 18: elipse, Stokes y esfera de Poincaré (convención de Saleh, e^{jwt}).

J = (1, 2 e^{j pi/3}) / sqrt(5) y su estado ortogonal J_perp.
Se calculan r, phi, psi, chi (ecs. 6.1-6 y 6.1-7), los parámetros de Stokes (6.1-9)
y se dibujan las dos elipses (con el sentido de giro) y los dos puntos en la esfera.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def parametros(J):
    """Devuelve r, phi, psi, chi (grados) y el vector de Stokes de un vector de Jones."""
    Ax, Ay = J
    r = abs(Ay) / abs(Ax)
    phi = np.angle(Ay) - np.angle(Ax)
    phi = (phi + np.pi) % (2 * np.pi) - np.pi          # fase en (-pi, pi]
    S0 = abs(Ax)**2 + abs(Ay)**2                      # (6.1-9a)
    S1 = abs(Ax)**2 - abs(Ay)**2                      # (6.1-9b)
    S2 = 2 * np.real(np.conj(Ax) * Ay)                # (6.1-9c)
    S3 = 2 * np.imag(np.conj(Ax) * Ay)                # (6.1-9d)
    # 2psi con el cuadrante correcto: atan2(S2, S1)  (equivale a 6.1-6)
    psi = 0.5 * np.arctan2(S2, S1)
    chi = 0.5 * np.arcsin(S3 / S0)                    # (6.1-7)
    return r, np.degrees(phi), np.degrees(psi), np.degrees(chi), np.array([S0, S1, S2, S3])


J = np.array([1, 2 * np.exp(1j * np.pi / 3)]) / np.sqrt(5)
Jp = np.array([2, -np.exp(1j * np.pi / 3)]) / np.sqrt(5)     # estado ortogonal

for nombre, v in (("J", J), ("J_perp", Jp)):
    r, phi, psi, chi, S = parametros(v)
    print(f"{nombre}: r = {r:.4f}, phi = {phi:.2f}°, psi = {psi:.2f}° "
          f"(= {psi % 180:.2f}°), chi = {chi:.2f}°")
    print(f"   tan(2psi) por (6.1-6) = {2*r*np.cos(np.radians(phi))/(1-r**2):.4f}")
    print(f"   Stokes = ({S[0]:.4f}, {S[1]:.4f}, {S[2]:.4f}, {S[3]:.4f}); "
          f"S1^2+S2^2+S3^2 - S0^2 = {S[1]**2+S[2]**2+S[3]**2-S[0]**2:.1e}")
    print(f"   Poincaré: polar = 90° - 2chi = {90-2*chi:.2f}°, azimut = 2psi = {2*psi:.2f}°")
print(f"producto interno (J, J_perp) = {J[0]*np.conj(Jp[0]) + J[1]*np.conj(Jp[1]):.2e}")

# ---------------- Figura: elipses y esfera ----------------
fig = plt.figure(figsize=(10, 4.6))
ax = fig.add_subplot(1, 2, 1)
wt = np.linspace(0, 2 * np.pi, 400)
for v, col, lab in ((J, 'C0', r'$\mathbf{J}$ (derecha)'), (Jp, 'C3', r'$\mathbf{J}_\perp$ (izquierda)')):
    # campo real en z = 0: E = Re{A e^{j w t}}  (6.1-4)
    Ex = np.real(v[0] * np.exp(1j * wt))
    Ey = np.real(v[1] * np.exp(1j * wt))
    ax.plot(Ex, Ey, col, label=lab)
    # flecha que indica el sentido de giro al aumentar t
    i = 40
    ax.annotate('', xy=(Ex[i + 6], Ey[i + 6]), xytext=(Ex[i], Ey[i]),
                arrowprops=dict(arrowstyle='-|>', color=col, lw=1.8))
    _, _, psi, _, _ = parametros(v)
    s = np.linspace(-1, 1, 2)
    ax.plot(s * np.cos(np.radians(psi)), s * np.sin(np.radians(psi)), col, ls=':', lw=1)
ax.set_aspect('equal')
ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
ax.set_xlabel(r'$\mathcal{E}_x$ (unid. de $|\mathbf{A}|$)')
ax.set_ylabel(r'$\mathcal{E}_y$ (unid. de $|\mathbf{A}|$)')
ax.set_title('Elipses en $z=0$ (la onda viene hacia el lector)')
ax.legend(loc='lower left', fontsize=8)
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1)

ax3 = fig.add_subplot(1, 2, 2, projection='3d')
u, w = np.mgrid[0:2 * np.pi:40j, 0:np.pi:20j]
ax3.plot_wireframe(np.cos(u) * np.sin(w), np.sin(u) * np.sin(w), np.cos(w),
                   color='0.8', lw=0.4)
ax3.plot(np.cos(wt), np.sin(wt), 0 * wt, 'k', lw=0.8)          # ecuador: lineales
for v, col, lab in ((J, 'C0', r'$\mathbf{J}$'), (Jp, 'C3', r'$\mathbf{J}_\perp$')):
    S = parametros(v)[4]
    ax3.plot([0, S[1]], [0, S[2]], [0, S[3]], col, lw=2)
    ax3.scatter(S[1], S[2], S[3], color=col, s=40)
    ax3.text(1.15 * S[1], 1.15 * S[2], 1.15 * S[3], lab, color=col)
ax3.text(0, 0, 1.15, 'R', ha='center'); ax3.text(0, 0, -1.3, 'L', ha='center')
ax3.text(1.25, 0, 0, r'LP$_x$'); ax3.text(-1.45, 0, 0, r'LP$_y$')
ax3.set_xlabel(r'$S_1/S_0$'); ax3.set_ylabel(r'$S_2/S_0$'); ax3.set_zlabel(r'$S_3/S_0$')
ax3.set_box_aspect((1, 1, 1))
ax3.view_init(elev=22, azim=35)
ax3.set_title('Esfera de Poincaré')
fig.tight_layout()

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras')
for ext in ('png', 'pdf'):
    fig.savefig(os.path.join(base, f't3_p18_elipse_poincare.{ext}'), dpi=200)
print("figura guardada")
