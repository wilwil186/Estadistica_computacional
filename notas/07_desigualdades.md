# 07 - Desigualdades (Markov, Chebyshev)

## Introducción
Las desigualdades de Markov y Chebyshev proporcionan límites superiores para probabilidades sin asumir una distribución específica, herramientas clave en análisis probabilístico como se presenta en el libro de Liliana Blanco.

## Conceptos Clave

### Desigualdad de Markov
- Para variable aleatoria no negativa X y a > 0: P(X ≥ a) ≤ E[X] / a.
- Útil para acotar colas superiores cuando se conoce la media.

### Desigualdad de Chebyshev
- Para cualquier variable con media μ y varianza σ^2: P(|X - μ| ≥ k σ) ≤ 1/k^2 para k > 0.
- Proporciona límites en términos de desviaciones estándar.

## Fórmulas Importantes
- Markov: P(X ≥ a) ≤ E[X]/a (para X ≥ 0)
- Chebyshev: P(|X - μ| ≥ ε) ≤ Var(X) / ε^2

## Ejemplos
- Acotar la probabilidad de que una suma exceda su media.
- Límites en distribuciones desconocidas usando solo momentos.

## Ejercicios de Estudio
1. Aplica la desigualdad de Markov a una variable exponencial.
2. Usa Chebyshev para estimar P(|X - μ| > 2σ).
3. Compara la fuerza de ambas desigualdades.
4. Encuentra un límite para la probabilidad de extremos en un dado.

## Recursos Adicionales
- Libro: "Probabilidad" de Liliana Blanco (capítulos sobre desigualdades).
- Videos: Khan Academy - Desigualdades en Probabilidad.