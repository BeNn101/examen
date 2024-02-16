import unittest
from somme_liste import somme_liste

class TestSommeListe(unittest.TestCase):

    def test_liste_vide(self):
        liste = []
        resultat_attendu = 0
        resultat_obtenu = somme_liste(liste)
        print("Résultat attendu pour une liste vide :", resultat_attendu)
        print("Résultat obtenu pour une liste vide :", resultat_obtenu)
        self.assertEqual(resultat_obtenu, resultat_attendu)

    def test_liste_positifs(self):
        liste = [1, 2, 3, 4, 5]
        resultat_attendu = 15
        resultat_obtenu = somme_liste(liste)
        print("Résultat attendu pour une liste de positifs :", resultat_attendu)
        print("Résultat obtenu pour une liste de positifs :", resultat_obtenu)
        self.assertEqual(resultat_obtenu, resultat_attendu)

    def test_liste_negatifs(self):
        liste = [-1, -2, -3, -4, -5]
        resultat_attendu = -15
        resultat_obtenu = somme_liste(liste)
        print("Résultat attendu pour une liste de négatifs :", resultat_attendu)
        print("Résultat obtenu pour une liste de négatifs :", resultat_obtenu)
        self.assertEqual(resultat_obtenu, resultat_attendu)


if __name__ == '__main__':
    unittest.main()
