# 02 - Variables Aleatorias y Funciones de Distribución

## Introducción
Una variable aleatoria es una función que asigna un número real a cada resultado de un experimento aleatorio. Las funciones de distribución permiten describir completamente su comportamiento probabilístico, como se detalla en textos como el de Liliana Blanco.

## Conceptos Clave

### Variable Aleatoria
- **Discreta**: Valores aislados o contables (e.g., conteo de eventos).
- **Continua**: Valores en un continuo (e.g., mediciones).

### Función de Probabilidad (PMF para discretas)
- P(X = x_k) = p_k, con ∑ p_k = 1.
- Propiedades básicas de probabilidad.

### Función de Densidad de Probabilidad (PDF para continuas)
- f(x) ≥ 0, ∫_{-∞}^{∞} f(x) dx = 1.
- Probabilidad en intervalos mediante integración.

### Función de Distribución Acumulativa (CDF)
- F(x) = P(X ≤ x)
- Para discretas: suma de probabilidades hasta x.
- Para continuas: integral de la densidad hasta x.
- Propiedades: no decreciente, límites 0 y 1.

## Fórmulas Importantes
- CDF: F(x) = P(X ≤ x)
- Para discretas: P(X > x) = 1 - F(x)
- Para continuas: f(x) = F'(x) donde existe

## Ejemplos
- Variable discreta: número de éxitos en n ensayos Bernoulli.
- Variable continua: tiempo hasta el siguiente evento en un proceso Poisson.

## Ejercicios de Estudio
1. Calcula P(X ≤ 3) para una distribución uniforme discreta en {1,2,3,4,5}.
2. Determina la CDF de una variable exponencial con parámetro λ.
3. Explica la diferencia entre PMF y PDF.
4. Construye la CDF para una variable binomial.

## Recursos Adicionales
- Libro: "Probabilidad" de Liliana Blanco (capítulos sobre variables aleatorias).
- Videos: MIT OpenCourseWare - Variables Aleatorias.