diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

print('z' in diccionario)

"""
valor = diccionario['d']
print(valor)
"""

# metodo get
valor = diccionario.get('p', 'mensaje de ayuda') # en caso de q la llave no exista
print(valor)

#metodo setdefault
#para obtener la llave y un default x si la llave no existe
valor = diccionario.setdefault('e', 5)
print(valor)
print(diccionario)

