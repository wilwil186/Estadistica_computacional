# Guía de Estudio: Desigualdades (Markov, Chebyshev)

## Introducción
Las desigualdades proporcionan límites superiores para probabilidades, útiles cuando no se conoce la distribución exacta.

## Conceptos Clave

### Desigualdad de Markov
- P(|X| ≥ a) ≤ E[|X|]/a para a > 0.
- Aplica a variables no negativas.

### Desigualdad de Chebyshev
- P(|X - μ| ≥ kσ) ≤ 1/k^2.
- Más fuerte, aplica a cualquier variable con varianza.

## Fórmulas Importantes
- Markov: P(X ≥ a) ≤ E[X]/a
- Chebyshev: P(|X - μ| ≥ ε) ≤ Var(X)/ε^2

## Ejemplos
- Límites en colas de distribuciones.

## Código Relacionado en el Repositorio
- `statistics/estadisticas.py`: Calcula varianza, usada en Chebyshev.

## Ejercicios de Estudio
1. Aplica Markov a una variable exponencial.
2. Usa Chebyshev para estimar P(|X| > 2σ).
3. Compara ambas desigualdades.
4. Encuentra un límite para la probabilidad en un dado.

## Recursos Adicionales
- Libros: "Concentration Inequalities" de Boucheron.
- Videos: Khan Academy - Chebyshev's Inequality.