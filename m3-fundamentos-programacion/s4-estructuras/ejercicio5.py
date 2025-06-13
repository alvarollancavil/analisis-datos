monedas={"Euro":"€","Dolar":"$","Yen":"¥"}

nombreMoneda=input("¿Moneda? ").capitalize()

if(nombreMoneda in monedas):
    print(monedas[nombreMoneda])
else:
    print("Divisa no encontrada")