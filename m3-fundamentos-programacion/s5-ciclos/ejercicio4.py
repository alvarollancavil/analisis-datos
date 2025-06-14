capital=float(input("Ingresar capital inicial: "))
interes=float(input("Ingresar interes anual (%): "))
tiempo=int(input("Ingresar tiempo (años): "))

for i in range(1,tiempo+1):
    capital=capital+capital*(interes/100)

print(f"Capital final: {capital:.2f}")