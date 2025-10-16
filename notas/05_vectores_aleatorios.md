# 05 - Vectores Aleatorios

## Introducción
Los vectores aleatorios permiten estudiar múltiples variables aleatorias simultáneamente, capturando dependencias y covarianzas, un tema avanzado en probabilidad como se presenta en el libro de Liliana Blanco.

## Conceptos Clave

### Definición
- Vector aleatorio: Tupla (X_1, X_2, ..., X_n) de variables aleatorias.
- Función de distribución conjunta: F(x_1, ..., x_n) = P(X_1 ≤ x_1, ..., X_n ≤ x_n).

### Distribuciones Marginales
- Distribución de una componente: Integrando o sumando sobre las otras.
- Ejemplo: Para (X,Y), marginal de X es P(X ≤ x) = ∑_y P(X=x, Y=y).

### Distribuciones Condicionales
- P(X ≤ x | Y = y) = P(X ≤ x, Y = y) / P(Y = y).
- Útil para modelar dependencias.

### Método de Transformación (Jacobiano)
- Técnica para encontrar la distribución de funciones de vectores aleatorios mediante el determinante Jacobiano.

## Fórmulas Importantes
- Covarianza: Cov(X,Y) = E[XY] - E[X]E[Y]
- Coeficiente de correlación: ρ_{XY} = Cov(X,Y) / (σ_X σ_Y)
- Para independencia: F(x,y) = F_X(x) F_Y(y)

## Ejemplos
- Posición bidimensional en un plano aleatorio.
- Vectores normales multivariados.

## Ejercicios de Estudio
1. Calcula la marginal de X en un vector uniforme sobre un cuadrado.
2. Determina la covarianza entre dos variables correlacionadas.
3. Aplica el método Jacobiano a una transformación lineal.
4. Explica cuándo dos componentes son independientes.

## Recursos Adicionales
- Libro: "Probabilidad" de Liliana Blanco (capítulos sobre vectores aleatorios).
- Videos: Coursera - Vectores Aleatorios.