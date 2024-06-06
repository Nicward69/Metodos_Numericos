import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Definir la función f(x, y)
def f(x, y):
    return y * x**2 - 1.1 * y

# Función del método de Heun
def heun_method(f, x0, y0, h, x_end, es=1):
    n_steps = int((x_end - x0) / h)
    x = np.linspace(x0, x_end, n_steps + 1)
    y = np.zeros(n_steps + 1)
    y[0] = y0
    results = []

    for i in range(n_steps):
        # Paso predictor
        y_pred = y[i] + h * f(x[i], y[i])
        
        # Iteración del corrector
        y_corr = y[i] + (h / 2) * (f(x[i], y[i]) + f(x[i+1], y_pred))
        e_s = np.abs((y_corr - y_pred) / y_corr) * 100
        while e_s > es:
            y_pred = y_corr
            y_corr = y[i] + (h / 2) * (f(x[i], y[i]) + f(x[i+1], y_pred))
            e_s = np.abs((y_corr - y_pred) / y_corr) * 100
        
        y[i + 1] = y_corr
        results.append((x[i+1], y_corr, e_s))
    
    return x, y, results

# Condiciones iniciales
x0 = 0
y0 = 1
h = 0.5
x_end = 2

# Resolver con el método de Heun
x_heun, y_heun, heun_results = heun_method(f, x0, y0, h, x_end)

# Crear DataFrame para tabular los resultados
df_heun = pd.DataFrame(heun_results, columns=['x', 'y', 'Error (%)'])
df_heun.index.name = 'Paso'
df_heun

# Graficar la solución
plt.plot(x_heun, y_heun, label='Método de Heun (h = 0.5)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la EDO usando el Método de Heun')
plt.legend()
plt.grid(True)
plt.show()

df_heun
