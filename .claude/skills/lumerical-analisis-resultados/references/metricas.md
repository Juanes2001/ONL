# Cómo se mide cada magnitud

Implementación de referencia: `simulaciones/pruebas/ring2_espectrometro/generar_figuras.py`.

## Localizar las resonancias

Máximos locales del drop por encima del 20 % del máximo, agrupando muestras contiguas
para no contar dos veces la misma meseta.

```python
def picos(lam, td):
    umbral = 0.2 * np.nanmax(td)
    crudos = [i for i in range(1, td.size - 1)
              if td[i] > umbral and td[i] >= td[i-1] and td[i] >= td[i+1]]
    sel = []
    for i in crudos:
        if sel and i - sel[-1] < 5:          # misma meseta: quedarse con el mayor
            if td[i] > td[sel[-1]]:
                sel[-1] = i
        else:
            sel.append(i)
    return sel
```

## FWHM — interpolando, siempre

```python
def cruces_media_altura(lam, y, i):
    """λ a media altura a cada lado del pico i, interpolando linealmente."""
    half = y[i] / 2.0
    l = i
    while l > 0 and y[l] > half:
        l -= 1
    r = i
    while r < y.size - 1 and y[r] > half:
        r += 1
    def interp(a, b):
        if y[b] == y[a]:
            return lam[b]
        return lam[a] + (half - y[a]) * (lam[b] - lam[a]) / (y[b] - y[a])
    return interp(l, l + 1), interp(r, r - 1), half

lo, hi, half = cruces_media_altura(lam, td, i)
fwhm = hi - lo
Q = lam[i] / fwhm
```

Sin interpolar, el error de cuantización llega a 2 muestras. Sobre un FWHM de 500 pm
muestreado a 20 pm son **8 % de error en Q** — suficiente para invertir el signo de la
conclusión.

## Las demás

```python
# Extinción del notch, respecto al nivel fuera de resonancia
t_off  = float(np.nanmax(tt))
er_db  = 10.0 * np.log10(t_off / max(tt[i], 1e-12))

# FSR: media de las diferencias entre resonancias consecutivas (≥2 picos)
fsr = float(np.mean(np.diff(lam[sel])))

# n_g a partir del FSR; L es la longitud del anillo, λ_c el centro de las resonancias
ng = (lam_c * 1e-9)**2 / (fsr * 1e-9 * L_um * 1e-6)

# n_eff a partir del orden de resonancia m (entero, el de diseño)
neff = m * lam_res * 1e-9 / (L_um * 1e-6)
```

**El orden `m`** se obtiene del diseño: `m = round(n_eff_diseño · L / λ_diseño)`. Que dé
entero exacto en toda una familia de componentes es además una buena prueba de coherencia
de las tablas de parámetros — un valor que se sale delata un typo.

## Balance de potencia

`T_through + T_drop` en resonancia dice cuánta potencia se pierde. Compáralo con lo
esperable de la atenuación de diseño:

- Pérdida por vuelta = `α [dB/m] · L [m]`, convertida a fracción.
- En resonancia la luz da del orden de `F/π` vueltas, con `F = FSR/FWHM` la finesse.

Si la pérdida observada es mucho mayor que `pérdida_por_vuelta × vueltas`, sobra
disipación: radiación por curvatura mal modelada, o discretización del gap.
