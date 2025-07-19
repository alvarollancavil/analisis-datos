import numpy as np
import matplotlib.pyplot as plt

lanzamientos=10000
resultadosLanzamientos=np.random.choice([0,1],size=lanzamientos,p=[0.5,0.5])

promediosAcumulados=np.cumsum(resultadosLanzamientos)/np.arange(1,lanzamientos+1)

plt.figure(figsize=(10,6))
plt.plot(promediosAcumulados,label='Promedio Acumulado')
plt.axhline(0.5,color='red',linestyle='--',label="Valor esperado 0.5")
plt.xlabel("Lanzaminetos")
plt.ylabel("Promedio caras")
plt.title("Ley grandes numeros lanzamiento de moneda")
plt.legend()
plt.grid(True)
plt.show()