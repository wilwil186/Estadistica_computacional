# Guía de Estudio: Experimento Aleatorio, Probabilidad, Probabilidad Condicional e Independencia

## 📋 Temario del Examen (Según Edital)

**Definiciones básicas:**
1. Experimento aleatorio
2. Probabilidad
3. Probabilidad condicional
4. Independencia

---

## 🎯 Conceptos Clave (Versión Concisa)

### 1. Experimento Aleatorio

**Definición**: Proceso que puede repetirse bajo las mismas condiciones pero cuyo resultado no se puede predecir con certeza.

**Características**:
- Reproducible
- Resultados conocidos de antemano
- Resultado específico impredecible
- Depende del azar

**Ejemplos**:
- Lanzar un dado: Ω = {1, 2, 3, 4, 5, 6}
- Lanzar una moneda: Ω = {Cara, Cruz}
- Extraer una carta: Ω = {52 cartas}
- Tiempo de espera: Ω = [0, ∞)

---

### 2. Probabilidad

**Axiomas de Kolmogorov** (los más importantes):

1. **P(A) ≥ 0** para todo evento A
2. **P(Ω) = 1** (certeza)
3. **P(A ∪ B) = P(A) + P(B)** si A ∩ B = ∅

**Fórmula Clásica** (Laplace):
```
P(A) = Casos favorables / Casos posibles
```

**Propiedades Derivadas**:
- P(A') = 1 - P(A)
- P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- 0 ≤ P(A) ≤ 1

---

### 3. Probabilidad Condicional

**Fórmula Principal**:
```
P(A|B) = P(A ∩ B) / P(B),  con P(B) > 0
```

**Regla de Multiplicación**:
```
P(A ∩ B) = P(A|B) · P(B) = P(B|A) · P(A)
```

**Teorema de la Probabilidad Total**:
```
P(B) = Σ P(B|Aᵢ) · P(Aᵢ)
```

**Teorema de Bayes**:
```
P(Aᵢ|B) = [P(B|Aᵢ) · P(Aᵢ)] / [Σ P(B|Aⱼ) · P(Aⱼ)]
```

---

### 4. Independencia

**Definición**: Dos eventos A y B son independientes si:
```
P(A ∩ B) = P(A) · P(B)
```

**Criterios Equivalentes** (basta uno):
1. P(A ∩ B) = P(A) · P(B)
2. P(A|B) = P(A)
3. P(B|A) = P(B)

**⚠️ IMPORTANTE**: 
- Independencia ≠ Incompatibilidad
- Si A y B son mutuamente excluyentes (A ∩ B = ∅) y P(A) > 0, P(B) > 0 → Son DEPENDIENTES

---

## 📚 Recursos de Estudio (Enlaces Directos)

### Teoría Completa

1. **Manual de Estadística - Probabilidad** (Universidad)
   - https://aprendeconalf.es/estadistica-manual/05-probabilidad.html
   - ✅ Cubre: Axiomas, probabilidad condicional, Bayes, independencia
   - Incluye ejemplos y demostraciones

2. **LibreTexts - Espacios de Muestra y Eventos** (En español)
   - https://espanol.libretexts.org/Estadisticas/Estadisticas_Introductorias/Libro:_Estad%C3%ADsticas_Introductorias_(Shafer_y_Zhang)/03:_Conceptos_b%C3%A1sicos_de_probabilidad/3.01:_Espacios_de_muestra,_eventos_y_sus_probabilidades
   - ✅ Conceptos básicos bien explicados

3. **Probabilidad Condicional y Bayes** (Universidad Carlos III)
   - https://halweb.uc3m.es/esp/personal/personas/mwiper/docencia/Spanish/Teoria_Est_El/tema4_orig.pdf
   - ✅ PDF completo con ejemplos paso a paso

### Ejercicios Resueltos

4. **Universidad de Zaragoza - Ejercicios Resueltos Completos**
   - https://ocw.unizar.es/ocw/ciencias-experimentales/conocimientos-basicos-de-matematicas-para-primeros-cursos-universitarios/b5_estadistica/b5_tema1/resueltos_B5_t1.pdf
   - ✅ Ejercicios básicos a avanzados con soluciones detalladas

5. **Universidad de La Laguna - Problemas Resueltos (Bayes)**
   - https://campusvirtual.ull.es/ocw/pluginfile.php/6032/mod_resource/content/1/tema8/PR8.1-probabilidad.pdf
   - ✅ Enfoque especial en Teorema de Bayes

6. **Alcaste - Cálculo de Probabilidades (100+ Ejercicios)**
   - https://alcaste.com/departamentos/matematicas/bachillerato/PrimeromateI/14_Calculo_probabilidad/Ejercicios_resueltos.pdf
   - ✅ Gran variedad de problemas

7. **UC3M - Ejercicios Tema 3**
   - https://halweb.uc3m.es/esp/Personal/personas/amalonso/esp/Tema3soluciones.pdf
   - ✅ Distribuciones y probabilidad

8. **Probabilidad Condicional - Ejercicios Específicos**
   - https://www.matematicasonline.es/BachilleratoCCNN/Primero/ejercicios/Ejercicios%20y%20problemas%20de%20probabilidad%20condicionada.pdf
   - ✅ Focus en probabilidad condicional

### Videos Recomendados

9. **Khan Academy - Probabilidad y Estadística**
   - https://es.khanacademy.org/math/statistics-probability
   - ✅ Videos cortos y ejercicios interactivos

---

## 🔥 Ejercicios Tipo Examen (Para Practicar)

### Ejercicio 1: Experimento Aleatorio Básico
Se lanza un dado equilibrado. Sea A = {número par} y B = {número ≥ 4}.
- a) Calcula P(A), P(B), P(A ∩ B)
- b) ¿Son A y B independientes?

