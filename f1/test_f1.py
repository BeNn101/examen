import unittest
from f1 import nb_premier

class TestNbPremier(unittest.TestCase):

    def test_nombres_negatifs(self):
        print("Résultat test nombres négatifs : ", nb_premier(-1))
        print("Résultat test nombres négatifs : ", nb_premier(-10))
        print("Résultat test nombres négatifs : ", nb_premier(-100))
        self.assertFalse(nb_premier(-1))
        self.assertFalse(nb_premier(-10))
        self.assertFalse(nb_premier(-100))

    def test_zero_et_un(self):
        print("Résultat test zéro et un : ", nb_premier(0))
        print("Résultat test zéro et un : ", nb_premier(1))
        self.assertFalse(nb_premier(0))
        self.assertFalse(nb_premier(1))

    def test_nombres_premiers(self):
        print("Résultat test nombres premiers : ", nb_premier(2))
        print("Résultat test nombres premiers : ", nb_premier(3))
        print("Résultat test nombres premiers : ", nb_premier(5))
        print("Résultat test nombres premiers : ", nb_premier(7))
        print("Résultat test nombres premiers : ", nb_premier(11))
        self.assertTrue(nb_premier(2))
        self.assertTrue(nb_premier(3))
        self.assertTrue(nb_premier(5))
        self.assertTrue(nb_premier(7))
        self.assertTrue(nb_premier(11))

    def test_nombres_non_premiers(self):
        print("Résultat test nombres non premiers : ", nb_premier(4))
        print("Résultat test nombres non premiers : ", nb_premier(6))
        print("Résultat test nombres non premiers : ", nb_premier(8))
        print("Résultat test nombres non premiers : ", nb_premier(9))
        print("Résultat test nombres non premiers : ", nb_premier(10))
        print("Résultat test nombres non premiers : ", nb_premier(12))
        self.assertFalse(nb_premier(4))
        self.assertFalse(nb_premier(6))
        self.assertFalse(nb_premier(8))
        self.assertFalse(nb_premier(9))
        self.assertFalse(nb_premier(10))
        self.assertFalse(nb_premier(12))

    def test_grands_nombres_premiers(self):
        print("Résultat test grands nombres premiers : ", nb_premier(7919))
        self.assertTrue(nb_premier(7919)) 

    def test_grands_nombres_non_premiers(self):
        print("Résultat test grands nombres non premiers : ", nb_premier(10000))
        self.assertFalse(nb_premier(10000))  

if __name__ == '__main__':
    unittest.main()
