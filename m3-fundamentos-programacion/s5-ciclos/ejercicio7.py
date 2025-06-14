frase=input("Ingresar frase: ")
letra=input("Ingresar letra: ")

count=0
i=0
while i<len(frase):
    if(letra==frase[i]):
        count+=1
    i+=1

print(f"La letra \'%s\' aparece %d veces en la frase."%(letra,count))