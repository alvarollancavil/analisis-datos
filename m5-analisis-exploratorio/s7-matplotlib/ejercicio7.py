# 7. Múltiples gráficos en una figura (subplot) 
# Muestra en una sola figura: 
# Un gráfico de líneas. 
# Un gráfico de barras. 
# Un gráfico de dispersión. 
# Un histograma. 

import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.arange(1, 6)
y_linea = np.array([1, 4, 6, 8, 10])
y_barras = np.array([5, 7, 3, 4, 6])
peso = [60, 72, 75, 80, 90, 100, 110]
altura = [1.60, 1.70, 1.75, 1.80, 1.85, 1.90, 2.00]
datos_normales = np.random.normal(loc=0, scale=1, size=1000)

# Crear figura y subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Visualización Comparativa', fontsize=14)

# Gráfico de líneas
axs[0, 0].plot(x, y_linea, marker='o', color='steelblue')
axs[0, 0].set_title('Gráfico de Líneas')
axs[0, 0].grid(True)

# Gráfico de barras
axs[0, 1].bar(x, y_barras, color='salmon')
axs[0, 1].set_title('Gráfico de Barras')
axs[0, 1].grid(axis='y', linestyle='--')

# Gráfico de dispersión
axs[1, 0].scatter(peso, altura, color='darkorange')
axs[1, 0].set_title('Gráfico de Dispersión')
axs[1, 0].set_xlabel('Peso (kg)')
axs[1, 0].set_ylabel('Altura (m)')
axs[1, 0].grid(True)

# Histograma
axs[1, 1].hist(datos_normales, bins=20, color='mediumseagreen', edgecolor='black')
axs[1, 1].set_title('Histograma')
axs[1, 1].grid(axis='y', linestyle='--')

# Ajustar diseño
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()