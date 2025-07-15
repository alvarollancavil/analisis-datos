import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parámetro λ (lambda): promedio de eventos por intervalo
lam = 3

# Valores discretos que queremos graficar
x = np.arange(0, 15)

# PMF de la distribución de Poisson
y = poisson.pmf(x, mu=lam)

# Graficar con stem correctamente
fig, ax = plt.subplots()
markerline, stemlines, baseline = ax.stem(x, y, linefmt='C0-', markerfmt='C0o', basefmt='k-')
plt.title(f'Distribución de Poisson (λ = {lam})')
plt.xlabel('Número de eventos (e/m)')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()