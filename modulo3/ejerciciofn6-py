import statistics

# Funciones
def estadisticas(lista:list)->dict:
    media=statistics.mean(lista)
    varianza=statistics.variance(lista)
    desviacion=statistics.stdev(lista)
    resp={"Media":media,"Varianza":varianza,"DesviacionStd":desviacion}
    return resp

# Main
lista=[10,20,30,40,50,60]
print(estadisticas(lista))