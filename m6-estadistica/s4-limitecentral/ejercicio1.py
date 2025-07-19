# Lanza una moneda equilibrada (probabilidad de cara = 0.5)
# un gran número de veces. 
 
# a) Simula con Python el lanzamiento de una moneda 10, 100, 1000 y 10000 veces. 
# b) Calcula la proporción de caras en cada experimento 
# c) Grafica cómo la proporción de caras se aproxima a 0.5 conforme aumenta el número de lanzamientos.

import numpy as np
import matplotlib.pyplot as plt

numeroLanzamientos=[
    10,100,1000,10000
    ]

resultadosLanzamientos=[
    np.random.choice([0,1],size=numeroLanzamientos[0],p=[0.5,0.5]),
    np.random.choice([0,1],size=numeroLanzamientos[1],p=[0.5,0.5]),
    np.random.choice([0,1],size=numeroLanzamientos[2],p=[0.5,0.5]),
    np.random.choice([0,1],size=numeroLanzamientos[3],p=[0.5,0.5]),
    ]

promediosAcumulados=[
    np.cumsum(resultadosLanzamientos[0])/np.arange(1,numeroLanzamientos[0]+1),
    np.cumsum(resultadosLanzamientos[1])/np.arange(1,numeroLanzamientos[1]+1),
    np.cumsum(resultadosLanzamientos[2])/np.arange(1,numeroLanzamientos[2]+1),
    np.cumsum(resultadosLanzamientos[3])/np.arange(1,numeroLanzamientos[3]+1),
    ]

plt.figure(figsize=(15,8))
plt.subplot(2,2,1)
plt.plot(promediosAcumulados[0])
plt.title("Proporcion de caras 10 lanzamientos")
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(promediosAcumulados[1])
plt.title("Proporcion de caras 100 lanzamientos")
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(promediosAcumulados[2])
plt.title("Proporcion de caras 1000 lanzamientos")
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(promediosAcumulados[3])
plt.title("Proporcion de caras 10000 lanzamientos")
plt.grid(True)


plt.show()