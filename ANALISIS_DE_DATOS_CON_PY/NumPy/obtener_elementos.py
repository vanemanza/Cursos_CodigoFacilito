import numpy as np

lista = [1,2,3,4,5,6]
a = np.array(lista)
print(a)
print(type(a))

print(a[0]) #obtener un elemento x su indice

print(a[a.size -1]) #obtener el ultimo elemento x el size menos 1

#a[100] # da index error

a[1:4] # slice
a[1:5:2] # con skip
a[::-1] # invertir el orden (del ultimo al primero)

# para acceder x los indices->
listab = [0,3,4,5]
print(a[listab])

# realizar operaciones sobre el array
print(a*10)
print(((a*10)-10)/2)