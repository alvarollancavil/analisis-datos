# 6. Histograma 
# Genera 1000 valores aleatorios con distribución 
# normal y crea un histograma con 20 bins. 

import numpy as np
import matplotlib.pyplot as plt

datos = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(datos, bins=20, color='mediumseagreen', edgecolor='black')
plt.title('Histograma de Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()