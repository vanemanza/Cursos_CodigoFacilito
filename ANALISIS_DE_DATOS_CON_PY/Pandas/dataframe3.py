# coding: utf-8
"""
np.arange(12)
np.arange(12).reshape(3,4)
a = np.arange(12).reshape(3,4)
a
df = pd.DataFrame(a)
df
df = pd.DataFrame(a, columns=['A', 'B', 'C', 'D'], index=['a', 'b', 'c'])
df
df.columns = 'AB', 'BB', 'CB', 'DB'
df
df.index = '1a', '2b', '3c'
df
df.rename(columns={'AB': 'ab'})
df.calificacion
df.calificacion[0]
df.calificacion[df.calificacion > 9]
df['nombre']
"""

# otra forma de crear un df es x medio de una matriz

import numpy as np
import pandas as pd

matriz = np.arange(12).reshape(3,4)
print(matriz)

df = pd.DataFrame(matriz)
print(df)

df = pd.DataFrame(matriz, columns=['A', 'B', 'C', 'D'], index=['a', 'b', 'c'])
print(df)

# redefinir el nombre de columnas e indices:
df.columns = 'AB', 'BB', 'CB', 'DB'
df.index = '1a', '1b', 'ac'
print(df)

# renombrar solo una columna o solo un indice:
df = df.rename(columns={'AB':'ab'})
df = df.rename(index={'1a':'1A'})
print(df)
