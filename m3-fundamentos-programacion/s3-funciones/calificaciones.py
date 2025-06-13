import math

# Funciones
def calcularPromedio(list:list[int])-> float:
    '''
    Calcula el promedio de una lista de numeros.
    '''
    return sum(list)/len(list)

# Main
notas=[10,7,6,8,9]
print(calcularPromedio(notas))
print(math.sqrt(notas[4]))
print(type(notas))