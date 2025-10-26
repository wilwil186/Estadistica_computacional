# Prova do processo seletivo do mestrado e doutorado direto Pippes - 26/10/2025

## Justifique todos os itens de todas as questões

---

## **Ejercicio 1** (2,25 puntos)

**Enunciado:** En un determinado país hay dos etnias. La etnia A representa el 60% de la población y el restante de la población pertenece a la etnia B. El gobierno de este país va a proponer cambios en la ley penal del país. Entre las personas de la etnia A, 70% son favorables al cambio, 20% son contrarios y el restante es neutro. Ya entre los habitantes de la etnia B, 20% son favorables al cambio, 60% son contrarios y el restante es neutro.

### **(a)** Si sorteamos aleatoriamente una persona de ese país, ¿cuál es la probabilidad de que sea de la etnia B y contraria al cambio en la ley penal?

**Solución paso a paso:**

**Paso 1: Identificar las probabilidades dadas**

$$P(A) = 0{,}60 \quad \text{(60% es de etnia A)}$$

$$P(B) = 0{,}40 \quad \text{(40% es de etnia B)}$$

**Paso 2: Probabilidades condicionadas para etnia B**

$$P(\text{Favorable} \mid B) = 0{,}20$$

$$P(\text{Contrario} \mid B) = 0{,}60$$

$$P(\text{Neutro} \mid B) = 0{,}20$$

**Paso 3: Calcular** $P(B \cap \text{Contrario})$

Usamos la regla de la multiplicación:

$$P(B \cap \text{Contrario}) = P(B) \times P(\text{Contrario} \mid B)$$

$$P(B \cap \text{Contrario}) = 0{,}40 \times 0{,}60 = 0{,}24$$

**Respuesta: $P(B \cap \text{Contrario}) = 0{,}24$ o 24%**

---

### **(b)** Si sorteamos aleatoriamente una persona de ese país y observamos que es favorable al cambio en la ley penal, ¿cuál es la probabilidad de que sea de la etnia A?

**Solución paso a paso:**

**Paso 1: Identificar que necesitamos el Teorema de Bayes**

Necesitamos $P(A \mid \text{Favorable})$, usamos:

$$P(A \mid \text{Favorable}) = \frac{P(A \cap \text{Favorable})}{P(\text{Favorable})}$$

**Paso 2: Calcular** $P(A \cap \text{Favorable})$

$$P(A \cap \text{Favorable}) = P(A) \times P(\text{Favorable} \mid A)$$

$$P(A \cap \text{Favorable}) = 0{,}60 \times 0{,}70 = 0{,}42$$

**Paso 3: Calcular** $P(\text{Favorable})$ **usando la ley de probabilidad total**

$$P(\text{Favorable}) = P(A) \times P(\text{Favorable} \mid A) + P(B) \times P(\text{Favorable} \mid B)$$

$$P(\text{Favorable}) = 0{,}60 \times 0{,}70 + 0{,}40 \times 0{,}20$$

$$P(\text{Favorable}) = 0{,}42 + 0{,}08 = 0{,}50$$

**Paso 4: Aplicar Bayes**

$$P(A \mid \text{Favorable}) = \frac{0{,}42}{0{,}50} = 0{,}84$$

**Respuesta: $P(A \mid \text{Favorable}) = 0{,}84$ o 84%**

---

## **Ejercicio 2** (2,75 puntos)

**Enunciado:** Sea $X$ una variable aleatoria continua con soporte en el intervalo $(0,1)$ y función densidad de probabilidad dada por $f(x) = 12x^2(1-x)$. Para esa variable aleatoria, obtenga:

### **(a)** $P(X = 0{,}5)$

**Solución:**

Para cualquier variable aleatoria continua, la probabilidad en un punto específico es cero.

**Explicación:** En variables continuas, solo intervalos tienen probabilidad positiva, los puntos individuales tienen probabilidad cero porque:

$$P(X = c) = \int_{c}^{c} f(x)\,dx = 0$$

**Respuesta: $P(X = 0{,}5) = 0$**

---

### **(b)** $P(X < 0{,}5 \mid X > 0{,}3)$

**Solución paso a paso:**

**Paso 1: Usar la definición de probabilidad condicional**

