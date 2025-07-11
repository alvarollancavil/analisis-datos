# 11: Dashboard de clima 
# Crea una figura que muestre 4 tipos de gráficos con 
# datos climáticos: 
# Temperatura semanal (línea) 
# Lluvias por mes (barras) 
# Distribución de humedad (histograma) 
# Porcentaje de días soleados/nublados/lluviosos (pastel) 

import matplotlib.pyplot as plt
import numpy as np

# Datos simulados
dias_semana = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
temperatura = [22, 24, 23, 25, 26, 28, 27]

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
lluvias = [120, 80, 60, 30, 50, 100]

humedad = np.random.normal(loc=70, scale=10, size=1000)  # Distribución simulada

condiciones = ['Soleado', 'Nublado', 'Lluvioso']
frecuencia_dias = [15, 10, 5]

# Estilo general
plt.style.use('seaborn-v0_8-darkgrid')
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Dashboard Climático', fontsize=16)

# Temperatura semanal (línea)
axs[0, 0].plot(dias_semana, temperatura, marker='o', color='coral')
axs[0, 0].set_title('Temperatura Semanal')
axs[0, 0].set_ylabel('°C')
axs[0, 0].grid(True)

# Lluvias por mes (barras)
axs[0, 1].bar(meses, lluvias, color='deepskyblue')
axs[0, 1].set_title('Lluvias Mensuales')
axs[0, 1].set_ylabel('mm')
axs[0, 1].grid(axis='y', linestyle='--')

# Distribución de humedad (histograma)
axs[1, 0].hist(humedad, bins=20, color='mediumseagreen', edgecolor='black')
axs[1, 0].set_title('Distribución de Humedad')
axs[1, 0].set_xlabel('% Humedad')
axs[1, 0].set_ylabel('Frecuencia')

# Porcentaje de días (pastel)
axs[1, 1].pie(frecuencia_dias, labels=condiciones, autopct='%1.1f%%', startangle=90,
              colors=['gold', 'silver', 'lightskyblue'])
axs[1, 1].set_title('Distribución de Condiciones Climáticas')
axs[1, 1].axis('equal')

# Ajustar diseño
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()