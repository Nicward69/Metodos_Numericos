import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Definir la función f(x, y)
def f(x, y):
    return y * x**2 - 1.1 * y

# Condiciones iniciales
x0 = 0
y0 = 1
h = 0.05  # Tamaño del paso
x_end = 2  # Extremo del intervalo

# Número de pasos
n_steps = int((x_end - x0) / h)

# Inicializar arrays para x y y
x = np.linspace(x0, x_end, n_steps + 1)
y = np.zeros(n_steps + 1)

# Condición inicial
y[0] = y0

# Método de Euler
for i in range(n_steps):
    y[i + 1] = y[i] + h * f(x[i], y[i])

# Graficar la solución
plt.plot(x, y, label='Aproximación con Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la EDO usando el Método de Euler')
plt.legend()
plt.grid(True)

# Crear un DataFrame con los resultados
resultados = pd.DataFrame({'x': x, 'y': y})

# Imprimir los resultados en un DataFrame
print("Resultados de la aproximación de Euler:")
print(resultados)

plt.show()
