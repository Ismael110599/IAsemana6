# Perceptrón para compuerta lógica OR

import numpy as np

# Entradas y salidas esperadas para la compuerta OR
entradas = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])

salidas = np.array([0, 1, 1, 1])  # Salidas esperadas

# Parámetros del perceptrón
pesos = np.zeros(2)  # w1, w2
bias = 0
tasa_aprendizaje = 1
épocas = 10

# Función de activación (escalón)
def escalon(x):
    return 1 if x >= 0 else 0

# Entrenamiento
for epoca in range(épocas):
    print(f"\nÉpoca {epoca+1}")
    error_total = 0

    for i in range(len(entradas)):
        x = entradas[i]
        y_esperado = salidas[i]

        # Calcular salida
        net = np.dot(x, pesos) + bias
        y_predicho = escalon(net)

        # Calcular error y actualizar pesos y bias
        error = y_esperado - y_predicho
        pesos += tasa_aprendizaje * error * x
        bias += tasa_aprendizaje * error

        error_total += abs(error)

        print(f"Entrada: {x}, Esperado: {y_esperado}, Predicho: {y_predicho}, Pesos: {pesos}, Bias: {bias}")

    if error_total == 0:
        print("Red entrenada correctamente ")
        break

# Prueba final
print("\n--- Prueba Final ---")
for x in entradas:
    net = np.dot(x, pesos) + bias
    y = escalon(net)
    print(f"Entrada: {x}, Salida: {y}")


