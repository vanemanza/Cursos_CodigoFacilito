import numpy as np

lista = [10,20,30,40,50,60]

# crear arreglos

a = np.array(lista)
lista = [1,2,3,45,6]

a = np.array(lista)

# son mas rapidos y compactos q las listas
# nos permiten hacer operaciones sin iterar

a.ndim # nos da la dimension del array
a.size # cuantos elementos posee
a.itemsize #elementos en bites
a.shape #forma del arreglo