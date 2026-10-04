# Figuras de resultados

Implementación: `src/plotting.py` (`apply_style`, `save_fig`) y
`simulaciones/pruebas/ring2_espectrometro/generar_figuras.py`.

## Convenciones

- **PNG y PDF vectorial** de cada figura, vía `save_fig()`. El PNG para revisar y para
  presentaciones; el PDF entra en la tesis sin perder calidad.
- Nombres **deterministas**: volver a correr el script sobrescribe, no acumula variantes.
- **El color codifica el solver; el trazo, la geometría.** Azul `#2a78d6` = FDTD 3D,
  naranja `#eb6834` = varFDTD; continuo = una geometría, discontinuo = la otra. Así la
  identidad de cada curva no depende solo del color y las figuras siguen siendo legibles
  impresas en blanco y negro.
- Rejilla recesiva, ejes finos, anotaciones con caja blanca sobre la curva.
- Las figuras se generan **desde los `.h5`, sin volver a simular**. Un script de figuras
  debe poder correrse cien veces sin tocar el solver.

## Una figura por magnitud

Superponer todo en un gráfico esconde justo lo que se quiere mostrar. Una figura por
magnitud, cada una con la anotación que la explica:

| Figura | Qué lleva anotado |
|---|---|
| λ de resonancia | drop y through juntos, cada λ_res marcada, y la λ de diseño como referencia |
| Extinción | el notch del through, el nivel fuera de resonancia, `T_min` y el **ER en dB** |
| FWHM y Q | zoom a la resonancia, los cruces a media altura marcados, flecha doble y **FWHM → Q** |
| FSR | las dos resonancias, flecha doble entre ellas, **FSR** y el n_g implícito |

Y para el conjunto: una figura con **todos los casos superpuestos** (drop y through en
paneles separados) más **tablas resumen** — valores absolutos y desviación contra el
diseño, esta última coloreada por umbral.

## Anotar es explicar

Cada anotación debe llevar **el valor medido y el de referencia**:

```
FWHM = 0.4968 nm
Q = λ_res/FWHM = 3130
diseño: 0,5000 nm · Q 3100
```

Sin la línea de referencia, el lector no sabe si 3130 es bueno o malo.

## Dónde van

Una carpeta `figuras/` dentro de cada carpeta de simulación para las figuras de ese caso,
y una `figuras/` a nivel del estudio para las comparativas y las tablas.

Los `.h5` no se versionan (ver `.gitignore`); las figuras **sí**, junto con los scripts que
las generan y las cifras en `notas.md` / `ESTADO.md`. Con eso cualquier resultado se
reconstruye volviendo a correr el barrido.
