# Escribir una función que reciba una serie de Pandas 
# con el número de ventas de un producto durante los 
# meses de un trimestre y un título y cree un diagrama 
# de sectores con las ventas en formato png con el 
# titulo dado. El diagrama debe guardarse en un fichero 
# con formato png y el titulo dado. 

import pandas as pd
import matplotlib.pyplot as plt

def graficar_ventas(serie_ventas,titulo):
    serie_ventas.plot(kind='pie',title=titulo, autopct='%1.1f%%',figsize=(8,8),ylabel='')
    plt.savefig(f"{titulo}.png")
    plt.show()

# Main
meses = ['Enero', 'Febrero', 'Marzo']
ventas = [150, 200, 170]
serie_ventas = pd.Series(data=ventas, index=meses, name='Ventas')
print(serie_ventas)
graficar_ventas(serie_ventas,"Ventas trimestre")