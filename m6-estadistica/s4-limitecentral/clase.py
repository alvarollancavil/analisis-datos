import numpy as np
import matplotlib.pyplot as plt

poblacion=np.random.exponential(scale=2,size=100000)

# Tamaño de la muestra
n=50
# Numero de muestras
numeroMuestras=1000

# Obtener medias muestrales
mediasMuestral=[]

for _ in range(numeroMuestras):
    muestra=np.random.choice(poblacion,size=50)
    mediasMuestral.append(np.mean(muestra))

# Graficar
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.hist(poblacion,bins=50,color='skyblue',edgecolor='black')
plt.title("Distribucion exponencial")

plt.subplot(1,2,2)
plt.hist(mediasMuestral,bins=30,color='orange',edgecolor='black')
plt.title("Distribucion de medias muestrales (TLC)")

plt.tight_layout()
plt.show()