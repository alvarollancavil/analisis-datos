import pandas as pd
import numpy as np

#======================================================================================
# Generacion de datos
#======================================================================================
# Semilla para reproducibilidad
np.random.seed(42)

# Crear datos simulados
regiones = ['Norte', 'Centro', 'Sur']
escuelas_por_region = {
    'Norte': ['Escuela A', 'Escuela B'],
    'Centro': ['Escuela C', 'Escuela D'],
    'Sur': ['Escuela E', 'Escuela F']
}

# Generar estudiantes por escuela y su puntaje en la prueba
data = []
for region in regiones:
    for escuela in escuelas_por_region[region]:
        for i in range(10):  # 10 estudiantes por escuela
            estudiante = {
                'Región': region,
                'Escuela': escuela,
                'ID_Estudiante': f'{escuela}_{i+1}',
                'Puntaje': np.random.randint(400, 700)  # Simular puntaje de prueba
            }
            data.append(estudiante)

df = pd.DataFrame(data)
print("Base de datos completa:")
print(df.head())

#======================================================================================
# Muestreo Multietapa
#======================================================================================

# Etapa 1: Seleccionar regiones aleatorias
regiones_seleccionadas = np.random.choice(regiones, size=2, replace=False)
df_etapa1 = df[df['Región'].isin(regiones_seleccionadas)]
print("\n Regiones seleccionadas:")
print(regiones_seleccionadas)

# Etapa 2: Seleccionar escuelas dentro de esas regiones
escuelas_disponibles = df_etapa1['Escuela'].unique()
escuelas_seleccionadas = np.random.choice(escuelas_disponibles, size=3, replace=False)
df_etapa2 = df_etapa1[df_etapa1['Escuela'].isin(escuelas_seleccionadas)]
print("\n Escuelas seleccionadas:")
print(escuelas_seleccionadas)

# Etapa 3: Seleccionar estudiantes finales
muestra_final = df_etapa2.sample(n=5)
print("\n Muestra final de estudiantes:")
print(muestra_final)