<details>
<summary>💡 Ver solución</summary>

a) 
- A = {2,4,6} → P(A) = 3/6 = 1/2
- B = {4,5,6} → P(B) = 3/6 = 1/2  
- A ∩ B = {4,6} → P(A ∩ B) = 2/6 = 1/3

b) P(A)·P(B) = (1/2)(1/2) = 1/4 ≠ 1/3 = P(A ∩ B)
**NO son independientes**
</details>

---

### Ejercicio 2: Probabilidad Condicional
En una urna hay 3 bolas rojas y 2 azules. Se extraen dos bolas SIN reposición.
- a) P(ambas rojas)
- b) P(segunda roja | primera roja)

<details>
<summary>💡 Ver solución</summary>

a) P(R₁ ∩ R₂) = P(R₁) · P(R₂|R₁) = (3/5) · (2/4) = 6/20 = **3/10**

b) P(R₂|R₁) = **2/4 = 1/2**
</details>

---

### Ejercicio 3: Teorema de Bayes (Problema Clásico)
Una enfermedad afecta al 1% de la población. Una prueba tiene:
- Sensibilidad (detecta enfermo): 95%
- Especificidad (detecta sano): 90%

Si una persona da positivo, ¿probabilidad de estar realmente enferma?

<details>
<summary>💡 Ver solución</summary>

Sea E = enfermo, P = prueba positiva

**Datos:**
- P(E) = 0.01, P(E') = 0.99
- P(P|E) = 0.95
- P(P|E') = 1 - 0.90 = 0.10

**Por probabilidad total:**
P(P) = P(P|E)·P(E) + P(P|E')·P(E')
     = 0.95(0.01) + 0.10(0.99)
     = 0.0095 + 0.099 = 0.1085

**Por Bayes:**
P(E|P) = [P(P|E)·P(E)] / P(P)
       = 0.0095 / 0.1085
       = **0.0876 ≈ 8.76%**

⚠️ **Interpretación importante**: Solo 8.76% de positivos están realmente enfermos debido a la baja prevalencia.
</details>

---

### Ejercicio 4: Independencia vs Incompatibilidad
Sean A y B eventos con P(A) = 0.4, P(B) = 0.3, P