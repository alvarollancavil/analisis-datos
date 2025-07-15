import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parámetros
n = 10       # número de ensayos
p = 0.5      # probabilidad de éxito

# Valores posibles de éxitos
x = np.arange(0, n+1)

# PMF (función de masa de probabilidad)
y = binom.pmf(x, n, p)

# Graficar
fig, ax = plt.subplots()
ax.stem(x, y, basefmt="k-", linefmt='C0-', markerfmt='C0o')
plt.title(f'Distribución Binomial (n={n}, p={p})')
plt.xlabel('Número de éxitos (c)')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()