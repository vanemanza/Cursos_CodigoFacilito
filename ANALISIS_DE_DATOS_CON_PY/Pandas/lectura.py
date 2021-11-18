import pandas as pd
import os
"""
usuarios = pd.read_csv('users.csv')

#for f in os.listdir("ANALISIS_DE_DATOS_CON_PY/Pandas"):
 #   	print(f)

#print(usuarios)

# metodo head() para acceder a los primeros 5 registros x default
# puedo decirles cuantos registros quiero ver

print(usuarios.head(12))

# metodo tail() los ultimos 5
print(usuarios.tail(7))

# metodo delimiter para indicar el caracter q separa la informacion
#usuarios = pd.read_csv('users.csv', delimiter=',')

# metodo header() indico a partir de q registro quiero q comience la lectura
usuarios = pd.read_csv('users.csv', delimiter=',', header=5)
print(usuarios)
"""
paises = pd.read_csv('paises.csv', usecols=['pais', 'poblacion', 'long', 'lat'])

#print(paises)

# remplazar los N/S x NaN

paises = pd.read_csv('paises.csv', usecols=['pais', 'poblacion', 'long', 'lat'], na_values='N/S')
print(paises)

print(type(paises[paises.poblacion.notnull()]))

"""
Podemos ver q los datos de poblacion son de tipo objects,
pero podemos pasarlos a int usando una funcion lambda.
Para verificar el tipo de dato, ejecuto--> 

paises.poblacion.values

print(paises.apply(lambda row: row['poblacion'] ,axis=1))
"""
# obtengo todos los paises con poblacion
paisesdf = paises[ paises.poblacion.notnull]

# ahora vamos a convertir los str a enteros

paises = paisesdf.apply( lambda row : int(str(row['poblacion']).replace('.', '')), axis=1)
print(paises)