import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

muestra=np.array([52,49,50,51,48,53,50,49,52,50])
tamañoMuestra=len(muestra)
mediaMuestral=np.mean(muestra)
desviacionStdMuestra=np.std(muestra,ddof=1) #formula de la muestra
confianza=0.95 #Z
gradosLibertad=tamañoMuestra-1
# valores criticos t para 95% confianza
alpha=1-confianza
t=stats.t.ppf(1-alpha/2,gradosLibertad)

errorStd=desviacionStdMuestra/np.sqrt(tamañoMuestra)
margenError=t*errorStd

limInferior=mediaMuestral-margenError
limSuperior=mediaMuestral+margenError

print(f"Media muestral= {mediaMuestral:.2f}")
print(f"Intervalo confianza {confianza*100:.0f}: {limInferior:.2f} - {limSuperior:.2f}")

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