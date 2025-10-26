# Prova do processo seletivo do mestrado e doutorado direto Pippes - 26/10/2025

## Justifique todos os itens de todas as questões

---

## **Ejercicio 1** (2,25 puntos)

**Enunciado:** En un país determinado, hay dos etnias: la etnia A representa el 60% de la población, y el resto pertenece a la etnia B. El gobierno propone cambios en la ley penal. Entre las personas de la etnia A, el 70% es favorable al cambio, el 20% es contrario y el resto es neutro. Entre los habitantes de la etnia B, el 20% es favorable, el 60% es contrario y el resto es neutro.

### **(a)** Si sorteamos aleatoriamente una persona de ese país, ¿cuál es la probabilidad de que sea de la etnia B y contraria al cambio en la ley penal?

**Solución paso a paso:**

**Paso 1: Identificar las probabilidades dadas**
- P(A) = 0,60 (60% es de etnia A)
- P(B) = 0,40 (40% es de etnia B)

**Paso 2: Probabilidades condicionadas para etnia B**
- P(Favorable | B) = 0,20
- P(Contrario | B) = 0,60
- P(Neutro | B) = 0,20

**Paso 3: Calcular P(B ∩ Contrario)**

Usamos la regla de la multiplicación, ya que queremos la probabilidad de que ocurra tanto B como Contrario, y conocemos P(Contrario | B):

```
P(B ∩ Contrario) = P(B) × P(Contrario | B)
P(B ∩ Contrario) = 0,40 × 0,60 = 0,24
```

**Respuesta: 0,24 o 24%**

---

### **(b)** Si sorteamos aleatoriamente una persona de ese país y observamos que es favorable al cambio en la ley penal, ¿cuál es la probabilidad de que sea de la etnia A?

**Solución paso a paso:**

**Paso 1: Identificar que necesitamos el Teorema de Bayes**

Para encontrar P(A | Favorable), aplicamos el Teorema de Bayes:

```
P(A | Favorable) = P(A ∩ Favorable) / P(Favorable)
```

**Paso 2: Calcular P(A ∩ Favorable)**

```
P(A ∩ Favorable) = P(A) × P(Favorable | A)
P(A ∩ Favorable) = 0,60 × 0,70 = 0,42
```

**Paso 3: Calcular P(Favorable) usando la ley de probabilidad total**

La ley de probabilidad total se aplica porque Favorable puede ocurrir de dos formas mutuamente exclusivas: a través de A o de B.

```
P(Favorable) = P(A) × P(Favorable | A) + P(B) × P(Favorable | B)
P(Favorable) = 0,60 × 0,70 + 0,40 × 0,20
P(Favorable) = 0,42 + 0,08 = 0,50
```

**Paso 4: Aplicar Bayes**

```
P(A | Favorable) = 0,42 / 0,50 = 0,84
```

**Respuesta: 0,84 o 84%**

---

## **Ejercicio 2** (2,75 puntos)

**Enunciado:** Sea X una variable aleatoria continua con soporte en el intervalo (0,1) y función de densidad de probabilidad f(x) = 12x²(1-x). Para esta variable aleatoria, obtenga:

### **(a)** P(X = 0,5)

**Solución:**

Para cualquier variable aleatoria continua, la probabilidad en un punto específico es cero.

**Explicación:** En variables aleatorias continuas, la probabilidad en un punto específico es cero, ya que solo intervalos tienen probabilidad positiva. Esto se debe a que la integral de la función de densidad en un punto único es cero:

```
P(X = c) = ∫ₖᶜ f(x)dx = 0
```

**Respuesta: P(X = 0,5) = 0**

---

### **(b)** P(X < 0,5 | X > 0,3)

**Solución paso a paso:**

**Paso 1: Usar la definición de probabilidad condicional**

La probabilidad condicional se define como la probabilidad del evento dado que el otro ha ocurrido:

```
P(X < 0,5 | X > 0,3) = P(0,3 < X < 0,5) / P(X > 0,3)
```

**Paso 2: Calcular P(0,3 < X < 0,5)**

```
P(0,3 < X < 0,5) = ∫₀.₃⁰·⁵ 12x²(1-x)dx
```

Expandimos: 12x²(1-x) = 12x² - 12x³

```
∫₀.₃⁰·⁵ (12x² - 12x³)dx = [4x³ - 3x⁴]₀.₃⁰·⁵
```

**Paso 3: Evaluar en los límites**

En x = 0,5:
```
4(0,5)³ - 3(0,5)⁴ = 4(0,125) - 3(0,0625) = 0,5 - 0,1875 = 0,3125
```

