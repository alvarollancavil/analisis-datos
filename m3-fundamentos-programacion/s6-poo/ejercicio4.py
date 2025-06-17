from Dado import Dado

# Funciones
def solicitarNumero():
    numero=int(input("Ingresar numero entre 1 y 6: "))
    while(numero<1 or numero>6):
        print("Numero invalido. Debe estar en el rango 1-6")
        numero=int(input("Ingresar numero entre 1 y 6: "))
    return numero

# Main
dado=Dado()
dado.girar()

numero=solicitarNumero()
while(numero!=dado.valor):
    print("Suerte para la proxima. Intentalo nuevamente")
    numero=solicitarNumero()
print(f"Ganaste el numero del dado es: {dado.valor}")