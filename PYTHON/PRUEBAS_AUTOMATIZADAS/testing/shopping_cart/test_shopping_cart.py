import unittest
from shopping_cart import Item

"""
las pruebas tienen q estar en una clase, que herede de 
unittest.TestCase

y las pruebas unitarias serán métodos, y deben comenzar 
con la palabra test
"""

class TestShoppingCart(unittest.TestCase):

    def test_cinco_mas_cinco_diez(self):
        assert 5 + 5 == 10 

    def test_nombre_igual_manzana(self):
        item =  Item("Manzana", 12.0)
        self.assertEqual(item.name, "Manzana")  

    def test_nombre_diferente_manzana(self):
        item =  Item("Pan blanco", 12.0)
        self.assertNotEqual(item.name, "Manzana")  
    

if __name__ == '__main__':
    unittest.main() # con esta linea se ejecutan todas las pruebas unitarias   