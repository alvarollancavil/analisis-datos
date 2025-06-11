password=input("password?: ")
print("Password guardada.")

reintentar=True
while reintentar:
    passwordConfirm=input("confirmar password: ")
    if(password.lower()==passwordConfirm.lower()):
        print("Confirmacion exitosa.")
        reintentar=False
    else:
        print("Password no coinciden.")
        reintentar=input("reintentar (s/n)") == "s"
        

    