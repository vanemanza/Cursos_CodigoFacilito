# atr iloc

# obtener info del df, pero en vez de trabajar
# con etiquetas, trabaja con posiciones.

df.iloc[0] # para obtener el primer elemento

df.iloc[0:4]

# para trabajar x columnas x posicion
df.iloc[0:4, 0] # para obtener solo el nombre
df.iloc[0:4, [0,2]] # obtengo nombre y calificacion

# 
