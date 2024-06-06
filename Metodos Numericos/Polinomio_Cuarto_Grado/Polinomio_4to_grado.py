import numpy as np

# Matriz de coeficientes
A = np.array([
    [1, 0, 0, 0, 0],
    [1, 10, 100, 1000, 10000],
    [1, 20, 400, 8000, 160000],
    [1, 30, 900, 27000, 810000],
    [1, 40, 1600, 64000, 2560000],
    [1, 50, 2500, 125000, 6250000]
])

# Vector de términos independientes
b = np.array([88.20, 226.00, 493.30, 875.00, 1325.50, 1857.90])

# Resolver el sistema de ecuaciones utilizando mínimos cuadrados
coefficients, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

# Coeficientes del polinomio
a0, a1, a2, a3, a4 = coefficients
print("Coeficientes del polinomio: ", coefficients)

# Definición del polinomio
def P(x):
    return a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4

# Cálculo de la población en 1995 (x = 26) y 2030 (x = 61)
poblacion_1995 = P(26)
poblacion_2030 = P(61)

print("Población en 1995: ", poblacion_1995)
print("Población en 2030: ", poblacion_2030)