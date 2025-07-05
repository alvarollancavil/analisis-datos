import numpy as np
from sklearn.linear_model  import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import math

velocidad = np.array([31, 30, 77, 41, 98]).reshape(-1, 1) 
consumo = np.array([13.67, 14.39, 10.82, 12.10, 10.43])

x=velocidad
y=consumo

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
plt.xlabel('Velocidad_kmh')
plt.ylabel('Consumo_litros_100km')
plt.legend()
plt.show()