"""
def pares():
    for numero in range(0,100,2):
        print(numero)

print(pares())

# un GENERADOR es una funcion q retorna objetos sin q esta finalice

def pares():
    for numero in range(0,100,2):
        return numero
        # solo mostrará 0 q es la primera iteracion
        # luego del return la funcion finaliza 
        # todo lo q se encuentre despues no se va a ejecutar
        print( 'mensaje q no se verá')
print(pares())

# por eso se usa YIELD en vez de return

def pares(): # Es un GENERADOR -> Lazy iterator
    for numero in range(0,100,2):
        yield numero
        print('se reanuda la ejecucion')

for par in pares():
    print(par)
"""

def pares():
    for numero in range(10):
        yield numero
        print('Reanudo la ejecucion')

generador = pares()

"""
print(next(generador))
print('ejecuto codigo entre llamados')
print(next(generador))
"""

# para manejar el StopIterationError -->

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizó!')    
        break
    