$$P(X < 0{,}5 \mid X > 0{,}3) = \frac{P(0{,}3 < X < 0{,}5)}{P(X > 0{,}3)}$$

**Paso 2: Calcular** $P(0{,}3 < X < 0{,}5)$

$$P(0{,}3 < X < 0{,}5) = \int_{0.3}^{0.5} 12x^2(1-x)\,dx$$

Expandimos: $12x^2(1-x) = 12x^2 - 12x^3$

$$\int_{0.3}^{0.5} (12x^2 - 12x^3)\,dx = \left[4x^3 - 3x^4\right]_{0.3}^{0.5}$$

**Paso 3: Evaluar en los límites**

En $x = 0{,}5$:

$$4(0{,}5)^3 - 3(0{,}5)^4 = 4(0{,}125) - 3(0{,}0625) = 0{,}5 - 0{,}1875 = 0{,}3125$$

En $x = 0{,}3$:

$$4(0{,}3)^3 - 3(0{,}3)^4 = 4(0{,}027) - 3(0{,}0081) = 0{,}108 - 0{,}0243 = 0{,}0837$$

$$P(0{,}3 < X < 0{,}5) = 0{,}3125 - 0{,}0837 = 0{,}2288$$

**Paso 4: Calcular** $P(X > 0{,}3)$

$$P(X > 0{,}3) = 1 - P(X \leq 0{,}3) = 1 - \int_{0}^{0.3} 12x^2(1-x)\,dx$$

$$P(X \leq 0{,}3) = \left[4x^3 - 3x^4\right]_{0}^{0.3} = 0{,}0837 - 0 = 0{,}0837$$

$$P(X > 0{,}3) = 1 - 0{,}0837 = 0{,}9163$$

**Paso 5: Calcular la probabilidad condicional**

$$P(X < 0{,}5 \mid X > 0{,}3) = \frac{0{,}2288}{0{,}9163} = 0{,}2497 \approx 0{,}25$$

**Respuesta: $P(X < 0{,}5 \mid X > 0{,}3) = 0{,}2497$ o aproximadamente $0{,}25$**

---

### **(c)** Sin calcular la esperanza, ¿usted espera que $E(X)$ sea mayor, menor o igual a 0,5? Justifique su respuesta.

**Solución paso a paso:**

**Paso 1: Analizar la forma de la función densidad**

$$f(x) = 12x^2(1-x)$$

**Paso 2: Encontrar el máximo de** $f(x)$

Derivamos:

$$f'(x) = 12[2x(1-x) + x^2(-1)]$$

$$f'(x) = 12[2x - 2x^2 - x^2]$$

$$f'(x) = 12[2x - 3x^2]$$

$$f'(x) = 24x - 36x^2 = 12x(2 - 3x) = 0$$

Soluciones: $x = 0$ o $2 - 3x = 0 \Rightarrow x = \frac{2}{3}$

**Paso 3: Verificar que** $x = \frac{2}{3}$ **es un máximo**

$$f''(x) = 24 - 72x$$

$$f''\left(\frac{2}{3}\right) = 24 - 48 = -24 < 0$$

Por lo tanto, $x = \frac{2}{3}$ es un máximo.

**Paso 4: Interpretar el resultado**

El máximo de la densidad está en $x = \frac{2}{3} \approx 0{,}667$

Como $\frac{2}{3} > 0{,}5$, la distribución tiene más "peso" (más probabilidad) hacia la derecha de $0{,}5$.

**Conclusión: $E(X) > 0{,}5$**

La distribución está sesgada hacia valores mayores que $0{,}5$, por lo que la media estará a la derecha de $0{,}5$.

---

### **(d)** $E(X)$

**Solución paso a paso:**

**Paso 1: Aplicar la definición de esperanza**

$$E(X) = \int_{0}^{1} x \cdot f(x)\,dx = \int_{0}^{1} x \cdot 12x^2(1-x)\,dx$$

**Paso 2: Simplificar el integrando**

$$E(X) = \int_{0}^{1} 12x^3(1-x)\,dx = \int_{0}^{1} (12x^3 - 12x^4)\,dx$$

**Paso 3: Integrar término a término**

$$E(X) = \left[12 \cdot \frac{x^4}{4} - 12 \cdot \frac{x^5}{5}\right]_{0}^{1}$$

