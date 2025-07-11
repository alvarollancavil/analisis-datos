# 2. Personaliza tu gráfico 
# Cambia el color, el estilo de línea y marca los puntos con 
# un círculo. 
# Añade etiquetas al eje X e Y y un título. 

import matplotlib.pyplot as plt

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"] 
temperaturas = [22, 24, 19, 21, 23, 25, 20]

plt.plot(dias, temperaturas, color='red', linestyle='dashed') 
plt.xlabel('Dias') 
plt.ylabel('Temperaturas') 
plt.title('Gráfico temperaturas diarias') 
plt.show() 