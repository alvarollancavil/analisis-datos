import pandas as pd

def estadisticas(alumnos:dict):
    serieNotas = pd.Series(alumnos)
    return serieNotas.describe().loc[["min","max","mean", "std"]].copy()

# Main
alumnos = {
    "Sofía": 5.0,
    "Mateo": 2.3,
    "Valentina": 7,
    "Lucas": 4,
    "Isabella": 3.9,
    "Tomás": 6,
    "Florencia": 3.8,
    "Benjamín": 3.6,
    "Martina": 4.1,
    "Diego": 5.8
}

print(estadisticas(alumnos))

