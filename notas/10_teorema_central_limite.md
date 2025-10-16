# 10 - Teorema Central del Límite

## Introducción
El Teorema Central del Límite (TCL) justifica la ubicuidad de la distribución normal en estadística, explicando cómo sumas de variables aleatorias se aproximan a ella, como se detalla en el libro de Liliana Blanco.

## Conceptos Clave

### Enunciado Básico
- Para variables iid X_1, ..., X_n con media μ y varianza σ^2 finitas, la suma estandarizada (∑ X_i - nμ) / (σ √n) converge en distribución a N(0,1).
- Versión para promedios: √n ( \bar{X}_n - μ ) / σ → N(0,1).

### Condiciones
- Variables independientes e idénticamente distribuidas.
- Esperanza y varianza finitas (condición de Lindeberg para generalizaciones).

## Fórmulas Importantes
- Forma estandarizada: Z_n = (S_n - E[S_n]) / √Var(S_n) → N(0,1)
- Aproximación normal para grandes n.

## Ejemplos
- Promedio de resultados de dados se aproxima a normal.
- Errores en mediciones independientes.

## Ejercicios de Estudio
1. Enuncia el Teorema Central del Límite.
2. Aplica el TCL a una distribución no normal como la exponencial.
3. Explica por qué es fundamental en inferencia estadística.
4. Describe cómo usar el TCL para aproximar probabilidades.

## Recursos Adicionales
- Libro: "Probabilidad" de Liliana Blanco (capítulos sobre teoremas límite).
- Videos: StatQuest - Teorema Central del Límite.