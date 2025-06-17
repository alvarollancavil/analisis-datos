class Persona:
    def __init__(self,nombre:str,edad:int):
        self.nombre=nombre
        self.edad=edad

    def cumpleaños(self):
        self.edad+=1