# 1. Primer gráfico de línea simple 
# Crea un gráfico de línea que muestre la evolución de las 
# temperaturas durante una semana. 
# dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"] 
# temperaturas = [22, 24, 19, 21, 23, 25, 20]

import matplotlib.pyplot as plt

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"] 
temperaturas = [22, 24, 19, 21, 23, 25, 20]

plt.plot(dias,temperaturas)
plt.show()
