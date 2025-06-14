print("\n========= Listas =============\n")

frutas=["Manzana","Platano","Cereza"]

for fruta in frutas:
    print(f"Me gusta la fruta %s."%fruta)
    if(fruta=="Platano"):
        break

print("\n========= Diccionarios =============\n")

precios={"Manzana":100,"Platano":80,"Cereza":120}
for fruta,precio in precios.items():
    print(f"La fruta %s vale %d pesos.\n"%(fruta,precio))

print("\n========= Range =============\n")

for i in range(1,6,2):
    print(i)