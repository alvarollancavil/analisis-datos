import numpy as np
from sklearn.linear_model  import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import math

Horas_Estudio = np.array([5, 12, 1, 7, 13]).reshape(-1, 1) 
Calificacion = np.array([50.9,90.16,49.38,61.62,86.13])

x=Horas_Estudio
y=Calificacion

# Modelo
modelo=LinearRegression()
modelo.fit(x,y)
# Pendiente e interseccion
print(f"Pendiente: {modelo.coef_[0]:.2f}")
print(f"Interseccion: {modelo.intercept_:.2f}")
# R²
r2 = r2_score(y, modelo.predict(x))
print("R²:", r2)
# MSE
mse = mean_squared_error(y, modelo.predict(x))
print("MSE:", mse)
print(f"sqrt(mse): {math.sqrt(mse)}")

# Grafica
plt.scatter(x,y,color='blue',label='Datos reales')
plt.plot(x,modelo.predict(x),color='red',label='Linea de regresion')
plt.xlabel('Horas_Estudio')
plt.ylabel('Calificacion')
plt.legend()
plt.show()