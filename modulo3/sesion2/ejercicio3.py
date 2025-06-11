print("=======================")
print("Division de dos numeros")
print("=======================")
n1=float(input("Ingresar numero 1: "))
n2=float(input("Ingresar numero 2: "))
if(n2!=0):
    r=n1/n2
    print(f"{n1:.2f} + {n2:.2f} = {r:.2f}")
else:
    print("Numero 2 debe ser distinto de cero.")