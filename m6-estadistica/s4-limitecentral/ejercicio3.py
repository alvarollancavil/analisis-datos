# La población de calificaciones de un examen tiene media 70 
# y desviación estándar 10 (puedes simularla con 10000 datos). 

# a) Toma muestras de tamaño 25, 50 y 100. 
# b) Calcula la media de cada muestra y construye la distribución muestral de la media para cada tamaño. 
# c) Grafica los resultados . 

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
poblacion=np.random.normal(loc=70,scale=10,size=10000)
tamañoMuestras=[25,50,100]
numeroMuestras=1000
mediasMuestrales=[]

i=0
for tamañoMuestra in tamañoMuestras:
    mediasMuestral=[]
    for _ in range(numeroMuestras):
        muestra=np.random.choice(poblacion,size=tamañoMuestra,replace=False)
        mediasMuestral.append(np.mean(muestra))
    mediasMuestrales.append(mediasMuestral)
    i=i+1

plt.figure(figsize=(16,6))
plt.subplot(2,2,1)
plt.hist(poblacion,bins=30,color='grey',edgecolor='black')
plt.title("Distribucion normal")

plt.subplot(2,2,2)
plt.hist(mediasMuestrales[0],bins=30,color='skyblue',edgecolor='black')
plt.title("Distribucion de medias muestrales tamañoMuestra=5")

plt.subplot(2,2,3)
plt.hist(mediasMuestrales[1],bins=30,color='orange',edgecolor='black')
plt.title("Distribucion de medias muestrales tamañoMuestra=30")

plt.subplot(2,2,4)
plt.hist(mediasMuestrales[2],bins=30,color='green',edgecolor='black')
plt.title("Distribucion de medias muestrales tamañoMuestra=100")

plt.tight_layout()
plt.show()