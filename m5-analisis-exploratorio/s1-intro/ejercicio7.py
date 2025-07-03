import pandas as pd
import matplotlib.pyplot as plt

# El fichero titanic.csv contiene información sobre los 
# pasajeros del Titanic. Crear un dataframe con 
# Pandas 
df=pd.read_csv("titanic.csv")
print(df.sample(5))

# Diagrama de sectores con los fallecidos y 
# supervivientes.
df['Survived'].value_counts().plot(kind='pie',title="Fallecidos y supervivientes", autopct='%1.1f%%',ylabel='')
plt.legend(['Fallecidos','Supervivientes'])
plt.show()
# 2. Histograma con las edades 
df['Age'].plot(kind='hist',bins=8,title='Histograma de edades',xlabel='Edad',ylabel='Frecuencia')
plt.show()
# 3. Diagrama de barras con el número de personas 
# en cada clase. 
df['Pclass'].value_counts().plot(kind='bar',title='Número de personas por clase',xlabel='Clase',ylabel='Número de personas')
plt.show()
# 4. Diagrama de barras con el número de personas 
# fallecidas y supervivientes en cada clase.
print(df.groupby(['Pclass', 'Survived']).size())
print(df.groupby(['Pclass', 'Survived']).size().unstack())
df.groupby(['Pclass', 'Survived']).size().unstack().plot(kind='bar',title='Fallecidos y supervivientes por clase',xlabel='Clase',ylabel='Número de personas')
plt.legend(['Fallecidos', 'Supervivientes'])
plt.show()
# 5. Diagrama de barras con el número de personas 
# fallecidas y supervivientes acumuladas en cada 
# clase. 
print(df.groupby(['Pclass', 'Survived']).size().unstack().cumsum())
df.groupby(['Pclass', 'Survived']).size().unstack().cumsum().plot(kind='bar',title='Fallecidos y supervivientes acumulados por clase',xlabel='Clase',ylabel='Número de personas')
plt.legend(['Fallecidos', 'Supervivientes']) 
plt.show()
