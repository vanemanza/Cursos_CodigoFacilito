# Metodos de clase
"""
class Circulo:

    pi = 3.141592

    def area(cls, radio): # continua siendo un metodo de instancia
        return cls.pi * (radio ** 2)
"""

class Circulo:
    
    pi = 3.141592

    @classmethod
    def area(cls, radio): # continua siendo un metodo de instancia
        return cls.pi * (radio ** 2)

resultado = Circulo.area(14)
print(resultado)