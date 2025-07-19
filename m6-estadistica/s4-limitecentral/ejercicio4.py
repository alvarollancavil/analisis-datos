# Tienes una población simulada de alturas de 100000 personas 
# con distribución normal (media = 165 cm, o = 10 cm). 

# a) Muestra 100 personas al azar y grafica su histograma comparándolo con la distribución de la población. 
# b) Repite el muestreo 500 veces y construye la distribución muestral de las medias. 
# c) Analiza las diferencias: 
# Forma de la distribución de la población. 
# Forma de una sola muestra 
# Forma de la distribución muestral. 

import numpy as np
import matplotlib.pyplot as plt

poblacion=np.random.normal(loc=165,scale=10,size=100000)

# Muestra aleatoria
muestraInicial=np.random.choice(poblacion,size=100,replace=False)

# Distribucion muestral
tamañoMuestras=[100]
numeroMuestras=500
mediasMuestrales=[]

i=0
for tamañoMuestra in tamañoMuestras:
    mediasMuestral=[]
    for _ in range(numeroMuestras):
        muestra=np.random.choice(poblacion,size=tamañoMuestra,replace=False)
        mediasMuestral.append(np.mean(muestra))
    mediasMuestrales.append(mediasMuestral)
    i=i+1

# Grafica
plt.figure(figsize=(16,6))
plt.subplot(1,3,1)
plt.hist(poblacion,bins=30,color='grey',edgecolor='black')
plt.title("Forma de la distribución de la población")

plt.subplot(1,3,2)
plt.hist(muestraInicial,bins=30,color='skyblue',edgecolor='black')
plt.title("Forma de una sola muestra tamañoMuestra=100")

plt.subplot(1,3,3)
plt.hist(mediasMuestrales[0],bins=30,color='orange',edgecolor='black')
plt.title("Forma de la distribución muestral tamañoMuestra=100")

plt.tight_layout()
plt.show()