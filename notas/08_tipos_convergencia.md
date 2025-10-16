# 08 - Tipos de Convergencia

## Introducción
Los tipos de convergencia describen cómo secuencias de variables aleatorias se aproximan a un límite, un concepto fundamental en teoría de la probabilidad y estadística, como se explora en el libro de Liliana Blanco.

## Conceptos Clave

### Convergencia en Distribución (Débil)
- Las funciones de distribución F_n convergen a F en puntos de continuidad.
- Relacionada con la Ley de los Grandes Números débil.

### Convergencia en Probabilidad
- P(|X_n - X| > ε) → 0 para todo ε > 0.
- X_n se acerca a X "en la mayoría de los casos".

### Convergencia Casi Segura (Casi Siempre)
- P(ω: X_n(ω) → X(ω)) = 1.
- Convergencia punto a punto con probabilidad 1.

### Convergencia en Media p-ésima (e.g., L^2)
- E[|X_n - X|^p] → 0 para p ≥ 1.
- Más fuerte que en probabilidad para p > 1.

## Fórmulas Importantes
- Jerarquía: Casi segura ⇒ En probabilidad ⇒ En distribución (generalmente).
- Para media cuadrática: E[(X_n - X)^2] → 0.

## Ejemplos
- Promedio muestral converge en probabilidad a la media poblacional.
- Secuencias que convergen casi seguramente pero no en media.

## Ejercicios de Estudio
1. Explica la diferencia entre convergencia en probabilidad y casi segura.
2. Proporciona un ejemplo de convergencia en distribución.
3. Relaciona con el Teorema Central del Límite.
4. Describe cómo verificar convergencia en un experimento.

## Recursos Adicionales
- Libro: "Probabilidad" de Liliana Blanco (capítulos sobre convergencia).
- Videos: MIT - Tipos de Convergencia.