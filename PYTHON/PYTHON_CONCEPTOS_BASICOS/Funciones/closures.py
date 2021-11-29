"""
e = 'e' # variable global

def funcion_principal():
    a = 'a' #variable local con scope superior, puede ser utilizada en bloques inferiores
    b = 'b'

    def funcion_anidada():
        c = 'c' # variable local
        nonlocal b
        b = 'otro valor'
        print(a)
        print(b)
        print(id(b))
        print(e)

    funcion_anidada()
    #print(c)
    print(b)
    print(id(b))

funcion_principal()        
"""
"""
def saludar():

    def mostrar_mensaje():
        print('hola mensaje')

    return mostrar_mensaje

respuesta = saludar()

respuesta()  
"""
# Closures: una funcion q puede generar de forma dinamica a otra funcion
# y esta funcion puede acceder a las variables locales cuando esta haya finalizado.

def saludar(username):
    mensaje = f'Hola {username}' # variable local
    
    def mostrar_mensaje(): # funcion anidada
        print(mensaje)

    return mostrar_mensaje

username = 'cody'
respuesta = saludar(username)    
respuesta()  