# Ejemplo de clase (Condicionales)

try:
    nota= float(input("Ingresa nota: "))
    asistencia=float(input("Asistencia?"))
    participa=input("Participa? (si/no)")
    #valida rango nota
    if(nota<0 or nota>100):
        print("Nota invalida. Nota debe ser entre 0 y 100.")
        exit()
    #valida rango asisttencia
    if(asistencia<0 or asistencia>100):
        print("Asistencia invallida. debe ser entre 0 y 100")
        exit()
    #valida participacion
    if not (participa.lower()=="si" or participa.lower()=="no"):
        print(f"participacion invalida: {participa.lower}")
        exit()
    #Valoraciones
    if(nota>=90 and (asistencia>=90 or participa.lower()=="si")):
        print(f"{nota:.2f} Es una muy buena nota.")
    elif(nota>=80 and (asistencia>=80 or participa.lower() =="si")):
        print(f"{nota:.2f} Bieen")
    elif(nota>=70 and( asistencia>=70 or participa.lower()=="si")):
        print(f"{nota:.2f} Puedes mejorar")
    else:
        print(f"{nota:.2f} Mal. Suerte a la otra.")
except:
    print("Algo salio mal.")


    #Operador ternario
    mensaje = "Aprobado" if nota >= 70 else "Reprobado"
    print(mensaje)