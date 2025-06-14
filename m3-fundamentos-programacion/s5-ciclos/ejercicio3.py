numero=int(input("Ingresar numero: "))
numeros=[]
while numero>=0:
    numeros.append(numero)
    numero-=1

print(", ".join(map(str, numeros)))