En x = 0,3:
```
4(0,3)³ - 3(0,3)⁴ = 4(0,027) - 3(0,0081) = 0,108 - 0,0243 = 0,0837
```

```
P(0,3 < X < 0,5) = 0,3125 - 0,0837 = 0,2288
```

**Paso 4: Calcular P(X > 0,3)**

```
P(X > 0,3) = 1 - P(X ≤ 0,3) = 1 - ∫₀⁰·³ 12x²(1-x)dx
```

```
P(X ≤ 0,3) = [4x³ - 3x⁴]₀⁰·³ = 0,0837 - 0 = 0,0837
```

```
P(X > 0,3) = 1 - 0,0837 = 0,9163
```

**Paso 5: Calcular la probabilidad condicional**

```
P(X < 0,5 | X > 0,3) = 0,2288 / 0,9163 = 0,2497 ≈ 0,25
```

**Respuesta: 0,2497 o aproximadamente 0,25**

---

### **(c)** Sin calcular la esperanza, ¿usted espera que E(X) sea mayor, menor o igual a 0,5? Justifique su respuesta.

**Solución paso a paso:**

**Paso 1: Analizar la forma de la función densidad**

f(x) = 12x²(1-x)

**Paso 2: Encontrar el máximo de f(x)**

Derivamos:
```
f'(x) = 12[2x(1-x) + x²(-1)]
f'(x) = 12[2x - 2x² - x²]
f'(x) = 12[2x - 3x²]
f'(x) = 24x - 36x² = 12x(2 - 3x) = 0
```

Soluciones: x = 0 o 2 - 3x = 0 → x = 2/3

**Paso 3: Verificar que x = 2/3 es un máximo**

```
f''(x) = 24 - 72x
f''(2/3) = 24 - 48 = -24 < 0
```

Por lo tanto, x = 2/3 es un máximo.

**Paso 4: Interpretar el resultado**

El máximo de la densidad está en x = 2/3 ≈ 0,667

Como 2/3 > 0,5, la distribución tiene más "peso" (más probabilidad) hacia la derecha de 0,5.

**Conclusión: E(X) > 0,5**

Dado que el modo está a la derecha de 0,5 y la distribución es unimodal, la media también tenderá a ser mayor que 0,5, ya que la distribución está sesgada hacia valores superiores.

---

### **(d)** E(X)

**Solución paso a paso:**

**Paso 1: Aplicar la definición de esperanza**

```
E(X) = ∫₀¹ x · f(x)dx = ∫₀¹ x · 12x²(1-x)dx
```

**Paso 2: Simplificar el integrando**

```
E(X) = ∫₀¹ 12x³(1-x)dx = ∫₀¹ (12x³ - 12x⁴)dx
```

**Paso 3: Integrar término a término**

```
E(X) = [12 · x⁴/4 - 12 · x⁵/5]₀¹
E(X) = [3x⁴ - 12x⁵/5]₀¹
```

**Paso 4: Evaluar en los límites**

```
E(X) = 3(1)⁴ - (12/5)(1)⁵ - 0
E(X) = 3 - 12/5
E(X) = 3 - 2,4 = 0,6
```

**Respuesta: E(X) = 0,6**

Esto confirma nuestra predicción del apartado (c): E(X) = 0,6 > 0,5 ✓

---

## **Ejercicio 3** (2,5 puntos)

**Enunciado:** En un juego de casino, la probabilidad de que el apostador gane es 0,05, y las jugadas son independientes. Un apostador va diariamente al casino y juega hasta ganar por primera vez. Sea X el número de juegos que participa por noche.

### **(a)** Si en una determinada noche no ganó hasta el 50º juego, ¿cuál es la probabilidad de que no gane hasta el 52º juego?

**Solución paso a paso:**

**Paso 1: Identificar la distribución**

X sigue una distribución geométrica con parámetro p = 0,05:

```
X ~ Geométrica(p = 0,05)
P(X = k) = (1-p)^(k-1) · p
```

**Paso 2: Plantear lo que buscamos**

Queremos: P(X > 52 | X > 50)

Esto significa: dado que no ganó en los primeros 50 juegos, ¿cuál es la probabilidad de no ganar en los primeros 52?

**Paso 3: Usar la propiedad de falta de memoria**

La distribución geométrica tiene la propiedad de "falta de memoria", que significa que la probabilidad de que el evento ocurra en el futuro no depende de lo que haya pasado en el pasado, siempre que no haya ocurrido aún:

