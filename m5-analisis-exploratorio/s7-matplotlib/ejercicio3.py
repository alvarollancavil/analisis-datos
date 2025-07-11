# 3. Guardar el gráfico en un archivo 
# Guarda el gráfico anterior como archivo PNG y PDF. 

import matplotlib.pyplot as plt

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"] 
temperaturas = [22, 24, 19, 21, 23, 25, 20]

plt.plot(dias, temperaturas, color='red', linestyle='dashed') 
plt.xlabel('Dias') 
plt.ylabel('Temperaturas') 
plt.title('Gráfico temperaturas diarias') 
plt.savefig("graficoTemperaturas.png")