# 06 - Función Generadora de Momentos y Función Característica

## Introducción
La función generadora de momentos y su análoga característica son herramientas esenciales para derivar momentos y propiedades de distribuciones, como se detalla en textos avanzados como el de Liliana Blanco.

## Conceptos Clave

### Función Generadora de Momentos (MGF)
- Definida como M_X(t) = E[e^{tX}] = ∑ e^{t x_k} p_k (discreta) o ∫ e^{t x} f(x) dx (continua).
- Única para cada distribución; si existe, identifica la distribución.
- Derivadas en t=0 dan momentos: M^{(k)}(0) = E[X^k].

### Función Característica
- ϕ_X(t) = E[e^{i t X}], versión compleja de la MGF.
- Siempre existe (por desigualdad triangular), útil para distribuciones sin MGF definida (e.g., Cauchy, log-normal).

## Fórmulas Importantes
- Expansión de Taylor: M(t) = ∑_{k=0}^∞ (E[X^k] / k!) t^k
- Relación: ϕ(t) = M(i t)
- Para independencia: M_{X+Y}(t) = M_X(t) M_Y(t) si independientes

## Ejemplos
- MGF de distribución exponencial: M(t) = λ / (λ - t) para t < λ
- Función característica de normal estándar: ϕ(t) = e^{-t^2 / 2}

## Ejercicios de Estudio
1. Deriva la MGF de una distribución normal N(μ, σ^2).
2. Usa la MGF para encontrar la varianza de una binomial.
3. Compara MGF y función característica en términos de existencia.
4. Aplica la MGF para probar independencia de sumas.

## Recursos Adicionales
- Libro: "Probabilidad" de Liliana Blanco (capítulos sobre funciones generadoras).
- Videos: NPTEL - Funciones Generadoras de Momentos.