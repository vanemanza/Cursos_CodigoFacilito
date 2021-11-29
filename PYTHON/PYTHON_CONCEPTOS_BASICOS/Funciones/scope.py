animal = 'Leon' #variable global -> funcion, condicion, ciclo

def imprimir_animal():
    #animal = 'Ballena' # variable local -> solo puede ser usada dentro del bloque donde fue creada
    tipo = 'mamifero' # cuando el bloque finaliza la variable local es destruida
    global animal
    animal = 'Ballena'
    print(id(animal))

imprimir_animal()    
print(id(animal))
#print(tipo) #NameError
# podemos imprimir el id del objeto para identificarlos