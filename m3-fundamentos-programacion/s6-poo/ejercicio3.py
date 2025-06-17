from Calculadora import Calculadora

numero1=float(input("Ingresar numero1: "))
operacion=input("Operacion (+ - * /): ")
numero2=float(input("Ingresar numero2: "))

calculadora=Calculadora(numero1,numero2)

if(operacion=="+"):
    resultado=calculadora.suma()
elif(operacion=="-"):
    resultado=calculadora.resta()
elif(operacion=="*"):
    resultado=calculadora.multiplicacion()
elif(operacion=="/"):
    resultado=calculadora.division()
else:
    resultado="Operacion desconocida"

if(type(resultado)==float):
    print(f"{numero1} {operacion} {numero2} = {resultado}")
else:
    print(resultado)
