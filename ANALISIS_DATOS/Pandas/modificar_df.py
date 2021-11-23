import pandas as pd
import numpy as np

df = pd.DataFrame( np.arange(16).reshape(4,4), columns=list('ABCD'), index=list('abcd'))

print(df)

# si quiero modificar un elemento x ej el 5 x 50
# primero ingreso a la columna 
"""
1) df['B']
2) df.B['b]
    df.B[1]
    
"""
df.B['b'] = 50 # le asigno el nuevo valor

#print(df)

# si queremos modificar la columna completa -->

df.B = 10,20,30,40

# print(df)

# si queremos eliminar una columna --> metodo drop() axis = 1

df.drop('D', axis=1)

print(df)

# si queremos eliminar una fila --> metodo drop() axis= 0

print(df.drop('b', axis=0))

# insertar una nueva columna --> metodo insert(<posicion>, <nombre de col>, [valores])
# si modifica al df

df.insert(1, 'Z', [100,200,300,400])

# otra forma con metodo asign(<nombre>=100,200,300,400)
# asign no modifica al df

print(df)