$$E(X) = \left[3x^4 - \frac{12x^5}{5}\right]_{0}^{1}$$

**Paso 4: Evaluar en los límites**

$$E(X) = 3(1)^4 - \frac{12}{5}(1)^5 - 0$$

$$E(X) = 3 - \frac{12}{5} = 3 - 2{,}4 = 0{,}6$$

**Respuesta: $E(X) = 0{,}6$ o $E(X) = \frac{3}{5}$**

Esto confirma nuestra predicción del apartado (c): $E(X) = 0{,}6 > 0{,}5$ ✓

---

## **Ejercicio 3** (2,5 puntos)

**Enunciado:** En un determinado juego de casino, la probabilidad de que el apostador gane es $0{,}05$ y hay independencia entre realizaciones sucesivas del juego. Un determinado apostador se dirige diariamente a este casino y apuesta en ese juego hasta que gane por primera vez. Sea $X$ el número de juegos en que participa por noche.

### **(a)** Si en una determinada noche no ganó hasta el 50º juego, ¿cuál es la probabilidad de que no gane hasta el 52º juego?

**Solución paso a paso:**

**Paso 1: Identificar la distribución**

$X$ sigue una distribución geométrica con parámetro $p = 0{,}05$:

$$X \sim \text{Geométrica}(p = 0{,}05)$$

$$P(X = k) = (1-p)^{k-1} \cdot p$$

**Paso 2: Plantear lo que buscamos**

Queremos: $P(X > 52 \mid X > 50)$

Esto significa: dado que no ganó en los primeros 50 juegos, ¿cuál es la probabilidad de no ganar en los primeros 52?

**Paso 3: Usar la propiedad de falta de memoria**

La distribución geométrica tiene la propiedad de "falta de memoria":

$$P(X > n + m \mid X > n) = P(X > m)$$

Por lo tanto:

$$P(X > 52 \mid X > 50) = P(X > 52 - 50) = P(X > 2)$$

**Paso 4: Calcular** $P(X > 2)$

$P(X > 2)$ significa que no gana ni en el juego 1 ni en el juego 2:

$$P(X > 2) = P(\text{no gana en juego 1}) \times P(\text{no gana en juego 2})$$

$$P(X > 2) = (1 - p)^2$$

$$P(X > 2) = (1 - 0{,}05)^2$$

$$P(X > 2) = (0{,}95)^2 = 0{,}9025$$

**Respuesta: $P(X > 52 \mid X > 50) = 0{,}9025$ o $90{,}25\%$**

**Explicación de la falta de memoria:** Como los juegos son independientes, si ya no ganó 50 veces, es como si "empezara de nuevo". Solo importan los próximos 2 juegos adicionales.

---

### **(b)** Sea $Y = \min(X, 2)$. Explique el significado de $Y$ en términos del problema en cuestión.

**Solución:**

**Paso 1: Entender la función** $\min(X, 2)$

$$Y = \min(X, 2) = \begin{cases} 
X & \text{si } X \leq 2 \\
2 & \text{si } X > 2
\end{cases}$$

**Paso 2: Determinar los valores posibles de** $Y$

- $Y = 1$ si gana en el primer juego (cuando $X = 1$)
- $Y = 2$ en dos casos:
  - Si gana en el segundo juego (cuando $X = 2$)
  - Si no gana en los primeros 2 juegos (cuando $X > 2$)

**Paso 3: Calcular las probabilidades**

$$P(Y = 1) = P(X = 1) = p = 0{,}05$$

$$P(Y = 2) = P(X = 2) + P(X > 2)$$

$$P(Y = 2) = (1-p) \cdot p + (1-p)^2$$

$$P(Y = 2) = 0{,}95(0{,}05) + (0{,}95)^2$$

$$P(Y = 2) = 0{,}0475 + 0{,}9025 = 0{,}95$$

O más simple:

$$P(Y = 2) = 1 - P(Y = 1) = 1 - 0{,}05 = 0{,}95$$

**Significado de** $Y$**:**

**$Y$ representa el número de juegos que el apostador juega por noche, limitado a un máximo de 2 juegos.**

