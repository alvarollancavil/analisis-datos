import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
poblacion=np.random.normal(loc=170,scale=10,size=10000)

tamañoMuestra=30
numeroMuestras=1000

mediaMuestral=[]
for _ in range(numeroMuestras):
    muestra=np.random.choice(poblacion,size=tamañoMuestra,replace=False)
    mediaMuestral.append(np.mean(muestra))

plt.figure(figsize=(12,5))
plt.hist(mediaMuestral,bins=30,color='skyblue',edgecolor='black')
plt.title("Distribucion de muestreo medias")
plt.xlabel("Media de la muestra")
plt.ylabel("Frecuencia")
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.show()