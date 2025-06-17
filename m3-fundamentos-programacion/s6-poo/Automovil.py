class Automovil:
    def __init__(self,marca,modelo,color):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.saldoLitros=0

    def cargaCombustible(self,litros):
        self.saldoLitros+=litros

    def avanza(self,distancia):
        if distancia>0:
            if self.saldoLitros>0:
                self.saldoLitros-=distancia*8 # km*lts/km
            else:
                print("Sin combustible")
        else:
            print("Distancia debe ser >0")
