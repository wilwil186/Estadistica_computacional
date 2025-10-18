# Guía de Estudio: Variables Aleatorias y Distribuciones

## 📋 Temario del Examen

**2. Variables aleatorias:**
- Variables aleatorias y funciones de distribución
- Tipos de variables aleatorias
- Esperanza, varianza, momentos
- Principales distribuciones de probabilidad

---

## 🎯 Conceptos Clave (Versión Concisa)

### 1. Variable Aleatoria (V.A.)

**Definición**: Función que asigna un número real a cada resultado de un experimento aleatorio.

```
X: Ω → ℝ
```

**Tipos**:

#### **Discretas**: 
- Toman valores aislados/contables
- Ejemplos: número de caras, dados, conteos
- Espacio: {x₁, x₂, x₃, ...}

#### **Continuas**: 
- Toman valores en un intervalo
- Ejemplos: tiempo, peso, temperatura
- Espacio: intervalos de ℝ

---

### 2. Funciones de Distribución

#### **PMF (Función de Probabilidad) - Discretas**
```
P(X = xₖ) = pₖ

Propiedades:
• pₖ ≥ 0 para todo k
• Σ pₖ = 1
```

#### **PDF (Función de Densidad) - Continuas**
```
f(x) ≥ 0

Propiedades:
• ∫₋∞^∞ f(x)dx = 1
• P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx
• P(X = x) = 0 (para cualquier x específico)
```

#### **CDF (Función de Distribución Acumulada)**

**Para discretas:**
```
F(x) = P(X ≤ x) = Σ_{xₖ≤x} pₖ
```

**Para continuas:**
```
F(x) = P(X ≤ x) = ∫₋∞ˣ f(t)dt

Relación: f(x) = F'(x)
```

**Propiedades de F(x)**:
- No decreciente
- lim_{x→-∞} F(x) = 0
- lim_{x→∞} F(x) = 1
- Continua por la derecha

---

### 3. Esperanza, Varianza y Momentos

#### **Esperanza (Media) E[X] o μ**

**Interpretación**: Valor promedio esperado a largo plazo

**Discretas:**
```
E[X] = Σ xᵢ · P(X = xᵢ)
```

**Continuas:**
```
E[X] = ∫₋∞^∞ x · f(x)dx
```

**Propiedades**:
- E[c] = c (constante)
- E[aX + b] = aE[X] + b
- E[X + Y] = E[X] + E[Y] (linealidad)

#### **Varianza Var(X) o σ²**

**Interpretación**: Medida de dispersión respecto a la media

**Fórmula:**
```
Var(X) = E[(X - μ)²] = E[X²] - (E[X])²
```

**Discretas:**
```
Var(X) = Σ (xᵢ - μ)² · P(X = xᵢ)
```

**Continuas:**
```
Var(X) = ∫₋∞^∞ (x - μ)² · f(x)dx
```

**Propiedades**:
- Var(c) = 0
- Var(aX + b) = a²Var(X)
- Var(X) ≥ 0

#### **Desviación Estándar σ**
```
σ = √Var(X)
```

#### **Momentos**

**Momento de orden n:**
```
E[Xⁿ] (momento respecto al origen)
```

**Momento central de orden n:**
```
E[(X - μ)ⁿ] (momento respecto a la media)
```

**Notas**:
- 1er momento = E[X] (media)
- 2do momento central = Var(X) (varianza)
- 3er momento central → Asimetría (skewness)
- 4to momento central → Curtosis (kurtosis)

---

### 4. Principales Distribuciones de Probabilidad

#### **DISCRETAS**

| Distribución | Notación | PMF | E[X] | Var(X) |
|-------------|----------|-----|------|--------|
| **Bernoulli** | X ~ Ber(p) | P(X=1)=p, P(X=0)=1-p | p | p(1-p) |
| **Binomial** | X ~ B(n,p) | P(X=k) = C(n,k)p^k(1-p)^(n-k) | np | np(1-p) |
| **Poisson** | X ~ Poi(λ) | P(X=k) = (e^(-λ)λ^k)/k! | λ | λ |
| **Geométrica** | X ~ Geo(p) | P(X=k) = (1-p)^(k-1)·p | 1/p | (1-p)/p² |

