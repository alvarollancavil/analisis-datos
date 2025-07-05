import numpy as np
from sklearn.linear_model  import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import math

Metros_Cuadrados = np.array([152, 229, 142, 64, 156]).reshape(-1,1)
Precio = np.array([81821.23, 123377.48, 79943.32, 39549.98, 75928.34])

x=Metros_Cuadrados
y=Precio

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
plt.xlabel('Metros_Cuadrados')
plt.ylabel('Precio')
plt.legend()
plt.show()