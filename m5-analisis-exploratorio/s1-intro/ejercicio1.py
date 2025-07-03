import pandas as pd
import matplotlib.pyplot as plt

# Escribir un programa que pregunte al usuario por las 
# ventas de un rango de años y muestre por pantalla 
# un diagrama de líneas con la evolución de las ventas. 

añoInicial=int(input("Ingresar año inicial: "))
añoFinal=int(input("Ingresar año final: "))

seriesVentas=pd.Series(dtype=int)

for i in range(añoFinal-añoInicial):
    año=añoInicial+i
    venta=int(input(f"Ingresar venta {año}: "))
    new_elem = pd.Series([venta], index=[año])
    seriesVentas=pd.concat([seriesVentas,new_elem])

print(seriesVentas)
seriesVentas.plot(kind='line', title='Evolucion de las ventas',xlabel='Año', ylabel='Ventas')
plt.show()