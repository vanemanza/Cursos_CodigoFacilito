#print('str', 10, 14.5, True) # recibe una n cantidad de argumentos

# funciones q reciben n cantidad de argumentos
"""
def promedio(listado):
    return sum(listado)/len(listado)

resultado = promedio([10,10,5,7,10])
print(resultado)
"""

def promedio(*args): # x convension se denomina args a los argumentos con *
    return sum(args)/len(args)

resultado = promedio(10,10,5,7,10) #ya no le paso una lista y se almacenan en una tupla
print(resultado)

# * crea una Tupla
def convinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

convinacion(1,2,3,4,5,6,7,8, p4=1000)    

# doble ** crea diccionarios
def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10,10,8], fernando=[10,9,8])  

def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1,2,3,4,5, cody=True, curso='Python')    

# a la izq los obligatorios, a la derecha los opcionales
def combinacion(p1, p2, *args, **kwargs, p4=100): 
    print(args)
    print(kwargs)