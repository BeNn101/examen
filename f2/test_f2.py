import unittest
from compter_mots import compter_mots

class TestCompterMots(unittest.TestCase):

    def test_phrase_vide(self):
        print("Test phrase vide : ")
        print("Résultat attendu : 0")
        resultat = compter_mots('')
        print("Résultat obtenu :", resultat)
        self.assertEqual(resultat, 0)

    def test_une_seule_mot(self):
        print("Test une seule mot : ")
        print("Résultat attendu : 1")
        resultat = compter_mots('Bonjour')
        print("Résultat obtenu :", resultat)
        self.assertEqual(resultat, 1)

    def test_espaces_supplementaires(self):
        print("Test espaces supplémentaires : ")
        print("Résultat attendu : 3")
        resultat = compter_mots('   Bonjour    le   monde   ')
        print("Résultat obtenu :", resultat)
        self.assertEqual(resultat, 3)

    def test_mots_multiples(self):
        print("Test mots multiples : ")
        print("Résultat attendu : 4")
        resultat = compter_mots('Il fait beau aujourd\'hui')
        print("Résultat obtenu :", resultat)
        self.assertEqual(resultat, 4)

if __name__ == '__main__':
    unittest.main()
