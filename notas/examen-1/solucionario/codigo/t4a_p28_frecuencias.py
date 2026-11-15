# -*- coding: utf-8 -*-
"""Problema 28(d): componentes de frecuencia de E~^3 con tres frecuencias (Boyd §1.2.9, p. 12-13).

E~(t) = sum_{k=±1,±2,±3} E_k exp(-i w_k t), con w_{-k} = -w_k y E_{-k} = E_k^*.
E~^3 = sum_{a,b,c} E_a E_b E_c exp[-i(w_a+w_b+w_c)t]: hay 6^3 = 216 ternas ORDENADAS.
Se agrupan por frecuencia suma y, dentro de cada frecuencia, por el multiconjunto {a,b,c}
(los términos que dan el mismo producto de amplitudes). El número de ternas ordenadas
de cada multiconjunto es el factor de degeneración D (1, 3 o 6) de (1.2.17).
"""
import sys
import itertools
from collections import defaultdict
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

# Frecuencias inconmensurables: ninguna combinación entera pequeña coincide por accidente
w = {1: 1.0, 2: np.sqrt(2.0), 3: np.sqrt(5.0)}
nombres = {1: 'w1', 2: 'w2', 3: 'w3'}

indices = [1, -1, 2, -2, 3, -3]             # +k = E_k, -k = E_k^* (frecuencia negativa)
def frec(k):
    return np.sign(k) * w[abs(k)]

grupos = defaultdict(lambda: defaultdict(int))   # suma -> multiconjunto -> nº de ternas ordenadas
for terna in itertools.product(indices, repeat=3):
    s = round(sum(frec(k) for k in terna), 9)
    multiconj = tuple(sorted(terna, key=lambda k: (abs(k), -k)))
    grupos[s][multiconj] += 1

def etiqueta_frec(mc):
    """Escribe la frecuencia como combinación de w1, w2, w3 (p. ej. 2w1-w2)."""
    coef = {1: 0, 2: 0, 3: 0}
    for k in mc:
        coef[abs(k)] += int(np.sign(k))
    txt = ''
    # primero los términos positivos, luego los negativos (p. ej. w3-2w1)
    orden = [j for j in (1, 2, 3) if coef[j] > 0] + [j for j in (1, 2, 3) if coef[j] < 0]
    for j in orden:
        c = coef[j]
        signo = '+' if c > 0 else '-'
        mag = '' if abs(c) == 1 else str(abs(c))
        txt += f'{signo}{mag}{nombres[j]}'
    return txt.lstrip('+') if txt else '0'

def etiqueta_amp(mc):
    """Producto de amplitudes, con * para las conjugadas."""
    return ' '.join(f'E{abs(k)}' + ('*' if k < 0 else '') for k in mc)

frecuencias = sorted(grupos)
positivas = [s for s in frecuencias if s > 0]
print(f'Ternas ordenadas en total: {sum(sum(g.values()) for g in grupos.values())} (debe ser 216)')
print(f'Frecuencias distintas: {len(frecuencias)}  (positivas: {len(positivas)}, '
      f'negativas: {len(frecuencias) - len(positivas)}, cero: {int(0.0 in grupos)})')
print()
print(f'{"frecuencia":>16s} {"valor":>9s}   términos  [factor D]')
factores = set()
for s in positivas:
    mcs = grupos[s]
    # la etiqueta de frecuencia se toma del multiconjunto "propio" (sin pares k,-k)
    nombre = min((etiqueta_frec(mc) for mc in mcs), key=len)
    terminos = ', '.join(f'{etiqueta_amp(mc)} [{n}]' for mc, n in
                         sorted(mcs.items(), key=lambda it: it[1]))
    factores.update(mcs.values())
    print(f'{nombre:>16s} {s:9.5f}   {terminos}')
print()
print('Factores de degeneración que aparecen:', sorted(factores))
