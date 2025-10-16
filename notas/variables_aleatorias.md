# Guía de Estudio: Variables Aleatorias y Funciones de Distribución

## Introducción
Una variable aleatoria asigna un número real a cada resultado de un experimento aleatorio. Las funciones de distribución describen su comportamiento probabilístico.

## Conceptos Clave

### Variable Aleatoria
- **Discreta**: Toma valores contables (e.g., número de éxitos en ensayos).
- **Continua**: Toma cualquier valor en un intervalo (e.g., tiempo de espera).

### Función de Probabilidad (para discretas)
- P(X = x) para cada x posible.
- Propiedades: 0 ≤ P(X = x) ≤ 1, ∑ P(X = x) = 1.

### Función de Densidad (para continuas)
- f(x) ≥ 0, ∫ f(x) dx = 1.
- P(a ≤ X ≤ b) = ∫_a^b f(x) dx.

### Función de Distribución Acumulativa (FDA)
- F(x) = P(X ≤ x)
- Para discretas: suma hasta x.
- Para continuas: integral hasta x.

## Fórmulas Importantes
- FDA: F(x) = P(X ≤ x)
- Para discretas: P(X > x) = 1 - F(x)
- Para continuas: f(x) = dF(x)/dx

## Ejemplos
- Variable discreta: X = número de caras en 2 lanzamientos de moneda.
- Variable continua: X = altura de estudiantes.

## Código Relacionado en el Repositorio
- `statistics/estadisticas.py`: Funciones para calcular media y varianza, útiles para variables aleatorias.
- `statistics/probabilidades.py`: Simulación de variables discretas con dados.

## Ejercicios de Estudio
1. Dada una distribución uniforme discreta, calcula P(X ≤ 3).
2. Encuentra la FDA de una variable exponencial.
3. Simula una variable aleatoria binomial usando código.
4. Explica la diferencia entre PMF y PDF.

## Recursos Adicionales
- Libros: "Introduction to Probability" de Bertsekas.
- Videos: MIT OpenCourseWare - Probability.