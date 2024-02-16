import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_calculer_perimetre(self):
        rectangle = Rectangle(5, 10)
        perimetre_attendu = 2 * (5 + 10)
        perimetre_obtenu = rectangle.calculer_perimetre()
        print("Périmètre attendu :", perimetre_attendu)
        print("Périmètre obtenu :", perimetre_obtenu)
        self.assertEqual(perimetre_obtenu, perimetre_attendu)

    def test_calculer_surface(self):
        rectangle = Rectangle(5, 10)
        surface_attendue = 5 * 10
        surface_obtenue = rectangle.calculer_surface()
        print("Surface attendue :", surface_attendue)
        print("Surface obtenue :", surface_obtenue)
        self.assertEqual(surface_obtenue, surface_attendue)

if __name__ == '__main__':
    unittest.main()
