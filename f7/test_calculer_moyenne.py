import unittest
from calculer_moyenne import calculer_moyenne

class TestCalculMoyenne(unittest.TestCase):

    def test_liste_non_vide(self):
        liste = [1, 2, 3, 4, 5]
        resultat_attendu = 3.0
        resultat_obtenu = calculer_moyenne(liste)
        print("Résultat attendu pour une liste non vide :", resultat_attendu)
        print("Résultat obtenu pour une liste non vide :", resultat_obtenu)
        self.assertEqual(resultat_obtenu, resultat_attendu)

    def test_liste_vide(self):
        liste = []
        with self.assertRaises(ValueError):
            calculer_moyenne(liste)

        
        print("Résultat attendu pour une liste vide : ValueError")
        print("Résultat obtenu pour une liste vide : ValueError")

if __name__ == '__main__':
    unittest.main()
