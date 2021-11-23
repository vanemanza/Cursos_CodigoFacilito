#class <CamelCase>
# x convencion se escribe en singular
"""
class Usuario: 
    #no le pondré atributos ni metodos
    #en python no se pueden dejar bloques vacios
    # en tal caso uso la palabra reservada pass
    pass

# instanciar un objeto de esa clase -->
cody = Usuario()
print(cody)

#-----------------------------------------------------

#Attrs de clase:
# le pertenecen a una clase
#Attrs de instancia:
# le pertenecen a un objeto

class Usuario:
    username = 'default' # atributos de clase
    email = '' # atributos de clase

Usuario.username = 'Usuario_uno'
Usuario.email = 'mail@mail.com'    

print(Usuario.username)    

user1 = Usuario()
user2 = Usuario()
print(user1.username)
print(user1.__dict__) # Dict

user1.username = 'Vanesa'
print(user1.username)
print(user1.__dict__)

user1.password = '1234'
print(user1.__dict__)
user1.password = 'miclave'
print(user1.__dict__)

print(user2.password) # podemos añadir atr a los objetos en tiempo de ejecucion
"""

# debemos estandarizar los atributos para nuestros objetos
"""
class Usuario:

    def inicializar(self, username, password): #self hace referencia al objeto por si mismo
        # añadiendo attrs al objeto
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()

print(user1.__dict__)
print(user2.__dict__)

user1.inicializar('User1', 'Pass1')
user2.inicializar('User2', 'Pass2')

print(user1.__dict__)
print(user2.__dict__)
"""

class Usuario:
    # Object
    # el metodo init se llama cuando el objeto es instanciado
    def __init__(self, username='', password=''): # puedo usar parametros x default
        self.username = username
        self.password = password

user1 = Usuario('usuario1', 'password1')        
user2 = Usuario('usuario2', 'password2')        
user3 = Usuario('usuario3', 'password3')       
user4 = Usuario()       
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
#print(user4.__dict__)