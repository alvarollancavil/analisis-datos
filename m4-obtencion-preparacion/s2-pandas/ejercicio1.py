import pandas as pd

añoInicial=int(input("Ingresar año inicial: "))
añoFinal=int(input("Ingresar año final: "))

seriesVentas=pd.Series(dtype=float)

for i in range(añoFinal-añoInicial):
    año=añoInicial+i
    venta=float(input(f"Ingresar venta {año}: "))
    new_elem = pd.Series([venta], index=[año])
    seriesVentas=pd.concat([seriesVentas,new_elem])

print(seriesVentas)
print(0.1*seriesVentas)