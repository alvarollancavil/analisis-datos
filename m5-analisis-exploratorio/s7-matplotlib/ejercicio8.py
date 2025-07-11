# 8. Gráfico de dispersión (scatter plot) 
# Usa los siguientes datos para mostrar una relación 
# entre peso y altura: 
# peso = [60, 72, 75, 80, 90, 100, 110] 
# altura = [1.60, 1.70, 1.75, 1.80, 1.85, 1.90, 2.00] 

import matplotlib.pyplot as plt

peso = [60, 72, 75, 80, 90, 100, 110]
altura = [1.60, 1.70, 1.75, 1.80, 1.85, 1.90, 2.00]

plt.scatter(peso, altura, color='darkorange', marker='o')
plt.title('Relación entre Peso y Altura')
plt.xlabel('Peso (kg)')
plt.ylabel('Altura (m)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()