#### **CONTINUAS**

| Distribución | Notación | PDF | E[X] | Var(X) |
|-------------|----------|-----|------|--------|
| **Uniforme** | X ~ U(a,b) | f(x) = 1/(b-a) para x∈[a,b] | (a+b)/2 | (b-a)²/12 |
| **Exponencial** | X ~ Exp(λ) | f(x) = λe^(-λx) para x≥0 | 1/λ | 1/λ² |
| **Normal** | X ~ N(μ,σ²) | f(x) = (1/(σ√(2π)))e^(-(x-μ)²/(2σ²)) | μ | σ² |

---

## 📚 Recursos de Estudio Recomendados

### Teoría Completa (Tu favorito ya incluido)

1. **AprendeConAlf - Variables Aleatorias** (EXCELENTE)
   - https://aprendeconalf.es/estadistica-manual/06-variables-aleatorias.html
   - ✅ Teoría clara, ejemplos, gráficos interactivos
   - ✅ Cubre discretas, continuas, esperanza, varianza

2. **Universidad de La Laguna - Variables Aleatorias (PDF Completo)**
   - https://campusvirtual.ull.es/ocw/pluginfile.php/6018/mod_resource/content/1/tema8/ME8.2-valeatorias.pdf
   - ✅ Teoría rigurosa con demostraciones
   - ✅ Cubre todas las distribuciones principales

3. **UC3M - Probabilidad y Variables Aleatorias**
   - https://halweb.uc3m.es/esp/Personal/personas/aarribas/esp/docs/estIG/tema4Print.pdf
   - ✅ Incluye ejemplos con R
   - ✅ TCL y aproximaciones

### Esperanza y Varianza

4. **Universidad Politécnica Valencia - Parámetros**
   - https://personales.upv.es/asala/DocenciaOnline/material/ParamsDistribPr.pdf
   - ✅ Focus en esperanza matemática y varianza
   - ✅ Propiedades y ejemplos

5. **UBA - Variables Aleatorias Discretas**
   - http://www.dm.uba.ar/materias/probabilidades_estadistica_C/2011/1/PyEC04.pdf
   - ✅ Bernoulli, Binomial, Poisson, Geométrica
   - ✅ Demostraciones de E[X] y Var(X)

6. **Universidad Granada - Variable Aleatoria**
   - https://www.ugr.es/~eues/webgrupo/Docencia/MonteroAlonso/estadisticaII/tema2.pdf
   - ✅ Esperanza matemática paso a paso
   - ✅ Ejemplos numéricos

### Ejercicios Resueltos

7. **Universidad de La Laguna - Problemas Resueltos**
   - https://campusvirtual.ull.es/ocw/pluginfile.php/6033/mod_resource/content/1/tema8/PR8.2-valeatorias.pdf
   - ✅ 12+ ejercicios completos
   - ✅ Binomial, Poisson, Normal
   - ✅ Aplicaciones médicas y biológicas

8. **UAM - Esperanza y Momentos (Ejercicios)**
   - http://verso.mat.uam.es/~pablo.fernandez/Tema-PREST-5.pdf
   - ✅ Ejercicios de esperanza, varianza, covarianza
   - ✅ Propiedades de momentos

9. **Asturias Corporación - Esperanza y Varianza**
   - https://www.centro-virtual.com/recursos/biblioteca/pdf/estadistica_i/unidad3_pdf2.pdf
   - ✅ Nota técnica concisa
   - ✅ Ejemplos numéricos

### Distribuciones Específicas

10. **AprendeConAlf - Distribuciones Discretas**
    - https://aprendeconalf.es/estadistica-manual/07-distribuciones-discretas.html
    - ✅ Bernoulli, Binomial, Poisson, Geométrica
    - ✅ Ejemplos interactivos

11. **AprendeConAlf - Distribuciones Continuas**
    - https://aprendeconalf.es/estadistica-manual/08-distribuciones-continuas.html
    - ✅ Uniforme, Exponencial, Normal
    - ✅ Gráficos y aplicaciones

