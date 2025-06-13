import statistics

str=input("Ingresar numeros separados por coma: ")
numerosStr=str.split(',')
numeros=list(map(int, numerosStr))

media=statistics.mean(numeros)
desviacionStd=statistics.stdev(numeros)

print(f"media: {media:.2f}")
print(f"desviacionStd: {desviacionStd:.2f}")