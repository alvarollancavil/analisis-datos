# Una empresa registra el tiempo de ensamble de un 
# producto. 
# Con una muestra de 225 registros, se obtiene una 
# media de 30 minutos. 
# La desviación estándar poblacional es conocida: 5 
# minutos. 
# Calcula el intervalo de confianza al 99% para el tiempo 
# de ensamble promedio. 

import numpy as np
import matplotlib.pyplot as plt

mediaMuestral=30
tamañoMuestra=225
desviacionStd=5 # Poblacional
confianza=0.99 # z=2.576

#=======================================================
# calculo intervalo
#=======================================================
errorStd=desviacionStd/np.sqrt(tamañoMuestra)
margenError=1.96*errorStd

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