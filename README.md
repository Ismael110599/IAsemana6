# Red Neuronal Simple - Compuerta OR

Un archivo Python que simula cómo funciona una neurona artificial básica (perceptrón) aprendiendo a resolver la función lógica OR.

## ¿De qué se trata?

Este script es una introducción práctica al mundo de las redes neuronales. Implementa desde cero un perceptrón simple que aprende por sí mismo a comportarse como una compuerta OR, mostrando de manera clara y visual:

- Cómo una neurona artificial procesa la información  
- El fascinante proceso de aprendizaje automático paso a paso  
- Cómo se van ajustando los pesos y el sesgo (bias) durante el entrenamiento  
- La magia de ver cómo la máquina "aprende" de sus errores  

## El desafío: Tabla de verdad OR

La red debe aprender esta lógica:

| Entrada 1 | Entrada 2 | ¿Qué debería salir? |
|-----------|-----------|---------------------|
| 0         | 0         | 0                   |
| 0         | 1         | 1                   |
| 1         | 0         | 1                   |
| 1         | 1         | 1                   |

## Cómo aprende la neurona

El perceptrón empieza "en blanco" (pesos y bias en cero) y va aprendiendo mediante:

- **Pesos iniciales**: 0, 0 (no sabe nada al principio)  
- **Bias inicial**: 0  
- **Velocidad de aprendizaje**: 1 (aprende rápido)  
- **Función de decisión**: Escalón (si la suma es positiva → 1, sino → 0)  
- **Regla de corrección**: Cuando se equivoca, ajusta los pesos según la fórmula del perceptrón  

## Tecnología

- **Python 3** – El lenguaje base  
- **NumPy** – Para las operaciones matemáticas básicas  
