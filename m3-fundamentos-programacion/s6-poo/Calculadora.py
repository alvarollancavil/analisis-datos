class Calculadora:
    def __init__(self,numero1:float,numero2:float):
        self.numero1=numero1
        self.numero2=numero2
    
    def suma(self):
        return self.numero1+self.numero2
    def resta(self):
        return self.numero1-self.numero2
    def multiplicacion(self):
        return self.numero1*self.numero2
    def division(self):
        if(self.numero2==0):
            return "Divisior debe ser distinto de cero."
        else:
            return self.numero1/self.numero2