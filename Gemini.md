# 🔬 TFM — Detección de Anomalías en Motores de Turbina Aeronáutica

**Dataset:** NASA C-MAPSS (FD001, FD002, FD003, FD004)
**Objetivo:** Modelo híbrido VAE + CNN-LSTM con cuantificación de incertidumbre (MC Dropout) e interpretabilidad (SHAP)

---

## 📝 Notas Rápidas

**En el código interno:** Es mejor mantener los nombres `s1`, `s2`... para que el código sea corto y compatible con las funciones de otros datasets (como el FD002 o FD004) donde a veces los sensores se filtran de forma distinta.

**Para la Documentación y Gráficos:** ¡Es obligatorio! No pongas un gráfico que diga "Sensor 11", pon un gráfico que diga "Presión Estática HPC (s11)".

### Significado de los Sensores

| Sensor | Símbolo | Descripción Física | Unidades | Estado (FD001/FD003) |
|:---:|:---:|:---|:---:|:---|
| **s1** | T2 | Temperatura total en la entrada del Fan | °R | ❌ Constante (Eliminado) |
| **s2** | T24 | Temperatura total a la salida del LPC | °R | ✅ Variable |
| **s3** | T30 | Temperatura total a la salida del HPC | °R | ✅ Variable |
| **s4** | T50 | Temperatura total a la salida de la LPT | °R | ✅ Variable |
| **s5** | P2 | Presión total en la entrada del Fan | psia | ❌ Constante (Eliminado) |
| **s6** | P15 | Presión total en el bypass-duct | psia | ❌ Constante (Eliminado) |
| **s7** | P30 | Presión total a la salida del HPC | psia | ✅ Variable |
| **s8** | Nf | Velocidad física del Fan | rpm | ✅ Variable |
| **s9** | Nc | Velocidad física del núcleo | rpm | ✅ Variable |
| **s10** | epr | Relación de presión del motor (P50/P2) | -- | ❌ Constante (Eliminado) |
| **s11** | Ps30 | Presión estática a la salida del HPC | psia | ✅ Variable |
| **s12** | phi | Relación flujo de combustible a Ps30 | pps/psi | ✅ Variable |
| **s13** | NRf | Velocidad corregida del Fan | rpm | ✅ Variable |
| **s14** | NRc | Velocidad corregida del núcleo | rpm | ✅ Variable |
| **s15** | BPR | Relación de derivación (Bypass Ratio) | -- | ✅ Variable |
| **s16** | farB | Relación aire-combustible | -- | ❌ Constante (Eliminado) |
| **s17** | htBleed | Entalpía de purga | -- | ✅ Variable |
| **s18** | Nf_dmd | Velocidad del Fan demandada | rpm | ❌ Constante (Eliminado) |
| **s19** | PCNfR_dmd | Velocidad corregida del Fan demandada | rpm | ❌ Constante (Eliminado) |
| **s20** | W31 | Purga de refrigerante de la HPT | lbm/s | ✅ Variable |
| **s21** | W32 | Purga de refrigerante de la LPT | lbm/s | ✅ Variable |

---

## 🏗️ Arquitectura del Sistema

Flujo del sistema: [Sensores IoT] → [Preprocesamiento] → [VAE] → [CNN-LSTM] → [RUL + Incertidumbre] → [SHAP]

1. Preprocesamiento: Limpieza, normalización adaptativa, generación RUL piecewise.
2. VAE — Detección de Anomalías: Entrenado en motores sanos; error de reconstrucción equivalente al Health Index.
3. CNN-LSTM — Predicción RUL: Ventanas 3D de 30 ciclos para predicción probabilística.
4. MC Dropout: Generación de intervalos de confianza en la predicción.
5. SHAP: Explicación por sensor para diagnóstico físico.

---

## 📋 Plan de Hitos

### FASE 1 — Data Engineering
* **Hito 1.1.1:** Carga y consolidación de FD001–FD004 (Train, Test, RUL) -- ✅ Completado
* **Hito 1.1.2:** Etiquetado Remaining Useful Life (RUL) con clip=125 -- ✅ Completado
* **Hito 1.1.3:** Pruning: Filtrado de sensores y settings de varianza cero -- ✅ Completado
* **Hito 1.2:** Normalización adaptativa (Min-Max en rango [0,1] ajustado sobre train) -- ✅ Completado
* **Hito 1.3:** Generador de ventanas deslizantes (tensores 3D [N, window=30, features]) -- ✅ Completado
* **Hito 1.4:** Análisis de correlación de Spearman sensores vs RUL -- ✅ Completado

