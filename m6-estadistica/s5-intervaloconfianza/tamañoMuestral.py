import math

# nivelConfianza 0,9=>z=1.645 0.95=>z=1.96 0.99=>z=2.576
Z=1.96
# variabilidad esperada (conservador)
P=0.5
# margen error 5%
E=0.05
# tamaño de la poblacion
N=10000

# Tamano muestral
n=(Z**2*P*(1-P))/E**2

# Ajuste
nAjustada=n/(1+((n-1)/N))

print(f"tamaño muestral (pob. infinita): {math.ceil(n)}")
print(f"tamaño muestral (pob. finita): {math.ceil(nAjustada)}")