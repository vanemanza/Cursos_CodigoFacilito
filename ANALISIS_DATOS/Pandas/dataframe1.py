# coding: utf-8
"""
usuarios = {
'nombre' : ['Eduardo', 'Uriel', 'Fernando', 'Jesi'],
'calificaciones': [9,10,8.5,9.5],
'edad' : [27,25,30,22],
'aprobado' : [True, True, False, True]
}
usuarios
import pandas as pd
pd.DataFrame(usuarios)
pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'])
usuarios = {
'nombre' : ['Eduardo', 'Uriel', 'Fernando', 'Jesi'],
'calificacion': [9,10,8.5,9.5],
'edad' : [27,25,30,22],
'aprobado' : [True, True, False, True]
}
usuarios = {
'nombre' : ['Eduardo', 'Uriel', 'Fernando', 'Jesi'],
'calificacion': [9,10,8.5,9.5],
'edad' : [27,25,30,22],
'aprobado' : [True, True, False, True]
}
usuarios
pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'])
a = pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'])
a
a.calificacion
a.calificacion.values
a.nombre
a.columns
a.index
a.values
a.values.ndim
"""
# es como una hoja de excell

# crear --> pd.DataFrame()

usuarios = {
    'nombre': ['Vanesa', 'Reni', 'Fausto', 'Augus'],
    'calificacion': [9,10,8.5,9.5],
    'edad': [46,17,14,11],
    'aprobado': [False, True, True, True],
}
print(usuarios)

import pandas as pd

df = pd.Series(usuarios)
print(df)

df = pd.DataFrame(usuarios)
print(df)

df = pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd'])
print(df)

# puedo acceder a las columnas
# x la llave -> df['nombre']
# x el atributo -> df.calificacion

print(df['nombre'])
print(df.calificacion)

# si quiero obtener los valores -> df.calificacion.values
print(df.calificacion.values)

# ver las columnas --> df.columns
# ver los indices --> df.index
# ver los valores --> df.values

print(df.columns)
print(df.index)
print(df.values)
print(df.values.ndim)
