"""Problema 37: Kramers-Kronig para Debye y para el oscilador anarmónico (Boyd §1.7).

Convención de Boyd: e^{-i w t}; chi(w) = int_0^inf R(tau) e^{i w tau} dtau, analítica en Im w > 0.
"""
import numpy as np
from scipy.integrate import quad

# ---------- (b) Debye: chi = chi0/(1 - i w tau_r) ----------
chi0, tau = 1.0, 1.0                     # unidades normalizadas (w en 1/tau_r)
chi = lambda w: chi0/(1 - 1j*w*tau)

def pv_semieje(f, w, L=2e4):
    """Valor principal de int_0^L f(w')/(w'^2 - w^2) dw' (quad con peso de Cauchy).
    1/(w'^2-w^2) = [1/(w'-w)]/(w'+w): el polo de w'=w lo maneja weight='cauchy'."""
    g = lambda x: f(x)/(x + w)
    a = quad(g, 0, 2*w, weight='cauchy', wvar=w, limit=400)[0]
    b = quad(lambda x: f(x)/(x**2 - w**2), 2*w, L, limit=2000)[0]
    return a + b

print("(b) Debye, verificación numérica de (1.7.9a) y (1.7.9b):")
for w in (0.3, 1.0, 3.0):
    re_kk = 2/np.pi*pv_semieje(lambda x: x*chi(x).imag, w)
    im_kk = -2*w/np.pi*pv_semieje(lambda x: chi(x).real, w)
    print(f"    w tau = {w:3.1f}: Re chi = {chi(w).real:.5f}  KK -> {re_kk:.5f};  "
          f"Im chi = {chi(w).imag:.5f}  KK -> {im_kk:.5f}")

# ---------- (c) Oscilador anarmónico: polos y KK en la recta real ----------
w0, g = 1.0, 0.05                       # w0 = 1, gamma = 0.05 w0
D = lambda w: w0**2 - w**2 - 2j*g*w
w3 = 1.3                                 # frecuencia fija del problema (c)
print("\n(c) Raíces de D(w)=0:", np.round(np.roots([-1, -2j*g, w0**2]), 4), "(Im = -gamma)")
print("    Raíces de D(2w)=0:", np.round(np.roots([-4, -4j*g, w0**2]), 4), "(Im = -gamma/2)")
print("    Raíces de D(-w2)=0:", np.round(np.roots([-1, 2j*g, w0**2]), 4), "(Im = +gamma: semiplano superior)")

def kk_completo(f, w, L=400.0, d=0.05):
    """(1/(i pi)) VP int_{-L}^{L} f(w')/(w'-w) dw'.
    El tramo [w-d, w+d] se integra con peso de Cauchy; el resto con quad normal,
    indicándole dónde están las resonancias (picos estrechos de ancho ~gamma)."""
    picos = [p for p in (-1, -0.5, 0, 0.5, 1, w3 - 1, w3 + 1, w1, -w1) if -L < p < L]
    def parte(h):
        c = quad(h, w - d, w + d, weight='cauchy', wvar=w)[0]
        izq = quad(lambda x: h(x)/(x - w), -L, w - d, points=[p for p in picos if p < w - d], limit=4000)[0]
        der = quad(lambda x: h(x)/(x - w), w + d, L, points=[p for p in picos if p > w + d], limit=4000)[0]
        return c + izq + der
    re = parte(lambda x: f(x).real)
    im = parte(lambda x: f(x).imag)
    return (re + 1j*im)/(1j*np.pi)

w1 = 0.4
chi2_shg = lambda w: 1/(D(2*w)*D(w)**2)        # chi2(2w;w,w) salvo la constante N e^3 a/(eps0 m^2)
chi2_dfg = lambda w2: 1/(D(w3 - w2)*D(w3)*D(-w2))  # chi2(w1; w3, -w2) en función de w2
print("    chi2(2w;w,w): comparación con (1.7.12)")
for w in (0.3, 0.5, 0.8):
    print(f"      w = {w}: chi = {chi2_shg(w):.5f}, KK = {kk_completo(chi2_shg, w):.5f}")
print("    chi2(w1;w3,-w2) con w3 = 1.3 w0, en función de w2:")
for w2 in (0.3, 0.6):
    print(f"      w2 = {w2}: chi = {chi2_dfg(w2):.5f}, KK = {kk_completo(chi2_dfg, w2):.5f}"
          f"  (razón KK/chi = {kk_completo(chi2_dfg, w2)/chi2_dfg(w2):.3f})")

# ---------- (d) chi3 autoinducido vs. haz auxiliar (modelo 1.4.52, sin constantes) ----------
chi3_auto = lambda w: 1/(D(w)**3*D(-w))
chi3_aux = lambda w: 1/(D(w)**2*D(w1)*D(-w1))
print("\n(d) chi3 en el modelo del oscilador:")
for w in (0.5, 0.8):
    print(f"    w = {w}: autoinducido chi = {chi3_auto(w):.4f}, KK = {kk_completo(chi3_auto, w):.4f};"
          f"  auxiliar chi = {chi3_aux(w):.4f}, KK = {kk_completo(chi3_aux, w):.4f}")
