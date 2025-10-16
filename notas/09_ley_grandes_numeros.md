# 09 - Ley de Grandes Números

## Introducción
La Ley de Grandes Números (LGN) es un pilar de la estadística que garantiza la convergencia de promedios muestrales a la media poblacional, un tema central en el libro de Liliana Blanco.

## Conceptos Clave

### LGN Débil
- El promedio (1/n) ∑_{i=1}^n X_i converge en probabilidad a E[X].
- Requiere variables independientes e idénticamente distribuidas (iid) con esperanza finita.

### LGN Fuerte
- El promedio converge casi seguramente a E[X].
- Más fuerte que la versión débil; requiere condiciones adicionales como varianza finita.

## Fórmulas Importantes
- Forma general: \bar{X}_n \to \mu en probabilidad (débil) o casi seguramente (fuerte).
- Condiciones: X_i iid, E[|X_i|] < ∞ (débil); Var(X_i) < ∞ (fuerte).

## Ejemplos
- Promedio de lanzamientos de moneda converge a 0.5.
- Estimación de probabilidades mediante frecuencias relativas.

## Ejercicios de Estudio
1. Enuncia la Ley de Grandes Números débil.
2. Proporciona un contraejemplo si las variables no son independientes.
3. Relaciona la LGN con la desigualdad de Chebyshev.
4. Explica la diferencia entre versión débil y fuerte.

## Recursos Adicionales
- Libro: "Probabilidad" de Liliana Blanco (capítulos sobre leyes de grandes números).
- Videos: Khan Academy - Ley de Grandes Números.