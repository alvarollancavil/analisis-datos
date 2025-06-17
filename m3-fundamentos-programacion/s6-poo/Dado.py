import random

class Dado:
    def __init__(self):
        self.valor=random.randint(1, 6)
    
    def girar(self):
        self.valor=random.randint(1, 6)