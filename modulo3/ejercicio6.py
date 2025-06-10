edad=int(input("edad?: "))
if(edad<4):
    print("Gratis")
elif(edad>=4 and edad<18):
    print("5 euros")
else:
    print("10 euros")