""""
Atributo loc
Permite tener info de los df a partir de etiquetas
"""

import pandas as pd
import numpy as np

usuarios = {
    'nombre':['vane', 'reni', 'faus', 'augus', 'sugi'],
    'edad': np.random.randint(11,46,5),
    'calificacion': np.random.randint(5,10,5), 
    'email': ['vane@mail.com', 'reni@mail.com', 'faus@mail.com', 'augus@mail.com', 'sugi@mail.com']   
}

df = pd.DataFrame(usuarios, index=list('abcde'))

print(df)

# para obtener una serie con los datos de una columna --> df['key']
print(df['edad'])

# para obtener informacion a partir de un indice uso el atr loc:
print(df.loc['a'])

# tambien puedo obtener un rango a partir de indices:
# df.loc['a':'c']

# tambien puedo seleccionar una columna en particular
print(df.loc['a':'c', ['nombre', 'edad']])

# con log puedo realizar consultas:
# df.loc[df.calificacion > 5]
# df.loc[df.calificacion > 5, 'nombre']
# df.loc[df.calificacion > 5, ['nombre', 'edad']]
# para obtener los 3 estudiantes con calificacion más alta:

print(df.loc[ df.calificacion > 5, ['nombre', 'calificacion']].sort_values('calificacion', ascending=False).head(3))