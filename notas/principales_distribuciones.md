# Guía de Estudio: Principales Distribuciones de Probabilidad

## Introducción
Existen varias distribuciones estándar que modelan fenómenos comunes en estadística y probabilidad. Cada una tiene parámetros específicos y aplicaciones.

## Conceptos Clave

### Distribuciones Discretas
- **Bernoulli**: Éxito/fallo, p = P(éxito).
- **Binomial**: Número de éxitos en n ensayos, parámetros n, p.
- **Poisson**: Número de eventos en un intervalo, λ = tasa media.

### Distribuciones Continuas
- **Uniforme**: Valores igualmente probables en [a,b].
- **Exponencial**: Tiempo entre eventos, λ = tasa.
- **Normal (Gaussiana)**: Simétrica, parámetros μ, σ^2.
- **Gamma, Beta, etc.**: Para casos más complejos.

## Fórmulas Importantes
- Binomial: P(X=k) = C(n,k) p^k (1-p)^{n-k}
- Poisson: P(X=k) = e^{-λ} λ^k / k!
- Normal: f(x) = (1/(σ√(2π))) exp(-(x-μ)^2/(2σ^2))

## Ejemplos
- Número de llamadas en una hora: Poisson(λ=5).
- Altura humana: Normal(μ=170, σ=10).

## Código Relacionado en el Repositorio
- `statistics/probabilidades.py`: Simula distribuciones discretas como dados (uniforme discreta).
- `random_walks/`: Relacionado con procesos estocásticos que pueden modelarse con distribuciones.

## Ejercicios de Estudio
1. Calcula P(X≥3) para Binomial(n=5, p=0.5).
2. Encuentra la media y varianza de una distribución exponencial.
3. Simula una distribución normal usando código.
4. Elige una distribución para modelar el tiempo de vida de un producto.

## Recursos Adicionales
- Libros: "Probability Distributions" en Wikipedia.
- Videos: Khan Academy - Distribuciones de Probabilidad.