import pandas as pd
import numpy as np

frutas = {
    'nombre':['Naranja', 'Manzana', 'Manzana', 'Pera', 'Naranja', 'Manzana', 'Sandia'],
    'color': ['Naranja', 'Rojo', 'Verde', 'Verde', 'Naranja', 'Rojo', 'Rojo'],
    'cantidad': np.random.randint(5,10,7),
    'precio':  np.random.randint(1,5,7),
}

df = pd.DataFrame(frutas)
#print(df)

# metodo groupby()
df.groupby('nombre') # obtengo un objeto del tipo dataframe groupby

# a partir de este objeto podemos usar distinto metodos de agregacion

df.groupby('nombre').cantidad.sum()

df.groupby('nombre').cantidad.sum().to_frame('cantidad') # obtenemos un nuevo df y recibe como argumento el nombre de la columna q queremos crear
# las llaves con las q agrupamos seran los indices del nuevo df

# al agrupar podemos realizar filtros con esos agrupamientos

df.groupby('nombre') # agrupamos x nombre

df.groupby('nombre').filter( lambda fruta: fruta.cantidad.sum() > 10) # el metodo filter recibe una funcion

# obtenemos un nuevo df con los registros separados y los podemos volver a agrupar con groupby
df.groupby('nombre').filter( lambda fruta: fruta.cantidad.sum() > 10).groupby('nombre').cantidad.sum()

# agrupar las manzanas x su color
print(df[ df.nombre == 'Manzana'].groupby('color').cantidad.sum())
