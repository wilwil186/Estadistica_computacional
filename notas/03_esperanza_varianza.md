# 03 - Esperanza, Varianza, Momentos

## Introducción
La esperanza y la varianza son parámetros fundamentales que caracterizan la ubicación y dispersión de una variable aleatoria. Los momentos extienden estos conceptos a órdenes superiores, como se explica en obras como "Probabilidad" de Liliana Blanco.

## Conceptos Clave

### Esperanza Matemática (Media)
- Valor promedio ponderado: E[X] = ∑ x_k p_k (discreta) o ∫ x f(x) dx (continua).
- Propiedades: E[c] = c, E[aX + b] = a E[X] + b, linealidad.

### Varianza
- Medida de variabilidad: Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2.
- Desviación estándar: σ = √Var(X), en mismas unidades que X.

### Momentos
- Momento de orden k: μ_k = E[X^k].
- Momentos centrales: ν_k = E[(X - μ)^k].
- Útiles para describir forma de la distribución (asimetría, curtosis).

## Fórmulas Importantes
- E[X] = μ
- Var(X) = E[X^2] - μ^2
- Desviación estándar: σ = √Var(X)
- Para Bernoulli: E[X] = p, Var(X) = p(1-p)

## Ejemplos
- Esperanza de un dado justo: μ = 3.5
- Varianza de una moneda sesgada: Var(X) = p q

## Ejercicios de Estudio
1. Calcula E[X] y Var(X) para una distribución binomial B(n,p).
2. Demuestra que Var(aX + b) = a^2 Var(X).
3. Encuentra los momentos centrales de una distribución normal estándar.
4. Interpreta el significado de la varianza en un experimento real.

## Recursos Adicionales
- Libro: "Probabilidad" de Liliana Blanco (capítulos sobre esperanza y varianza).
- Videos: StatQuest - Esperanza y Varianza.