import pandas as pd

datos = pd.read_csv('users.csv', usecols=['nombre', 'edad', 'genero', 'pais', 'email'])
#print(datos)

df = pd.DataFrame(datos)
#print(df)

"""
Como obtener el nombre de los usuarios cuya edad sea mayor a 20
1) df[<condicion>].columna

2) df.loc[df.<condicion>, '<columna>']

"""
#print(df.loc[df.edad > 20, 'nombre'])

"""
Obtener el nombre de los usuario sexo fem edad > 20
"""

#print(df.loc[(df.edad > 20) & (df.genero == 'female'), 'nombre'])

"""
Obtener todos los usuarios cuyos emails terminen en @gmail.com:
"""

#print(df.loc[ df.email.str.endswith('@gmail.com')])

# los q no finalicen en @gmail.com
#print(df.loc[ - df.email.str.endswith('@gmail.com')])

# todos los usuarios de un determinado pais

#print(df.loc[ df.pais.isin(['Germany', 'Finland', 'Canada'])])

"""
Obtener el nombre y mail de todos los usuarios cuyo:
- sexo = fem
- edad > 20
- pais = 'lista de paises'
"""

print(df.loc[ (df.genero == 'Female') & (df.edad > 20) & (df.pais.isin(['Geramany', 'Finland', 'Canada'])), ['nombre', 'email'] ])
# ¡ me da Empty DataFrame != al curso !!!!

# los diez usuarios mas viejos
print(df.sort_values('edad', ascending=False).head(10))