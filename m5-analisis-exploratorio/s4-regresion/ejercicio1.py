import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model  import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import math

# Años de experiencia 
x = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1) 
# Sueldo en miles 
y = np.array([30,35, 37, 40, 45, 50, 52, 55]) 

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

# Prediccion para 6.5 años de experiencia
print(f"Prediccion de sueldo para 6.5 años: {modelo.predict([[6.5]])}")

# Grafica
plt.scatter(x,y,color='blue',label='Datos reales')
plt.plot(x,modelo.predict(x),color='red',label='Linea de regresion')
plt.xlabel('Años de experiencia')
plt.ylabel('Sueldo en miles')
plt.legend()
plt.show()

