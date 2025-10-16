# Guía de Estudio: Teorema Central del Límite

## Introducción
El Teorema Central del Límite (TCL) explica por qué muchas distribuciones se aproximan a la normal cuando se suman muchas variables.

## Conceptos Clave

### Enunciado
- Suma estandarizada de iid converge a N(0,1): (∑ X_i - nμ) / (σ√n) → N(0,1) en distribución.

### Condiciones
- Variables iid con varianza finita.

## Fórmulas Importantes
- Aproximación: Z ≈ (X̄ - μ) / (σ/√n)

## Ejemplos
- Promedio de dados se aproxima a normal para n grande.

## Código Relacionado en el Repositorio
- `random_walks/camino_aleatorio.py`: Simula procesos que ilustran TCL en caminatas.
- `statistics/calculo_pi.py`: Usa TCL implícitamente en estimaciones.

## Ejercicios de Estudio
1. Enuncia el TCL.
2. Aplica a una distribución no normal.
3. Simula TCL con código.
4. Explica su importancia en estadística.

## Recursos Adicionales
- Libros: "All of Statistics" de Wasserman.
- Videos: StatQuest - Central Limit Theorem.