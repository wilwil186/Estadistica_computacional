# Guía de Estudio: Ley de Grandes Números

## Introducción
La Ley de Grandes Números (LGN) establece que el promedio de observaciones independientes converge a la esperanza poblacional.

## Conceptos Clave

### LGN Débil
- (1/n) ∑ X_i → E[X] en probabilidad.

### LGN Fuerte
- (1/n) ∑ X_i → E[X] casi seguramente.

## Fórmulas Importantes
- Condiciones: Variables iid con E[|X|] < ∞.

## Ejemplos
- Promedio de lanzamientos de moneda converge a 0.5.

## Código Relacionado en el Repositorio
- `statistics/estadisticas.py`: Base para calcular promedios.
- `statistics/calculo_pi.py`: Usa LGN en estimación de Pi.

## Ejercicios de Estudio
1. Enuncia la LGN débil.
2. Da un contraejemplo si no se cumple independencia.
3. Simula LGN con dados.
4. Relaciona con desigualdades.

## Recursos Adicionales
- Libros: "Probability" de Ross.
- Videos: Khan Academy - Law of Large Numbers.