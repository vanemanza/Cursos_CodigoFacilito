import pandas as pd
import numpy as np

usuarios = {
    'nombre': ['vane', 'reni', 'faus', 'augus'],
    'calificacion': [6,9,9.5,10],
    'edad': [46,17,14,11],
    'aprobado': [False, True, True, True]
}

df = pd.DataFrame(usuarios)
print(df)

pd.DataFrame(usuarios, index=[1,2,3,4], columns=['nombre', 'calificacion', 'edad'])

print(df)

# apply

df.apply(lambda row: row['edad'] + 1, axis=1) # asi solo obtengo una nueva serie


# si quiero modificar el df(toda la columna) lo guardo en una variable
df.edad = df.apply(lambda row: row['edad'] + 1, axis=1)
print(df)

