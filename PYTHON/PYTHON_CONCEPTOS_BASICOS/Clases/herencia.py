"""
class Mascota: # Clase Padre
    
    def comer(self):
        print('La mascota come.')

    def dormir(self):
        print('La mascota duerme.')

class Perro(Mascota): # Clase Hija
    pass

class Gato(Mascota):
    pass

Duke = Perro()
patricio = Gato()

Duke.comer()
Duke.dormir()
patricio.comer()
patricio.dormir()

"""

# Herencia Múltiple

"""
class Animal():
    def comer(self):
        print('el animal come')

    def dormir(self):
        print('el animal duermeee')


class Mascota(Animal):
    pass    

class Felino:

    def cazar(self):
        print('cazaaa')

class Gato(Mascota, Felino):
    pass

patricio = Gato()

patricio.comer()
patricio.dormir()
patricio.cazar()
"""

# sobrecarga de metodos o sobreescritura
# una clase hija puede cambiar el comportamiento de los metodos de la clase padre
"""
class SerVivo:

    def dormir(self):
        print('El ser duerme.')

class Animal(SerVivo):
    # mientras mas nivel jerarquico es mas abstracta sera la clase
    def comer(self):
        print('el animal come')

class Mascota(Animal):

    def comer(self):
        print('La mascota ahora come')   

class Felino:

    def cazar(self):
        print('cazaaa')

class Gato(Mascota, Felino):
    # mientras menos nivel jerarquico  mas concreta sera la clase
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f'{self.nombre} come.')    
   
patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()
"""

# deseo ejecutar el metodo comer de la clase padre y no de la hija
# uso la funcion super y accedo al padre inmediato

class SerVivo:
    
    def dormir(self):
        print('El ser duerme.')

class Animal(SerVivo):
    # mientras mas nivel jerarquico es mas abstracta sera la clase
    def comer(self):
        print('el animal come')

class Mascota(Animal):

    def comer(self):
        super().comer()
        print('La mascota ahora come')   

class Felino:

    def cazar(self):
        print('cazaaa')

class Gato(Mascota, Felino):
    # mientras menos nivel jerarquico  mas concreta sera la clase
    
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'{self.nombre} come.')    
   
patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()