Es decir, el apostador adopta la siguiente estrategia:
- Si gana en el primer juego, $Y = 1$ (jugó 1 vez)
- Si no gana en el primer juego pero gana en el segundo, $Y = 2$ (jugó 2 veces)
- Si no gana en ninguno de los dos primeros juegos, se detiene de todas formas, y $Y = 2$

Es una variable que "trunca" o "limita" el número de intentos a máximo 2 por noche.

---

### **(c)** Obtenga $\text{Var}(Y)$, siendo $Y$ la variable aleatoria definida en el ítem anterior.

**Solución paso a paso:**

**Paso 1: Recordar la distribución de** $Y$

$$\begin{align}
Y = 1 &\quad \text{con probabilidad } 0{,}05 \\
Y = 2 &\quad \text{con probabilidad } 0{,}95
\end{align}$$

**Paso 2: Calcular** $E(Y)$

$$E(Y) = 1 \cdot P(Y = 1) + 2 \cdot P(Y = 2)$$

$$E(Y) = 1(0{,}05) + 2(0{,}95)$$

$$E(Y) = 0{,}05 + 1{,}90 = 1{,}95$$

**Paso 3: Calcular** $E(Y^2)$

$$E(Y^2) = 1^2 \cdot P(Y = 1) + 2^2 \cdot P(Y = 2)$$

$$E(Y^2) = 1(0{,}05) + 4(0{,}95)$$

$$E(Y^2) = 0{,}05 + 3{,}80 = 3{,}85$$

**Paso 4: Aplicar la fórmula de la varianza**

$$\text{Var}(Y) = E(Y^2) - [E(Y)]^2$$

$$\text{Var}(Y) = 3{,}85 - (1{,}95)^2$$

$$\text{Var}(Y) = 3{,}85 - 3{,}8025$$

$$\text{Var}(Y) = 0{,}0475$$

**Respuesta: $\text{Var}(Y) = 0{,}0475$**

---

## **Ejercicio 4** (2,5 puntos)

**Enunciado:** Sea $X$ una variable aleatoria continua, en que $E(X) = 10$ y $\text{Var}(X) = 4$.

### **(a)** Obtenga un límite inferior no trivial para $P(8 < X < 12)$.

**Solución paso a paso:**

**Paso 1: Identificar los parámetros**

$$\mu = E(X) = 10$$

$$\sigma^2 = \text{Var}(X) = 4$$

$$\sigma = \sqrt{4} = 2$$

**Paso 2: Recordar la Desigualdad de Chebyshev**

La desigualdad de Chebyshev establece:

$$P(|X - \mu| \geq k) \leq \frac{\sigma^2}{k^2}$$

O equivalentemente:

$$P(|X - \mu| < k) \geq 1 - \frac{\sigma^2}{k^2}$$

**Paso 3: Expresar el intervalo** $(8, 12)$ **en términos de** $|X - \mu|$

$$P(8 < X < 12) = P(-2 < X - 10 < 2) = P(|X - 10| < 2)$$

Aquí identificamos que $k = 2$

**Paso 4: Aplicar Chebyshev con** $k = 2$

$$P(|X - 10| < 2) \geq 1 - \frac{\sigma^2}{k^2}$$

$$P(|X - 10| < 2) \geq 1 - \frac{4}{4}$$

$$P(|X - 10| < 2) \geq 1 - 1$$

$$P(|X - 10| < 2) \geq 0$$

**Observación:** Este límite es trivial porque no nos proporciona información útil (cualquier probabilidad es $\geq 0$).

**Explicación de por qué es trivial:** 

El problema está en que el intervalo $(8, 12)$ corresponde exactamente a $\mu \pm \sigma$, es decir, una desviación estándar a cada lado de la media. Con $k = \sigma = 2$ y $\sigma^2 = 4$:

$$\frac{\sigma^2}{k^2} = \frac{4}{4} = 1$$

Esto hace que el límite sea $1 - 1 = 0$, que no nos da información.

**Respuesta: $P(8 < X < 12) \geq 0$ (límite trivial)**

**Nota:** Para obtener un límite no trivial usando Chebyshev, necesitaríamos un intervalo más amplio. Por ejemplo, con $k = 3$:

$$P(|X - 10| < 3) \geq 1 - \frac{4}{9} \approx 0{,}56$$

