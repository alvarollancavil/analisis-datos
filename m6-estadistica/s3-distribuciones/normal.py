import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros de la distribución normal
mu = 0       # media
sigma = 1    # desviación estándar

# Crear un rango de valores en el eje x
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Calcular la densidad de probabilidad para cada valor
y = norm.pdf(x, mu, sigma)

# Graficar
plt.plot(x, y, label='Distribución Normal', color='blue')
plt.title('Distribución Normal estándar (μ=0, σ=1)')
plt.xlabel('Valores')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.legend()
plt.show()