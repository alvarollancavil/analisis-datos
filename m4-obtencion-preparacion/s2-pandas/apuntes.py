import pandas as pd

print("=============")
s=pd.Series([10,20,30,40],index=["a","b","c","d"])
s2=pd.Series([10,20,30,40])
print(s)
print(s["d"])
print(s2)

print("=============")
df=pd.DataFrame({
    "Nombre":["Ana","Luis","Carlos","Laura","Alma"],
    "Edad":[25,30,35,20,37],
    "Estado Civil":["soltero","divorciado","casado","soltero","casada"]
    })
print(df)
print("============= fila")
#fila
print(df.loc[0])
print("============= col")
#col
print(df["Nombre"])
#filtrat
print("=============filtrat")
print(df[df["Edad"]>25])
#exploracion
print("=============exp")
print(df.describe())

#cols2
print("============= cols2")
n=["Nombre","Edad","Estado Civil"]
n2=n[0:1]
print(df[n2])

#condicional
print(df[(df["Edad"]>25) & ((df["Estado Civil"]=="casado")|(df["Estado Civil"]=="casada"))])

#exploracion
print("============= exp2")
print(df.info())