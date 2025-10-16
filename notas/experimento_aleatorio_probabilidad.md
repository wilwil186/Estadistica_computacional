# Guía de Estudio: Experimento Aleatorio, Probabilidad, Probabilidad Condicional, Independencia

## Introducción
Los conceptos fundamentales de la probabilidad comienzan con la definición de experimentos aleatorios y la asignación de probabilidades a los eventos. Estos forman la base para análisis más avanzados como la probabilidad condicional y la independencia.

## Conceptos Clave

### Experimento Aleatorio
- Un experimento que, al repetirse bajo las mismas condiciones, puede producir diferentes resultados impredecibles.
- Ejemplos: lanzar un dado, seleccionar una carta de una baraja.

### Espacio Muestral y Eventos
- **Espacio muestral (S)**: Conjunto de todos los posibles resultados de un experimento.
- **Evento**: Subconjunto del espacio muestral.
- Eventos simples, compuestos, mutuamente excluyentes, complementarios.

### Probabilidad
- Medida numérica de la likelihood de que ocurra un evento.
- Propiedades:
  - P(S) = 1
  - 0 ≤ P(E) ≤ 1 para cualquier evento E
  - P(A ∪ B) = P(A) + P(B) si A y B son mutuamente excluyentes

### Probabilidad Condicional
- Probabilidad de un evento A dado que B ha ocurrido: P(A|B) = P(A ∩ B) / P(B), donde P(B) > 0.
- Útil para actualizar probabilidades con nueva información.

### Independencia
- Dos eventos A y B son independientes si P(A ∩ B) = P(A) * P(B).
- Implica que la ocurrencia de uno no afecta al otro.

## Fórmulas Importantes
- Probabilidad clásica: P(E) = número de casos favorables / número de casos posibles.
- Probabilidad condicional: P(A|B) = P(A ∩ B) / P(B)
- Eventos independientes: P(A|B) = P(A)

## Ejemplos
- Lanzar un dado justo: P(6) = 1/6
- Seleccionar una carta: P(as de espadas) = 1/52
- Probabilidad de lluvia dado que está nublado: P(lluvia|nublado) = 0.8

## Código Relacionado en el Repositorio
- `cards/barajas.py`: Simulación de probabilidades con cartas (e.g., probabilidad de pares).
- `statistics/probabilidades.py`: Simulación de probabilidades con dados.

## Ejercicios de Estudio
1. Define un experimento aleatorio simple y su espacio muestral.
2. Calcula la probabilidad de obtener al menos un 6 en dos lanzamientos de dado.
3. Dados dos eventos independientes, verifica si cumplen la condición de independencia.
4. Explica cómo la probabilidad condicional cambia con nueva evidencia.

## Recursos Adicionales
- Libros: "Probability and Statistics" de DeGroot.
- Videos: Khan Academy - Introducción a la Probabilidad.