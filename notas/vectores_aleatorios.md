# Guía de Estudio: Vectores Aleatorios

## Introducción
Los vectores aleatorios extienden las variables aleatorias a múltiples dimensiones, permitiendo modelar dependencias entre variables.

## Conceptos Clave

### Definición
- Un vector aleatorio (X,Y) donde cada componente es una variable aleatoria.
- Distribución conjunta: F(x,y) = P(X≤x, Y≤y).

### Distribuciones Marginales y Condicionales
- Marginal: P(X=x) = ∑ P(X=x, Y=y)
- Condicional: P(X=x|Y=y) = P(X=x,Y=y) / P(Y=y)

### Método Jacobiano
- Técnica para transformar variables aleatorias y encontrar nuevas densidades.

## Fórmulas Importantes
- Covarianza: Cov(X,Y) = E[XY] - E[X]E[Y]
- Correlación: ρ = Cov(X,Y) / (σ_X σ_Y)

## Ejemplos
- Posición (X,Y) de un punto aleatorio en un círculo.

## Código Relacionado en el Repositorio
- `random_walks/coordenada.py`: Maneja coordenadas en 2D, similar a vectores aleatorios.
- `statistics/calculo_pi.py`: Usa coordenadas aleatorias para estimación.

## Ejercicios de Estudio
1. Calcula la distribución marginal de X en un vector (X,Y) uniforme en un cuadrado.
2. Encuentra la covarianza de dos variables normales.
3. Aplica el método Jacobiano a una transformación simple.
4. Interpreta la independencia en vectores aleatorios.

## Recursos Adicionales
- Libros: "Multivariate Statistics" de Anderson.
- Videos: Coursera - Multivariate Probability.