import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.0074*x**4 - 0.284*x**3 + 3.355*x**2 - 12.183*x + 5

x = np.linspace(15, 20, 100) 
y = f(x)

plt.figure(figsize=(8, 6))
plt.axhline(0, color='k', lw=0.5)  
plt.axvline(0, color='k', lw=0.5)  
plt.plot(x, y)
plt.scatter(16.3445843, 0, color='r', marker='o', s=50, zorder=10)  
plt.annotate('Raíz: x = 16.3445843', xy=(16.3445843, 0.2), xytext=(17, 1),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title('Gráfica de f(x) = 0.0074x^4 - 0.284x^3 + 3.355x^2 - 12.183x + 5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

print("Numpy instalado correctamente!")
