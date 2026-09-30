# Tarea 1 — Punto 4: Saleh 5.2-1 (a) — Clasificación de un medio dieléctrico

**Enunciado** (Saleh & Teich, *Fundamentals of Photonics*, 2.ª ed., Problemas del cap. 5,
p. 195 del libro = p. 217 del PDF). Identificar el medio descrito por la ecuación siguiente en
cuanto a linealidad, dispersividad, dispersividad espacial y homogeneidad. Se supone que todos
los medios son isótropos:

$$ \mathcal{P} = \epsilon_0 \chi\, \mathcal{E} - a\, \nabla \times \mathcal{E}, \qquad \chi,\ a \ \text{constantes}. $$

## Criterios (definiciones de Saleh, §5.2, p. 156)

- **Lineal:** 𝒫(r, t) está relacionado linealmente con ℰ(r, t), así que vale la superposición.
- **No dispersivo:** la respuesta es instantánea, es decir, 𝒫 en el instante t depende solo de ℰ
  en ese mismo instante.
- **Homogéneo:** la relación entre 𝒫 y ℰ no depende de la posición r.
- **Isótropo:** la relación no depende de la dirección de ℰ; en ese caso 𝒫 ∥ ℰ.
- **Espacialmente no dispersivo:** la relación es local, es decir, 𝒫 en r depende solo de ℰ en ese
  mismo punto r. Los medios ópticamente activos (§6.4A) son espacialmente dispersivos.

## Solución

**1. Linealidad: lineal.** El rotacional es un operador lineal:

$$ \nabla\times(c_1\mathcal{E}_1 + c_2\mathcal{E}_2) = c_1\nabla\times\mathcal{E}_1 + c_2\nabla\times\mathcal{E}_2 . $$

Por tanto, si ℰ₁ → 𝒫₁ y ℰ₂ → 𝒫₂, entonces c₁ℰ₁ + c₂ℰ₂ → c₁𝒫₁ + c₂𝒫₂ y se cumple la
superposición. En cambio, en el inciso (b) el término 𝒫² sí la rompe.

> Nota sobre el razonamiento: ∇×ℰ **no** es un campo independiente de ℰ. Está completamente
> determinado por ℰ y, por Faraday, ∇×ℰ = −μ₀ ∂ℋ/∂t. Además, que ℰ no se pueda recuperar a partir
> de su rotacional no interviene en la linealidad. Lo que decide la linealidad es que el
> operador sea lineal.

**2. Dispersión temporal: no dispersivo.** No aparecen derivadas temporales ni una convolución en
t como en (5.2-23). Por eso 𝒫(r, t) depende de ℰ solo en el mismo instante t y la respuesta no
tiene memoria.

**3. Dispersión espacial: espacialmente dispersivo.** ∇×ℰ contiene derivadas espaciales, y una
derivada en r depende de los valores de ℰ en un entorno de r. La relación es **no local**. Para
verlo mejor, se toma una onda plana monocromática, ℰ = Re{E₀ exp(jωt − jk·r)}. Con ella
∇× → −jk×, y la relación entre amplitudes complejas queda

$$ \mathbf{P} = \epsilon_0\chi\,\mathbf{E} + j\,a\,\mathbf{k}\times\mathbf{E} . $$

La respuesta depende del **vector de onda k**. Del mismo modo que la dispersión temporal
corresponde a una dependencia en ω, la dispersión espacial corresponde a una dependencia en k.

**4. Homogeneidad: homogéneo.** χ y a son constantes, así que la relación es la misma en todo r.

**5. Isotropía: isótropo (lo supone el enunciado), con un matiz.** El término k×E es perpendicular
a E, de modo que 𝒫 y ℰ no son estrictamente paralelos, como exige la definición de la p. 156.
Aun así, ∇× no privilegia ninguna dirección, porque es invariante ante rotaciones, y el medio no
tiene ejes propios. Lo que se rompe es la simetría de inversión: *a* actúa como una constante
quiral. Esta relación constitutiva es el modelo de un **medio ópticamente activo** (quiral), que
Saleh cita justamente como ejemplo de medio espacialmente dispersivo.

## Resultado

| Propiedad | Clasificación |
|---|---|
| Linealidad | Lineal |
| Dispersión temporal | No dispersivo |
| Dispersión espacial | **Espacialmente dispersivo** |
| Homogeneidad | Homogéneo |
| Isotropía | Isótropo (supuesto; medio quiral / ópticamente activo) |
