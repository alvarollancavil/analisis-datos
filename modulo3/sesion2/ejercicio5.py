nombre=input("nombre? :").lower()
sexo=input("sexo? (m/f): ").lower()

primeraLetra=ord(nombre[0])

if((sexo=="f" and primeraLetra>=97 and primeraLetra<=108)) or ((sexo=="m" and primeraLetra>=111 and primeraLetra<=122)):
    print("Grupo A")
else:
    print("Grupo B")