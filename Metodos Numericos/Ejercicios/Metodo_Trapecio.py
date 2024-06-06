import numpy as np

# Datos de tiempo (en minutos) y carros pasados
tiempo = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 110, 120])
carros = np.array([9, 12, 10, 14, 9, 11, 10, 11, 13, 8, 9, 10, 9, 8, 7, 9, 6, 8, 10])

# Método del trapecio
trapecio = np.trapz(carros, tiempo)

# Imprimir el resultado
print(f"Integral por el método del trapecio: {trapecio}")
