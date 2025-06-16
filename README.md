# 🤖 Simulación de Red Neuronal Artificial – Compuerta Lógica OR

Este proyecto consiste en la construcción, entrenamiento y simulación de una **red neuronal artificial simple** (Perceptrón) para resolver un problema lógico básico: la **compuerta OR**.

## 📘 Objetivo

Comprender los fundamentos del funcionamiento de una red neuronal artificial a través de la implementación paso a paso de un perceptrón, aplicando conceptos clave como:

- Entradas, pesos y bias.
- Función de activación (escalón).
- Regla de aprendizaje (Perceptrón).
- Entrenamiento supervisado de la red.

---

## 🛠 Tecnologías utilizadas

- **Python 3**
- **NumPy** para operaciones matriciales básicas

---

## 🧠 Lógica del Perceptrón

Se simula el comportamiento de un perceptrón para aprender la tabla OR:

| X1 | X2 | Y (esperado) |
|----|----|--------------|
| 0  | 0  | 0            |
| 0  | 1  | 1            |
| 1  | 0  | 1            |
| 1  | 1  | 1            |

El perceptrón usa:
- Pesos iniciales en 0.
- Bias inicial en 0.
- Tasa de aprendizaje: 1.
- Función de activación: Escalón (Step Function).
- Ajustes según la **regla del perceptrón**:
  \[
  \Delta w_i = \alpha (Y_d - Y) X_i \quad,\quad \Delta b = \alpha (Y_d - Y)
  \]

---

## 🚀 Ejecución del código

```bash
python perceptron_or.py
