# En un estudio de tiempos de respuesta de un servidor, 
# se obtiene un promedio muestral de 240 ms con una 
# muestra de 100 mediciones. 
# La desviación estándar poblacional se conoce y es de 
# 20 ms. 
# Calcula el intervalo de confianza al 99% para el tiempo 
# promedio de respuesta. 

import numpy as np
import matplotlib.pyplot as plt

mediaMuestral=240
tamañoMuestra=100
desviacionStd=20 # Poblacional
confianza=0.99 # z=2.576

#=======================================================
# calculo intervalo
#=======================================================
errorStd=desviacionStd/np.sqrt(tamañoMuestra)
margenError=2.576*errorStd

print(f"Media muestral= {mediaMuestral:.3f}")
print(f"Intervalo confianza : {mediaMuestral-margenError:.3f} - {mediaMuestral+margenError:.3f}")

#=======================================================
# Grafica
#=======================================================
limInferior=mediaMuestral-margenError
limSuperior=mediaMuestral+margenError
plt.figure(figsize=(12,6))
plt.errorbar(x=mediaMuestral,y=1,xerr=margenError,fmt='o',color='blue',ecolor='red',elinewidth=3,capsize=8)
plt.axvline(mediaMuestral,color='green',linestyle='--',label='media')
plt.axvline(limInferior,color='gray',linestyle=':',label='Limite inferior')
plt.axvline(limSuperior,color='gray',linestyle=':',label='Limite Superior')
plt.yticks([])
plt.xlabel('valor')
plt.title(f'Intervalo de confianza del {confianza*100:.0f}% para la media')
plt.legend()
plt.tight_layout()
plt.show()