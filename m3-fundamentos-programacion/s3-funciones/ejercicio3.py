# Funciones
def factorial(n:int)->int:
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)

def isValidInput(n:int)->bool:
    if not (type(n)==int):
        return False
    if (n<=0):
        return False
    return True

# Main
try:
    n=int(input("Ingresar factorial n: "))
    if(isValidInput(n)):
        print(factorial(n))
    else:
        print("Entrada invalida.")
except:
    print("Error")
