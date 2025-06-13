numerosLoteria=[]

print("Ingresar 6 numeros de la loteria en rango 1 - 49")
numerosLoteria.append(int(input("ingresar numero (1/6): ")))
numerosLoteria.append(int(input("ingresar numero (2/6): ")))
numerosLoteria.append(int(input("ingresar numero (3/6): ")))
numerosLoteria.append(int(input("ingresar numero (4/6): ")))
numerosLoteria.append(int(input("ingresar numero (5/6): ")))
numerosLoteria.append(int(input("ingresar numero (6/6): ")))

numerosLoteria.sort()
print(numerosLoteria)