---

## 🔥 Ejercicios Tipo Examen

### Ejercicio 1: Variable Aleatoria Discreta Básica

Se lanza un dado equilibrado. Sea X = "número obtenido"
- a) ¿Es X discreta o continua?
- b) Escribe la PMF de X
- c) Calcula E[X] y Var(X)

<details>
<summary>💡 Ver solución</summary>

a) **Discreta** (toma valores finitos aislados)

b) PMF: P(X = k) = 1/6 para k = 1,2,3,4,5,6

c) 
```
E[X] = Σ k·P(X=k) 
     = 1(1/6) + 2(1/6) + ... + 6(1/6)
     = 21/6 = 3.5

E[X²] = 1²(1/6) + 2²(1/6) + ... + 6²(1/6)
      = 91/6

Var(X) = E[X²] - (E[X])²
       = 91/6 - (3.5)²
       = 91/6 - 12.25
       ≈ 2.92
```
</details>

---

### Ejercicio 2: Distribución Binomial

Una moneda tiene P(cara) = 0.6. Se lanza 10 veces.
- a) ¿Qué distribución sigue X = "número de caras"?
- b) Calcula P(X = 7)
- c) Calcula E[X] y Var(X)

<details>
<summary>💡 Ver solución</summary>

a) **X ~ B(10, 0.6)**

b) 
```
P(X = 7) = C(10,7) · (0.6)⁷ · (0.4)³
         = 120 · 0.0279936 · 0.064
         ≈ 0.215
```

c)
```
E[X] = np = 10(0.6) = 6
Var(X) = np(1-p) = 10(0.6)(0.4) = 2.4
```
</details>

---

### Ejercicio 3: Distribución de Poisson

En un hospital llegan en promedio 4 emergencias por hora.
Sea X = "número de emergencias en 1 hora"
- a) ¿Qué distribución sigue X?
- b) P(X ≤ 2)
- c) E[X] y Var(X)

<details>
<summary>💡 Ver solución</summary>

a) **X ~ Poi(λ = 4)**

b)
```
P(X ≤ 2) = P(X=0) + P(X=1) + P(X=2)
         = e⁻⁴(4⁰/0!) + e⁻⁴(4¹/1!) + e⁻⁴(4²/2!)
         = e⁻⁴(1 + 4 + 8)
         = 13e⁻⁴
         ≈ 0.238
```

c)
```
E[X] = λ = 4
Var(X) = λ = 4
```
</details>

---

### Ejercicio 4: Distribución Uniforme Continua

X ~ U(0, 10)
- a) Escribe f(x) y F(x)
- b) P(3 < X < 7)
- c) E[X] y Var(X)

<details>
<summary>💡 Ver solución</summary>

a)
```
f(x) = 1/10  para x ∈ [0,10]
       0     en otro caso

F(x) = 0        si x < 0
       x/10     si 0 ≤ x ≤ 10
       1        si x > 10
```

b)
```
P(3 < X < 7) = ∫₃⁷ (1/10)dx = [x/10]₃⁷ = 4/10 = 0.4
```

c)
```
E[X] = (a+b)/2 = (0+10)/2 = 5
Var(X) = (b-a)²/12 = 100/12 ≈ 8.33
```
</details>

---

### Ejercicio 5: Distribución Exponencial

El tiempo (en horas) hasta la siguiente llamada es X ~ Exp(λ = 0.5)
- a) P(X > 2)
- b) E[X] (tiempo promedio entre llamadas)
- c) Var(X)

<details>
<summary>💡 Ver solución</summary>

a)
```
P(X > 2) = 1 - F(2) = 1 - (1 - e^(-λ·2))
         = e^(-0.5·2)
         = e^(-1)
         ≈ 0.368
```

b)
```
E[X] = 1/λ = 1/0.5 = 2 horas
```

c)
```
Var(X) = 1/λ² = 1/(0.5)² = 4
```
</details>

---

### Ejercicio 6: Distribución Normal

