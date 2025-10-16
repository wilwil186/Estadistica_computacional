# 04 - Principales Distribuciones de Probabilidad

## Introducción
Las distribuciones de probabilidad modelan el comportamiento de variables aleatorias en escenarios comunes. El libro de Liliana Blanco dedica secciones a estas distribuciones clave, destacando sus propiedades y aplicaciones.

## Conceptos Clave

### Distribuciones Discretas
- **Bernoulli**: Modelo para un ensayo con éxito (p) o fracaso (1-p).
- **Binomial**: Suma de ensayos Bernoulli independientes, parámetros n (número de ensayos) y p (probabilidad de éxito).
- **Poisson**: Número de ocurrencias en un intervalo fijo, parámetro λ (tasa promedio).

### Distribuciones Continuas
- **Uniforme**: Todos los valores en [a,b] igualmente probables.
- **Exponencial**: Tiempo entre eventos en un proceso Poisson, parámetro λ.
- **Normal**: Distribución simétrica en forma de campana, parámetros μ (media) y σ^2 (varianza).
- **Otras**: Gamma, Beta, t-Student, etc., para modelados especializados.

## Fórmulas Importantes
- Bernoulli: P(X=1) = p, P(X=0) = 1-p
- Binomial: P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}
- Poisson: P(X=k) = e^{-\lambda} \lambda^k / k!
- Normal: f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-(x-\mu)^2 / (2\sigma^2)}

## Ejemplos
- Número de defectos en un lote: Binomial.
- Tiempo hasta la próxima llamada: Exponencial.
- Mediciones con error aleatorio: Normal.

## Ejercicios de Estudio
1. Calcula P(X ≥ 3) para Binomial(n=5, p=0.5).
2. Determina media y varianza de una distribución exponencial.
3. Describe las propiedades de la distribución normal.
4. Elige una distribución adecuada para modelar el número de llegadas en una cola.

## Recursos Adicionales
- Libro: "Probabilidad" de Liliana Blanco (capítulos sobre distribuciones).
- Videos: Khan Academy - Distribuciones de Probabilidad.