import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Definir la función f(x, y)
def f(x, y):
    return y * x**2 - 1.1 * y

# Función del método de Euler
def euler_method(f, x0, y0, h, x_end):
    n_steps = int((x_end - x0) / h)
    x = np.linspace(x0, x_end, n_steps + 1)
    y = np.zeros(n_steps + 1)
    y[0] = y0
    for i in range(n_steps):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

# Condiciones iniciales
x0 = 0
y0 = 1
x_end = 2

# Soluciones con diferentes tamaños de paso
h1 = 0.5
x1, y1 = euler_method(f, x0, y0, h1, x_end)

h2 = 0.25
x2, y2 = euler_method(f, x0, y0, h2, x_end)

# Crear DataFrames con los resultados
resultados_h1 = pd.DataFrame({'x': x1, 'y': y1})
resultados_h2 = pd.DataFrame({'x': x2, 'y': y2})

# Graficar las soluciones
plt.plot(x1, y1, label='h = 0.5', marker='o')
plt.plot(x2, y2, label='h = 0.25', marker='x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparación de soluciones con diferentes tamaños de paso usando el Método de Euler')
plt.legend()
plt.grid(True)

# Imprimir los resultados en DataFrames
print("Resultados para h = 0.5:")
print(resultados_h1)
print("\nResultados para h = 0.25:")
print(resultados_h2)

plt.show()
