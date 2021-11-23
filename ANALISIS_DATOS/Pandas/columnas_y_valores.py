# coding: utf-8
"""
a = pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'])
a
a['nombre']
df = a
df
df['nombre']
df.calificacion
"""

# obtener informacion
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

print(df['nombre'])
print(df.calificacion)
print(df.calificacion[0])
print(df.calificacion[df.calificacion > 9])



