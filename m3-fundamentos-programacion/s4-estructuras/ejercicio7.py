precioFrutas={"Platano":1.35,"Manzana":0.8,"Pera":0.85,"Naranja":0.7}

nombreFruta=input("¿Nombre fruta?: ").capitalize()
kilosFruta=float(input("¿Kilos de fruta?: "))

if(nombreFruta in precioFrutas):
    precioTotal=precioFrutas[nombreFruta]*kilosFruta
    print(f"Precio total: {precioTotal:.2f}")
else:
    print("Fruta no encontrada")