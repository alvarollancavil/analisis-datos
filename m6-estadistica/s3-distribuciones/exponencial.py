import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Parámetro de escala (λ = 1/media)
# lambda es la tasa de ocurrencia de eventos.
scale = 1 #(λ = 1/media)

# Rango de valores
x = np.linspace(0, 10, 1000)

# Densidad de probabilidad
y = expon.pdf(x, scale=scale)

# Graficar
plt.plot(x, y, label=f'λ = {1/scale}', color='green')
plt.title('Distribución Exponencial')
plt.xlabel('Tiempo')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.legend()
plt.show()