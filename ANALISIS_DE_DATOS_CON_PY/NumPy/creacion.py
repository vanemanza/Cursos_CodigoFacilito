import numpy as np
# array
np.array([1,2,3])

# arange: crea un array a partir de un rango
# recibe dos argumentos: inicio, fin (el ultimo no se cuenta)
# puede recibir un tercer argumento skip
np.arange(0, 9, 2)


# zeros()
# recibe la longitud  y e l tipo de dato
np.zeros(10, dtype=np.integer)

# ones()
np.ones(10)

# full()
# el primer argumento cantidad de elem y el seg los elementos del arreglo
np.full(10, 5)

# random
np.random.random(15)
np.random.random(15)*10

#randint
#los dos primeros definen el rango y el tercero la cantidad de elementos
np.random.randint(0, 25, 10)

# linspace
# dos primeros argumentos definen el rango, el tercero la cantidad de elem del array
np.linspace(0,10,10)

