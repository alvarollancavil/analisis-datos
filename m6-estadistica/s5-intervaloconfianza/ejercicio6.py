# Se prueba un nuevo tipo de fertilizante en 9 parcelas, 
# obteniendo rendimientos (en kg por parcela): 
# [50, 55, 53, 52, 51, 49, 54, 50, 52] 
# Calcula el intervalo de confianza al 95% para el 
# rendimiento medio poblacional. 

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

muestra=np.array([50, 55, 53, 52, 51, 49, 54, 50, 52])
tamañoMuestra=len(muestra)
mediaMuestral=np.mean(muestra)
desviacionStd=np.std(muestra,ddof=1) # muestral
confianza=0.95 # z=1.96

#=======================================================
# calculo intervalo
#=======================================================
gradosLibertad=tamañoMuestra-1
alpha=1-confianza
t=stats.t.ppf(1-alpha/2,gradosLibertad)

errorStd=desviacionStd/np.sqrt(tamañoMuestra)
margenError=t*errorStd

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