Estaturas de hombres adultos: X ~ N(170, 100) (en cm, σ² = 100 → σ = 10)
- a) P(X > 180)
- b) P(160 < X < 180)

<details>
<summary>💡 Ver solución</summary>

**Estandarizar:** Z = (X - μ)/σ ~ N(0,1)

a)
```
P(X > 180) = P((X-170)/10 > (180-170)/10)
           = P(Z > 1)
           = 1 - Φ(1)
           ≈ 1 - 0.8413
           = 0.1587
```

b)
```
P(160 < X < 180) = P(-1 < Z < 1)
                  = Φ(1) - Φ(-1)
                  = 0.8413 - 0.1587
                  = 0.6826
```
(Aproximadamente 68% - regla empírica)
</details>

---

## ✅ Checklist de Preparación

- [ ] Entiendo la diferencia entre v.a. discretas y continuas
- [ ] Sé calcular PMF, PDF y CDF
- [ ] Puedo calcular E[X] para discretas y continuas
- [ ] Puedo calcular Var(X) usando ambas fórmulas
- [ ] Conozco las propiedades de E[X] y Var(X)
- [ ] Reconozco cuándo usar cada distribución
- [ ] Sé los parámetros de Bernoulli, Binomial, Poisson
- [ ] Sé los parámetros de Uniforme, Exponencial, Normal
- [ ] Puedo estandarizar una normal
- [ ] Entiendo qué son los momentos

---

## 📝 Fórmulas para Memorizar

### Esperanza y Varianza
```
E[X] discreta: Σ xᵢ·pᵢ
E[X] continua: ∫ x·f(x)dx

Var(X) = E[X²] - (E[X])²

σ = √Var(X)
```

### Distribuciones Clave

**Binomial**: X ~ B(n,p)
- E[X] = np
- Var(X) = np(1-p)

**Poisson**: X ~ Poi(λ)
- E[X] = λ
- Var(X) = λ

**Normal**: X ~ N(μ,σ²)
- E[X] = μ
- Var(X) = σ²
- Estandarización: Z = (X-μ)/σ

**Exponencial**: X ~ Exp(λ)
- E[X] = 1/λ
- Var(X) = 1/λ²

---

## 🎓 Estrategia de Estudio

### Semana 1:
1. Lee recursos #1 y #2 (teoría base)
2. Entiende diferencia discreta/continua
3. Practica calcular E[X] y Var(X) (recurso #4, #6)

### Semana 2:
1. Estudia distribuciones discretas (recursos #5, #10)
2. Estudia distribuciones continuas (recurso #11)
3. Resuelve ejercicios del recurso #7

### Semana 3:
1. Practica ejercicios del recurso #8
2. Resuelve los 6 ejercicios tipo examen de esta guía
3. Repasa momentos (recurso #9)

### Última semana:
1. Repasa fórmulas y parámetros de distribuciones
2. Haz más ejercicios del recurso #7
3. Revisa el checklist

---

## ⚠️ Errores Comunes

1. **Confundir PMF con PDF** → PMF es para discretas, PDF para continuas
2. **P(X = x) en continuas** → Siempre es 0, usa intervalos
3. **Olvidar √ en desviación estándar** → σ = √Var(X), no Var(X)
4. **Confundir E[X²] con (E[X])²** → Son diferentes!
5. **No estandarizar en normal** → Siempre Z = (X-μ)/σ
6. **Confundir parámetros** → λ en Poisson vs p en Binomial

---

## 💡 Tips Finales

**Para recordar distribuciones**:
- **Binomial**: n ensayos, éxito/fracaso → contar éxitos
- **Poisson**: eventos raros en tiempo/espacio → arribosnúmero de
- **Geométrica**: repetir hasta primer éxito → intentos necesarios
- **Uniforme**: "todos igual de probables" → segmento
- **Exponencial**: tiempo entre eventos Poisson → esperas
- **Normal**: campana de Gauss → naturaleza, errores

**Práctica**: Los recursos #7 y #8 tienen decenas de ejercicios resueltos. Dedica al menos 3 horas resolviendo problemas.
