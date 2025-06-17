class Estudiante:
    def __init__(self,nombre:str,nota:int):
        self.nombre=nombre.capitalize()
        self.nota=nota
    
    def getNombre(self):
        return self.nombre
    
    def getNota(self):
        return self.nota
    
    def getAprobacion(self):
        if(self.nota>=4):
            return (f"Aprueba con nota {self.nota}")
        else:
            return (f"Reprueba con nota {self.nota}")