### FASE 2 — Detección de Anomalías (VAE)
* **Hito 2.1:** Arquitectura VAE (Encoder-Decoder + capa latente) -- ✅ Completado
* **Hito 2.2:** Entrenamiento VAE solo con ciclos sanos -- ✅ Completado
* **Hito 2.3:** Umbral crítico de anomalía (percentil 95 del error de reconstrucción) -- ✅ Completado
* **Hito 2.4:** Optimización de umbral y reporte de False Alarm Rate (FAR) -- ✅ Completado
* **Hito 2.5:** Localización de Fallos por Sensor (Huella de la Anomalía) -- ✅ Completado

### FASE 3 — Predicción de RUL (CNN-LSTM)
* **Hito 3.1:** Arquitectura híbrida 1D-CNN + LSTM (o Transformer) -- ⏳ Pendiente
* **Hito 3.2:** Función de pérdida personalizada (NASA Score + RMSE) -- ⏳ Pendiente
* **Hito 3.3:** Entrenamiento y ajuste de hiperparámetros -- ⏳ Pendiente

### FASE 4 — Validación Científica Q1
* **Hito 4.1:** Monte Carlo Dropout, intervalos de confianza -- ⏳ Pendiente
* **Hito 4.2:** Ablation Studies (con/sin CNN, con/sin VAE) -- ⏳ Pendiente
* **Hito 4.3:** Comparación vs baselines literatura (Saxena 2008, Heimes 2008) -- ⏳ Pendiente

### FASE 5 — Interpretabilidad y Cierre (XAI)
* **Hito 5.1:** KernelExplainer de SHAP, importancia de sensores -- ⏳ Pendiente
* **Hito 5.2:** Correlación hallazgos IA ↔ termodinámica del motor -- ⏳ Pendiente
* **Hito 5.3:** Tablas y gráficos de alta resolución para manuscrito -- ⏳ Pendiente

---

## 🗂️ Estructura del Proyecto

* Experimentos/
  * Main.ipynb: Notebook principal (todos los hitos)
  * README.md: Este archivo (tracker de progreso)
  * CMAPSSData/: Datos NASA C-MAPSS (train/test/RUL x4)
  * .venv/: Entorno Python 3.14

---

## 📌 Estado Actual

* ESTADO DEL PROYECTO: Fase 3 — Predicción de RUL (CNN-LSTM) iniciada
* PRÓXIMO PASO: Fase 3 — Implementación de arquitectura híbrida CNN-LSTM

### 📝 Log de Cambios

* 2026-03-05 (Hitos 1.1.1, 1.1.2, 1.1.3): Carga multi-dataset, RUL piecewise, y filtrado modularizado de features sin varianza.
* 2026-03-05 (Hito 1.2): Normalización Min-Max sobre conjunto de entrenamiento.
* 2026-03-05 (Hito 1.3): Generador de ventanas deslizantes make_windows_train / make_windows_test, tensores 3D funcionales comprobados visualmente con heatmap normalizado.
* 2026-03-12 (Hito 1.4): Análisis correlación Spearman de sensores vs RUL.
* 2026-03-12 (Hitos 2.1, 2.2, 2.3): Arquitectura VAE implementada, entrenada con datos sanos y validada definiendo el umbral de anomalía al percentil 95. Matriz de confusión generada.* 2026-03-15 (Hitos 2.4, 2.5): Optimización de umbral mediante Curva Precision-Recall (Óptimo F1), reporte de False Alarm Rate (FAR) y despliegue de Localización de Fallos por Sensor (Huella de la Anomalía: Ps30, T50, Setting 2). Fase 2 completada al 100%.
* 2026-03-16 (Hito 2.6): Implementación de Lógica de Persistencia (3 de 5) para reducción de FAR. Reducción del FAR del 6.45% al 4.31% y mejora de precisión al 78.59%.
* 2026-03-16 (Hito 2.7): Validación Estadística (N=5) completada. FAR medio del 1.78% (±0.24%) y F1-Score del 0.7698 (±0.0038). Fase 2 finalizada con rigor científico.
