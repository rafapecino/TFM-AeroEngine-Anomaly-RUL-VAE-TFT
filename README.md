# Anomaly Detection and RUL Prediction in Aero-Engine Turbines using Deep Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Target: Q1 Journal](https://img.shields.io/badge/Research-Q1%20Target-red.svg)](#)

Este repositorio contiene el código fuente y la metodología del Trabajo Fin de Máster (TFM) enfocado en el mantenimiento predictivo (PdM) de motores turbofán. La investigación integra arquitecturas de vanguardia para abordar la naturaleza estocástica de la degradación mecánica.

## 🔬 Resumen de la Investigación
El objetivo es desarrollar un framework robusto que combine la detección de anomalías no supervisada mediante **Variational Autoencoders (VAE)** con la predicción precisa de la Vida Útil Remanente (RUL) usando **Temporal Fusion Transformers (TFT)**. 

### Características principales:
- **Dataset:** Benchmarking exhaustivo con NASA C-MAPSS (Subsets FD001-FD004).
- **Hybrid Architecture:** Extracción de características espacio-temporales mediante 1D-CNN + LSTM.
- **Uncertainty Quantification:** Implementación de Monte Carlo Dropout para intervalos de confianza en tiempo real.
- **XAI (Explainable AI):** Interpretabilidad local y global mediante valores SHAP y mecanismos de atención.

## 🛠 Estructura del Proyecto
```text
├── data/               # Scripts de descarga y preprocesamiento de C-MAPSS
├── models/             # Definiciones de arquitecturas (VAE, TFT, CNN-LSTM)
├── notebooks/          # Experimentos iniciales y visualización
├── src/                # Scripts de entrenamiento, validación y evaluación
│   ├── preprocessing.py
│   ├── trainer.py
│   └── metrics.py      # Implementación de la NASA Scoring Function
├── tests/              # Tests unitarios para las capas de la red
├── results/            # Pesos de modelos y logs de Ablation Studies
└── README.md
