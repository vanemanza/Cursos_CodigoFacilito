diccionario = {'a':1, 'b':2, 'c':3, 'd':4}
print(len(diccionario))
del diccionario['a'] #1
valor = diccionario.pop('b')

diccionario.clear() #~elimina todos los elementos y obtengo un dicc vacio
print(diccionario)

print(len(diccionario))