Pero el problema pide específicamente el intervalo $(8, 12)$, que resulta en un límite trivial.

---

### **(b)** Si $X$ tiene distribución normal y $\Phi(.)$ es la función distribución de la normal estándar, obtenga $P(8 < X < 12)$ en función de $\Phi(.)$.

**Solución paso a paso:**

**Paso 1: Identificar la distribución**

$$X \sim N(\mu = 10, \sigma^2 = 4)$$

Esto significa que $X$ sigue una distribución normal con media 10 y varianza 4, por lo tanto $\sigma = 2$.

**Paso 2: Estandarizar la variable**

Para cualquier $X \sim N(\mu, \sigma^2)$, la variable estandarizada:

$$Z = \frac{X - \mu}{\sigma}$$

sigue una distribución normal estándar $N(0,1)$.

En nuestro caso:

$$Z = \frac{X - 10}{2} \sim N(0,1)$$

**Paso 3: Transformar el intervalo**

$$P(8 < X < 12) = P\left(\frac{8-10}{2} < \frac{X-10}{2} < \frac{12-10}{2}\right)$$

$$= P\left(\frac{-2}{2} < Z < \frac{2}{2}\right)$$

$$= P(-1 < Z < 1)$$

**Paso 4: Expresar en términos de** $\Phi$

Por definición de la función de distribución:

$$P(-1 < Z < 1) = P(Z < 1) - P(Z \leq -1)$$

$$= \Phi(1) - \Phi(-1)$$

**Paso 5: Simplificar usando la simetría de la normal**

La distribución normal estándar es simétrica alrededor de cero, por lo que:

$$\Phi(-a) = 1 - \Phi(a)$$

Por lo tanto:

$$\Phi(-1) = 1 - \Phi(1)$$

Sustituyendo:

$$P(-1 < Z < 1) = \Phi(1) - (1 - \Phi(1))$$

$$= \Phi(1) - 1 + \Phi(1)$$

$$= 2\Phi(1) - 1$$

**Respuesta: $P(8 < X < 12) = 2\Phi(1) - 1$**

**Forma alternativa:** $P(8 < X < 12) = \Phi(1) - \Phi(-1)$

**Valor numérico aproximado:**

Usando tablas estándar, $\Phi(1) \approx 0{,}8413$:

$$P(8 < X < 12) = 2(0{,}8413) - 1 = 1{,}6826 - 1 = 0{,}6826$$

**$P(8 < X < 12) \approx 0{,}6826$ o aproximadamente $68{,}26\%$**

Este resultado confirma la regla empírica de que aproximadamente el 68% de los datos en una distribución normal están dentro de una desviación estándar de la media.

---

## Resumen de Respuestas

| Ejercicio | Apartado | Respuesta |
|-----------|----------|-----------|
| 1 | (a) | $0{,}24$ |
| 1 | (b) | $0{,}84$ |
| 2 | (a) | $0$ |
| 2 | (b) | $0{,}2497$ |
| 2 | (c) | $E(X) > 0{,}5$ |
| 2 | (d) | $0{,}6$ o $\frac{3}{5}$ |
| 3 | (a) | $0{,}9025$ |
| 3 | (b) | Variable que limita intentos a máx. 2 por noche |
| 3 | (c) | $0{,}0475$ |
| 4 | (a) | $0$ (límite trivial con Chebyshev) |
| 4 | (b) | $2\Phi(1) - 1 \approx 0{,}6826$ |

---

## Fórmulas Clave Utilizadas

### Teorema de Bayes
$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

### Ley de Probabilidad Total
$$P(B) = \sum_{i} P(B \mid A_i) \cdot P(A_i)$$

### Esperanza de Variable Continua
$$E(X) = \int_{-\infty}^{\infty} x \cdot f(x)\,dx$$

### Varianza
$$\text{Var}(X) = E(X^2) - [E(X)]^2$$

### Desigualdad de Chebyshev
$$P(|X - \mu| < k) \geq 1 - \frac{\sigma^2}{k^2}$$

### Estandarización Normal
$$Z = \frac{X - \mu}{\sigma} \sim N(0,1)$$

### Propiedad de Falta de Memoria (Geométrica)
$$P(X > n + m \mid X > n) = P(X > m)$$

---