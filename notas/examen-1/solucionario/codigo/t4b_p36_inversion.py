"""Problema 36(a): respuestas de la Fig. 1.5.2 de Boyd y su contenido armónico.

(c) medio centrosimétrico:      P(t) = sin(wt) - 0.25 sin(3wt)
(d) medio no centrosimétrico:   P(t) = -0.2 + sin(wt) + 0.2 cos(2wt)
Se calcula la serie de Fourier con una FFT sobre un periodo y se verifica la
simetría de media onda P(t + T/2) = -P(t), propia de una respuesta impar.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

N = 1024
t = np.arange(N) / N                     # tiempo en unidades del periodo T (wt = 2 pi t)
wt = 2*np.pi*t
Pc = np.sin(wt) - 0.25*np.sin(3*wt)
Pd = -0.2 + np.sin(wt) + 0.2*np.cos(2*wt)

def armonicos(f, nmax=4):
    """Amplitud real de cada armónico: f = a0 + sum_n A_n cos(n wt + fase)."""
    F = np.fft.rfft(f) / N
    A = np.abs(F[:nmax+1]) * 2
    A[0] = F[0].real                      # término DC (con signo)
    return A

for nombre, f in (('centrosimétrico (c)', Pc), ('no centrosimétrico (d)', Pd)):
    A = armonicos(f)
    media_onda = np.max(np.abs(np.roll(f, -N//2) + f))
    print(f"{nombre}: DC = {A[0]:+.3f}, |w| = {A[1]:.3f}, |2w| = {A[2]:.3f}, "
          f"|3w| = {A[3]:.3f}, |4w| = {A[4]:.3f};  max|P(t+T/2)+P(t)| = {media_onda:.3f}")

fig, axs = plt.subplots(1, 2, figsize=(9, 3.4))
axs[0].plot(t, np.sin(wt), 'k--', lw=0.8, label=r'lineal: $\sin\omega t$')
axs[0].plot(t, Pc, 'C0', label='(c) centrosimétrico')
axs[0].plot(t, Pd, 'C3', label='(d) no centrosimétrico')
axs[0].axhline(0, color='gray', lw=0.5)
axs[0].set_xlabel(r'Tiempo $t/T$'); axs[0].set_ylabel(r'Polarización $\tilde P(t)$ (u. arb.)')
axs[0].legend(fontsize=7, loc='lower left'); axs[0].grid(alpha=0.3)
n = np.arange(5)
axs[1].bar(n - 0.18, np.abs(armonicos(Pc)), width=0.35, color='C0', label='(c)')
axs[1].bar(n + 0.18, np.abs(armonicos(Pd)), width=0.35, color='C3', label='(d)')
axs[1].set_xticks(n); axs[1].set_xticklabels(['DC', r'$\omega$', r'$2\omega$', r'$3\omega$', r'$4\omega$'])
axs[1].set_xlabel('Componente de frecuencia'); axs[1].set_ylabel('Amplitud (u. arb.)')
axs[1].legend(fontsize=8); axs[1].grid(alpha=0.3, axis='y')
fig.tight_layout()
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras', 't4b_p36_armonicos')
fig.savefig(base + '.png', dpi=200); fig.savefig(base + '.pdf')