```
P(X > n + m | X > n) = P(X > m)
```

Por lo tanto:

```
P(X > 52 | X > 50) = P(X > 52 - 50) = P(X > 2)
```
P(X > n + m | X > n) = P(X > m)
```

Por lo tanto:
```
P(X > 52 | X > 50) = P(X > 52 - 50) = P(X > 2)
```

**Paso 4: Calcular P(X > 2)**

P(X > 2) significa que no gana ni en el juego 1 ni en el juego 2:

```
P(X > 2) = P(no gana en juego 1) × P(no gana en juego 2)
P(X > 2) = (1 - p)²
P(X > 2) = (1 - 0,05)²
P(X > 2) = (0,95)² = 0,9025
```

**Respuesta: 0,9025 o 90,25%**

**Explicación de la falta de memoria:** Como los juegos son independientes, si ya no ganó 50 veces, es como si "empezara de nuevo". Solo importan los próximos 2 juegos adicionales.

---

### **(b)** Sea Y = mínimo(X, 2). Explique el significado de Y en términos del problema en cuestión.

**Solución:**

**Paso 1: Entender la función mínimo(X, 2)**

```
Y = mínimo(X, 2) = { X  si X ≤ 2
                    { 2  si X > 2
```

**Paso 2: Determinar los valores posibles de Y**

- Y = 1 si gana en el primer juego (cuando X = 1)
- Y = 2 en dos casos:
  - Si gana en el segundo juego (cuando X = 2)
  - Si no gana en los primeros 2 juegos (cuando X > 2)

**Paso 3: Calcular las probabilidades**

```
P(Y = 1) = P(X = 1) = p = 0,05
```

```
P(Y = 2) = P(X = 2) + P(X > 2)
P(Y = 2) = (1-p)·p + (1-p)²
P(Y = 2) = 0,95(0,05) + (0,95)²
P(Y = 2) = 0,0475 + 0,9025 = 0,95
```

O más simple:
```
P(Y = 2) = 1 - P(Y = 1) = 1 - 0,05 = 0,95
```

**Significado de Y:**

**Y representa el número de juegos que el apostador juega por noche, truncado a un máximo de 2 juegos.**

Es decir, el apostador adopta la siguiente estrategia:
- Si gana en el primer juego, Y = 1 (jugó 1 vez).
- Si no gana en el primero pero gana en el segundo, Y = 2 (jugó 2 veces).
- Si no gana en los primeros dos juegos, se detiene de todas formas, y Y = 2.

Y es una variable que limita el número de intentos a un máximo de 2 por noche.

---

### **(c)** Obtenga Var(Y), siendo Y la variable aleatoria definida en el ítem anterior.

**Solución paso a paso:**

**Paso 1: Recordar la distribución de Y**

```
Y = 1 con probabilidad 0,05
Y = 2 con probabilidad 0,95
```

**Paso 2: Calcular E(Y)**

```
E(Y) = 1 · P(Y = 1) + 2 · P(Y = 2)
E(Y) = 1(0,05) + 2(0,95)
E(Y) = 0,05 + 1,90
E(Y) = 1,95
```

**Paso 3: Calcular E(Y²)**

```
E(Y²) = 1² · P(Y = 1) + 2² · P(Y = 2)
E(Y²) = 1(0,05) + 4(0,95)
E(Y²) = 0,05 + 3,80
E(Y²) = 3,85
```

**Paso 4: Aplicar la fórmula de la varianza**

```
Var(Y) = E(Y²) - [E(Y)]²
Var(Y) = 3,85 - (1,95)²
Var(Y) = 3,85 - 3,8025
Var(Y) = 0,0475
```

**Respuesta: Var(Y) = 0,0475**

---

## **Ejercicio 4** (2,5 puntos)

**Enunciado:** Sea X una variable aleatoria continua con E(X) = 10 y Var(X) = 4.

### **(a)** Obtenga un límite inferior no trivial para P(8 < X < 12).

**Solución paso a paso:**

**Paso 1: Identificar los parámetros**

```
μ = E(X) = 10
σ² = Var(X) = 4
σ = √4 = 2
```

**Paso 2: Recordar la Desigualdad de Chebyshev**

La desigualdad de Chebyshev establece:

```
P(|X - μ| ≥ k) ≤ σ²/k²
```

O equivalentemente:

```
P(|X - μ| < k) ≥ 1 - σ²/k²
```

**Paso 3: Expresar el intervalo (8, 12) en términos de |X - μ|**

```
P(8 < X < 12) = P(-2 < X - 10 < 2)
              = P(|X - 10| < 2)
```

Aquí identificamos que k = 2

**Paso 4: Aplicar Chebyshev con k = 2**

```
P(|X - 10| < 2) ≥ 1 - σ²/k²
P(|X - 10| < 2) ≥ 1 - 4/4
P(|X - 10| < 2) ≥ 1 - 1
P(|X - 10| < 2) ≥ 0
```

**Observación:** Este límite es trivial porque no proporciona información útil, ya que cualquier probabilidad es mayor o igual a 0. Esto ocurre porque el intervalo corresponde exactamente a una desviación estándar, haciendo que el límite sea 0.

**Explicación de por qué es trivial:** 

El problema está en que el intervalo (8, 12) corresponde exactamente a μ ± σ, es decir, una desviación estándar a cada lado de la media. Con k = σ = 2 y σ² = 4:

```
σ²/k² = 4/4 = 1
```

Esto hace que el límite sea 1 - 1 = 0, que no nos da información.

**Respuesta: P(8 < X < 12) ≥ 0 (límite trivial)**

**Nota:** Para obtener un límite no trivial usando Chebyshev, necesitaríamos un intervalo más amplio. Por ejemplo, con k = 3:

```
P(|X - 10| < 3) ≥ 1 - 4/9 ≈ 0,56
```

Pero el problema pide específicamente el intervalo (8, 12), que resulta en un límite trivial.

---

### **(b)** Si X tiene distribución normal y Φ(.) es la función distribución de la normal estándar, obtenga P(8 < X < 12) en función de Φ(.).

**Solución paso a paso:**

**Paso 1: Identificar la distribución**

```
X ~ N(μ = 10, σ² = 4)
```

Esto significa que X sigue una distribución normal con media 10 y varianza 4, por lo tanto σ = 2.

**Paso 2: Estandarizar la variable**

Para cualquier X ~ N(μ, σ²), la variable estandarizada Z = (X - μ)/σ sigue una distribución normal estándar N(0,1). Esto nos permite usar las tablas de la normal estándar para calcular probabilidades.

En nuestro caso:

```
Z = (X - 10)/2 ~ N(0,1)
```
Z = (X - μ)/σ
```

sigue una distribución normal estándar N(0,1).

En nuestro caso:
```
Z = (X - 10)/2 ~ N(0,1)
```

**Paso 3: Transformar el intervalo**

```
P(8 < X < 12) = P((8-10)/2 < (X-10)/2 < (12-10)/2)
              = P(-2/2 < Z < 2/2)
              = P(-1 < Z < 1)
```

**Paso 4: Expresar en términos de Φ**

Por definición de la función de distribución:

```
P(-1 < Z < 1) = P(Z < 1) - P(Z ≤ -1)
              = Φ(1) - Φ(-1)
```

**Paso 5: Simplificar usando la simetría de la normal**

La distribución normal estándar es simétrica alrededor de cero, por lo que:

```
Φ(-a) = 1 - Φ(a)
```

Por lo tanto:
```
Φ(-1) = 1 - Φ(1)
```

Sustituyendo:
```
P(-1 < Z < 1) = Φ(1) - (1 - Φ(1))
              = Φ(1) - 1 + Φ(1)
              = 2Φ(1) - 1
```

**Respuesta: P(8 < X < 12) = 2Φ(1) - 1**

**Forma alternativa:** P(8 < X < 12) = Φ(1) - Φ(-1)

**Valor numérico aproximado:**

Usando tablas estándar, Φ(1) ≈ 0,8413:

```
P(8 < X < 12) = 2(0,8413) - 1 = 1,6826 - 1 = 0,6826
```

**P(8 < X < 12) ≈ 0,6826 o aproximadamente 68,26%**

Este resultado confirma la regla empírica de que aproximadamente el 68% de los datos en una distribución normal están dentro de una desviación estándar de la media.

---

## Resumen de Respuestas

| Ejercicio | Apartado | Respuesta |
|-----------|----------|-----------|
| 1 | (a) | 0,24 |
| 1 | (b) | 0,84 |
| 2 | (a) | 0 |
| 2 | (b) | 0,2497 |
| 2 | (c) | E(X) > 0,5 |
| 2 | (d) | 0,6 |
| 3 | (a) | 0,9025 |
| 3 | (b) | Variable que limita intentos a máx. 2 por noche |
| 3 | (c) | 0,0475 |
| 4 | (a) | 0 (límite trivial) |
| 4 | (b) | 2Φ(1) - 1 ≈ 0,6826 |

---
