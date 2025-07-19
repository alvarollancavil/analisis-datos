# Una fábrica produce tornillos con una longitud 
# promedio muestral de 5.2 cm a partir de una muestra de 64 tornillos. 
# Se sabe que la desviación estándar poblacional es 0.8 cm. 
# Calcula el intervalo de confianza al 95% para la media poblacional. 

import numpy as np
import matplotlib.pyplot as plt

mediaMuestral=5.2
tamañoMuestra=64
desviacionStd=0.8 # Poblacional
confianza=0.95 # z=1.96

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