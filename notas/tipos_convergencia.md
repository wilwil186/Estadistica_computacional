# Guía de Estudio: Tipos de Convergencia

## Introducción
La convergencia describe cómo las distribuciones o estadísticos se aproximan a un límite cuando el tamaño de muestra aumenta.

## Conceptos Clave

### Convergencia en Distribución
- F_n(x) → F(x) para continuidad de F.
- Ley de los Grandes Números débil.

### Convergencia en Probabilidad
- P(|X_n - X| > ε) → 0 para todo ε > 0.

### Convergencia Casi Segura
- P(límite X_n = X) = 1.

### Convergencia en Media Cuadrática
- E[(X_n - X)^2] → 0.

## Fórmulas Importantes
- Relaciones: Casi segura ⇒ En probabilidad ⇒ En distribución.

## Ejemplos
- Promedio muestral converge a la media poblacional.

## Código Relacionado en el Repositorio
- `statistics/calculo_pi.py`: Demuestra convergencia en simulaciones de Monte Carlo.

## Ejercicios de Estudio
1. Explica la diferencia entre convergencia en probabilidad y casi segura.
2. Da un ejemplo de cada tipo.
3. Relaciona con TCL.
4. Simula convergencia con código.

## Recursos Adicionales
- Libros: "Asymptotic Statistics" de van der Vaart.
- Videos: MIT - Modes of Convergence.