# Guía de Estudio: Función Generadora de Momentos y Función Característica

## Introducción
Estas funciones son herramientas poderosas para obtener momentos de distribuciones y facilitar cálculos en probabilidad.

## Conceptos Clave

### Función Generadora de Momentos (MGF)
- M(t) = E[e^{tX}] = ∑ e^{tx} P(X=x) (discreta) o ∫ e^{tx} f(x) dx (continua).
- Única para cada distribución.
- Momentos: μ_k = M^{(k)}(0)

### Función Característica
- ϕ(t) = E[e^{itX}], versión compleja de MGF.
- Siempre existe, útil para distribuciones sin MGF (e.g., Cauchy).

## Fórmulas Importantes
- M(t) = 1 + μ t + (μ_2 / 2!) t^2 + ...
- ϕ(t) = M(it)

## Ejemplos
- MGF de Poisson: e^{λ(e^t - 1)}

## Código Relacionado en el Repositorio
- `statistics/estadisticas.py`: Calcula momentos directamente, relacionados con MGF.

## Ejercicios de Estudio
1. Deriva la MGF de una distribución normal.
2. Usa MGF para encontrar varianza de una binomial.
3. Compara MGF y función característica.
4. Aplica a una distribución conocida en el repo.

## Recursos Adicionales
- Libros: "Probability Theory" de Billingsley.
- Videos: NPTEL - Moment Generating Functions.