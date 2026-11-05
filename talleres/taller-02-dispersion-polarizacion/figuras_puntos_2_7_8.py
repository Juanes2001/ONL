"""Figuras de apoyo de la Tarea 2 (puntos 2, 7 y 8).

Se ejecuta con el Python de Windows (el único con numpy/matplotlib en esta máquina):
  "/mnt/c/Users/jero0/AppData/Local/Programs/Python/Python311/python.exe" figuras_puntos_2_7_8.py

Punto 2: índice n, índice de grupo N y velocidad de grupo v/c0 de un medio resonante
         diluido (ecs. 5.5-23, 5.5-24 y 5.5-27 de Saleh y Teich) en función de la frecuencia.
Punto 7: ángulo de walk-off rho(theta) entre k y S de la onda extraordinaria en cuarzo.
Punto 8: transmitancia cos^(2N)(pi/2N) de la cadena de N polarizadores.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(AQUI, "figuras")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": 0.3})


def guardar(fig, nombre):
    fig.savefig(os.path.join(OUT, nombre + ".png"), dpi=170, bbox_inches="tight")
    fig.savefig(os.path.join(OUT, nombre + ".pdf"), bbox_inches="tight")
    plt.close(fig)


# ----------------------------------------------------------------- Punto 2
def medio_resonante(n0, chi0, Q, x):
    """x = (nu - nu0)/Dnu. Devuelve n, N y v/c0 (modelo cerca de resonancia)."""
    # chi'(nu) = -(chi0 nu0/2) d/(d^2 + a^2), con d = nu - nu0, a = Dnu/2
    # n = n0 + chi'/(2 n0);  N = n + nu dn/dnu  (nu ~ nu0 en el factor);  v = c0/N
    a = 0.5                                   # a/Dnu
    d = x                                     # d/Dnu
    nu0 = Q                                   # nu0/Dnu
    chi_p = -(chi0 * nu0 / 2) * d / (d**2 + a**2)          # chi' (adimensional, nu en unidades de Dnu)
    dchi_p = -(chi0 * nu0 / 2) * (a**2 - d**2) / (d**2 + a**2) ** 2   # d chi'/d nu  (1/Dnu)
    n = n0 + chi_p / (2 * n0)
    N = n + (nu0 + d) * dchi_p / (2 * n0)
    return n, N, 1.0 / N


x = np.linspace(-3, 3, 2001)
fig, axs = plt.subplots(3, 2, figsize=(10, 8.2), sharex=True)
for j, (chi0, Q, titulo) in enumerate([(0.002, 10, r"acoplamiento débil: $\chi_0 Q^2/n_0^2 = 0.2$"),
                                       (0.05, 10, r"parámetros de la Fig. 5.6-4: $\chi_0 = 0.05$, $Q = 10$")]):
    n0 = 1.0
    n, N, v = medio_resonante(n0, chi0, Q, x)
    axs[0, j].plot(x, n, "k"); axs[0, j].set_ylabel(r"$n(\nu)$"); axs[0, j].set_title(titulo)
    axs[1, j].plot(x, N, "b"); axs[1, j].set_ylabel(r"$N(\nu)=c_0/v$")
    axs[1, j].axhline(n0, color="gray", ls=":")
    axs[2, j].plot(x, v, "r"); axs[2, j].set_ylabel(r"$v/c_0 = 1/N$")
    axs[2, j].axhline(1 / n0, color="gray", ls=":", label=r"$c_0/n_0$")
    axs[2, j].set_xlabel(r"$(\nu-\nu_0)/\Delta\nu$")
    if j == 1:
        axs[2, j].set_ylim(-1.5, 2.0)
        axs[1, j].set_ylim(-4.5, 2.0)
    else:
        axs[2, j].set_ylim(0.7, 1.3)
    for ax in axs[:, j]:
        ax.axvspan(-0.5, 0.5, color="orange", alpha=0.15)
        ax.axvline(-np.sqrt(3) / 2, color="green", ls="--", lw=0.8)
        ax.axvline(np.sqrt(3) / 2, color="green", ls="--", lw=0.8)
    axs[0, j].text(0, axs[0, j].get_ylim()[1] * 0.999, r"$dn/d\nu<0$" + "\n(anómala)", ha="center", va="top", fontsize=8)
    axs[0, j].text(-2, axs[0, j].get_ylim()[1] * 0.999, r"$dn/d\nu>0$" + "\n(normal)", ha="center", va="top", fontsize=8)
    axs[0, j].text(2, axs[0, j].get_ylim()[1] * 0.999, r"$dn/d\nu>0$" + "\n(normal)", ha="center", va="top", fontsize=8)
    axs[2, j].text(np.sqrt(3) / 2 + 0.05, axs[2, j].get_ylim()[0] + 0.05 * np.diff(axs[2, j].get_ylim())[0],
                   r"mínimos locales de $v$ en $\nu_0\pm\frac{\sqrt{3}}{2}\Delta\nu$", fontsize=8, color="green")
axs[2, 0].legend(loc="upper right", fontsize=8)
fig.suptitle(r"Punto 2. Medio resonante diluido: $n=n_0+\chi'(\nu)/2n_0$, $N=n+\nu\,dn/d\nu$, $v=c_0/N$. "
             "Zona naranja: $|\\nu-\\nu_0|<\\Delta\\nu/2$", fontsize=10)
fig.tight_layout()
guardar(fig, "punto2_velocidad_grupo")

# ----------------------------------------------------------------- Punto 7
ne, no = 1.553, 1.544
th = np.radians(np.linspace(0, 90, 901))
tan_rho = (ne**2 - no**2) * np.sin(th) * np.cos(th) / (ne**2 * np.cos(th) ** 2 + no**2 * np.sin(th) ** 2)
rho = np.degrees(np.arctan(tan_rho))
th_max = np.degrees(np.arctan(ne / no))
rho_max = np.degrees(np.arctan((ne**2 - no**2) / (2 * ne * no)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2))
ax1.plot(np.degrees(th), rho, "b", lw=1.5)
ax1.plot(th_max, rho_max, "ro")
ax1.annotate(rf"$\theta_{{max}} = {th_max:.2f}^\circ$, $\rho_{{max}} = {rho_max:.3f}^\circ$",
             (th_max, rho_max), (30, 0.12), arrowprops=dict(arrowstyle="->"), fontsize=9)
ax1.set_xlabel(r"$\theta$: ángulo entre $\mathbf{k}$ y el eje óptico (grados)")
ax1.set_ylabel(r"$\rho$: ángulo entre $\mathbf{k}$ y $\mathbf{S}$ (grados)")
ax1.set_title(r"Cuarzo ($n_e=1.553$, $n_o=1.544$): walk-off de la onda $e$", fontsize=9)
ax1.set_xlim(0, 90)

# construcción con la superficie k (elipse exagerada para que se vea)
ne_d, no_d = 1.40, 1.0
t = np.radians(np.linspace(0, 90, 400))
# elipse: ky^2/ne^2 + kz^2/no^2 = 1  (eje óptico = z vertical; y horizontal)
ky = ne_d * np.sin(t); kz = no_d * np.cos(t)
ax2.plot(ky, kz, "b", label="superficie k, onda e (elipse)")
ax2.plot(no_d * np.sin(t), no_d * np.cos(t), "k:", label="onda o (circunferencia)")
thd = np.arctan(ne_d / no_d)                     # theta_max del dibujo
# punto de la elipse en la dirección theta: k = n(theta) (sin, cos)
n_th = 1 / np.sqrt(np.cos(thd) ** 2 / no_d**2 + np.sin(thd) ** 2 / ne_d**2)
P = n_th * np.array([np.sin(thd), np.cos(thd)])
ax2.annotate("", xy=P, xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="r", lw=1.6))
ax2.text(P[0] * 0.55 + 0.05, P[1] * 0.55 - 0.08, r"$\mathbf{k}$", color="r", fontsize=12)
# normal a la elipse en P: (ky/ne^2, kz/no^2)
nrm = np.array([P[0] / ne_d**2, P[1] / no_d**2]); nrm /= np.linalg.norm(nrm)
ax2.annotate("", xy=P + 0.45 * nrm, xytext=P, arrowprops=dict(arrowstyle="->", color="g", lw=1.6))
ax2.text(*(P + 0.47 * nrm), r"$\mathbf{S}$ (rayo)", color="g", fontsize=11)
# tangente
tg = np.array([-nrm[1], nrm[0]])
ax2.plot([P[0] - 0.5 * tg[0], P[0] + 0.5 * tg[0]], [P[1] - 0.5 * tg[1], P[1] + 0.5 * tg[1]], "g--", lw=0.8)
ax2.annotate("", xy=(0, 1.55), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="k"))
ax2.text(0.03, 1.5, "eje óptico (z)")
ax2.text(1.45, 0.03, r"$k_y/k_0$")
ax2.text(0.12, 0.42, r"$\theta$", fontsize=11)
ax2.text(P[0] + 0.08, P[1] + 0.12, r"$\rho$", fontsize=11, color="purple")
ax2.set_aspect("equal"); ax2.set_xlim(-0.05, 1.7); ax2.set_ylim(-0.05, 1.65)
ax2.set_title("Construcción: S es normal a la superficie k (índices exagerados)", fontsize=9)
ax2.legend(loc="lower left", fontsize=8)
fig.tight_layout()
guardar(fig, "punto7_walkoff_cuarzo")

# ----------------------------------------------------------------- Punto 8
Ns = np.arange(1, 201)
T = np.cos(np.pi / (2 * Ns)) ** (2 * Ns)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.semilogx(Ns, T, "o-", ms=3, lw=1)
ax.semilogx(Ns, np.exp(-np.pi**2 / (4 * Ns)), "r--", lw=1, label=r"asíntota $e^{-\pi^2/4N}$")
ax.set_xlabel("Número de polarizadores N (ejes espaciados $\\theta=\\pi/2N$)")
ax.set_ylabel(r"Transmitancia $\mathcal{T}=\cos^{2N}(\pi/2N)$")
ax.set_title("Punto 8. Rotación de 90° con N polarizadores en cascada")
for Nn in [1, 2, 3, 10, 100]:
    ax.annotate(f"N={Nn}: {np.cos(np.pi/(2*Nn))**(2*Nn):.3f}", (Nn, np.cos(np.pi / (2 * Nn)) ** (2 * Nn)),
                (5, -12), textcoords="offset points", fontsize=8)
ax.set_ylim(-0.05, 1.05); ax.legend(loc="lower right")
fig.tight_layout()
guardar(fig, "punto8_transmitancia")
print("figuras escritas en", OUT)
