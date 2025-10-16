# Guía de Estudio: Esperanza, Varianza, Momentos

## Introducción
La esperanza y la varianza son medidas centrales que resumen el comportamiento de una variable aleatoria. Los momentos proporcionan información adicional sobre su distribución.

## Conceptos Clave

### Esperanza (Media)
- Valor esperado de una variable aleatoria: E[X] = ∑ x P(X = x) (discreta) o ∫ x f(x) dx (continua).
- Propiedad lineal: E[aX + b] = a E[X] + b.

### Varianza
- Medida de dispersión: Var(X) = E[(X - μ)^2] = E[X^2] - (E[X])^2.
- Desviación estándar: σ = √Var(X).

### Momentos
- Momento k-ésimo: μ_k = E[X^k].
- Momento central: E[(X - μ)^k].

## Fórmulas Importantes
- E[X] = μ
- Var(X) = σ^2 = E[X^2] - μ^2
- Para distribución normal: ~N(μ, σ^2)

## Ejemplos
- Esperanza de un dado: E[X] = (1+2+3+4+5+6)/6 = 3.5
- Varianza de una moneda: Var(X) = p(1-p) para Bernoulli.

## Código Relacionado en el Repositorio
- `statistics/estadisticas.py`: Implementa funciones para calcular media y varianza directamente.
- `statistics/calculo_pi.py`: Usa media y desviación estándar en simulaciones.

## Ejercicios de Estudio
1. Calcula E[X] y Var(X) para una distribución binomial.
2. Demuestra que Var(aX + b) = a^2 Var(X).
3. Encuentra los primeros momentos de una distribución uniforme.
4. Interpreta la varianza en un contexto real.

## Recursos Adicionales
- Libros: "Mathematical Statistics" de Hogg.
- Videos: StatQuest - Mean and Variance.