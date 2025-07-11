# 12: Análisis de notas de alumnos 
# Simula una base de datos con calificaciones y crea 
# visualizaciones para: 
# Distribución de notas (histograma) 
# Promedio por materia (barra) 
# Comparación por género (boxplot o barras 
# agrupadas) 
# Relación entre estudio y nota (scatter) 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simular base de datos de alumnos
np.random.seed(42)
n = 100
alumnos = pd.DataFrame({
    'Nombre': [f'Alumno{i}' for i in range(n)],
    'Género': np.random.choice(['Masculino', 'Femenino'], size=n),
    'Materia': np.random.choice(['Matemáticas', 'Historia', 'Ciencias'], size=n),
    'Horas_Estudio': np.random.normal(loc=5, scale=2, size=n).round(1),
    'Nota': np.clip(np.random.normal(loc=70, scale=10, size=n), 0, 100).round(1)
})

# --- 1. Histograma: Distribución de notas ---
plt.figure(figsize=(6, 4))
plt.hist(alumnos['Nota'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribución de Notas')
plt.xlabel('Nota')
plt.ylabel('Frecuencia')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# --- 2. Promedio por materia ---
promedios = alumnos.groupby('Materia')['Nota'].mean()
plt.figure(figsize=(6, 4))
promedios.plot(kind='bar', color='salmon')
plt.title('Promedio de Notas por Materia')
plt.ylabel('Nota Promedio')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# --- 3. Comparación por género: boxplot ---
plt.figure(figsize=(6, 4))
alumnos.boxplot(column='Nota', by='Género', grid=False)
plt.title('Comparación de Notas por Género')
plt.suptitle('')
plt.xlabel('Género')
plt.ylabel('Nota')
plt.tight_layout()
plt.show()

# --- 4. Relación estudio vs nota: scatter ---
plt.figure(figsize=(6, 4))
plt.scatter(alumnos['Horas_Estudio'], alumnos['Nota'], color='mediumseagreen', alpha=0.7)
plt.title('Relación entre Horas de Estudio y Nota')
plt.xlabel('Horas de Estudio')
plt.ylabel('Nota')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()