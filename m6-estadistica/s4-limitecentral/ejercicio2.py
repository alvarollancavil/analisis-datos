# Supón que la distribución de edades de una población 
# empleados en una empresa NO es normal, sino sesgada 
# (por ejemplo, más jóvenes que mayores). 

# a) Genera una población de 50000 edades (por ejemplo, distribución exponencial con media de 30 años). 
# b) Toma muestras aleatorias de tamaño 5, 30 y 100, cada una con 1000 repeticiones. 
# c) Grafica los histogramas de las medias muestrales y observa cómo, al aumentar el tamaño de la muestra, la distribución de las 
# medias se aproxima a una normal. 

import numpy as np
import matplotlib.pyplot as plt

poblacion=np.random.exponential(scale=30,size=50000)
tamañoMuestras=[5,30,100]
numeroMuestras=1000
mediasMuestrales=[]

i=0
for tamañoMuestra in tamañoMuestras:
    mediasMuestral=[]
    for _ in range(numeroMuestras):
        muestra=np.random.choice(poblacion,size=tamañoMuestra)
        mediasMuestral.append(np.mean(muestra))
    mediasMuestrales.append(mediasMuestral)
    i=i+1

plt.figure(figsize=(16,6))
plt.subplot(2,2,1)
plt.hist(poblacion,bins=30,color='grey',edgecolor='black')
plt.title("Distribucion exponencial")

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