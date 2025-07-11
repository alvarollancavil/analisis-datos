# 10. Anotaciones y líneas de referencia 
# En un gráfico de evolución de precios, dibuja una línea 
# horizontal que indique el precio objetivo y anota el punto 
# más alto de la serie. 

import matplotlib.pyplot as plt
import numpy as np

# Datos simulados de precios
dias = np.arange(1, 11)
precios = [100, 105, 98, 115, 120, 118, 125, 130, 128, 127]
precio_objetivo = 122

# Buscar el punto más alto
indice_max = np.argmax(precios)
dia_max = dias[indice_max]
precio_max = precios[indice_max]

# Crear gráfico
plt.plot(dias, precios, marker='o', color='teal')
plt.title('Evolución de Precios')
plt.xlabel('Día')
plt.ylabel('Precio')

# Línea de referencia horizontal
plt.axhline(precio_objetivo, color='red', linestyle='--', linewidth=1.5, label=f'Precio objetivo: {precio_objetivo}')

# Anotación del punto más alto
plt.annotate(f'Máximo: {precio_max}',
             xy=(dia_max, precio_max),
             xytext=(dia_max + 1, precio_max + 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10,
             backgroundcolor='white')

plt.legend()
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()