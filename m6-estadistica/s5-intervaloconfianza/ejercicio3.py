# Una muestra de 15 estudiantes obtuvo un puntaje 
# promedio de 78 en un examen. 
# La desviación estándar de la muestra fue de 10. 
# No se conoce la desviación estándar poblacional. 
# Calcula el intervalo de confianza al 95% para el puntaje 
# medio poblacional. 

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

mediaMuestral=78
tamañoMuestra=15
desviacionStd=10 # muestral
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