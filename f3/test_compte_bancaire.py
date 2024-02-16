import unittest
from compte_bancaire import CompteBancaire

class TestCompteBancaire(unittest.TestCase):

    def test_deposer(self):
        compte = CompteBancaire(100)
        compte.deposer(50)
        solde_attendu = 150
        solde_obtenu = compte.obtenir_solde()
        print(f"Solde attendu après dépôt : {solde_attendu}")
        print(f"Solde obtenu après dépôt : {solde_obtenu}")
        self.assertEqual(solde_obtenu, solde_attendu)

    def test_retirer(self):
        compte = CompteBancaire(100)
        compte.retirer(50)
        solde_attendu = 50
        solde_obtenu = compte.obtenir_solde()
        print(f"Solde attendu après retrait : {solde_attendu}")
        print(f"Solde obtenu après retrait : {solde_obtenu}")
        self.assertEqual(solde_obtenu, solde_attendu)

    def test_obtenir_solde(self):
        solde_attendu = 100
        compte = CompteBancaire(solde_attendu)
        solde_obtenu = compte.obtenir_solde()
        print(f"Solde attendu : {solde_attendu}")
        print(f"Solde obtenu : {solde_obtenu}")
        self.assertEqual(solde_obtenu, solde_attendu)

if __name__ == '__main__':
    unittest.main()
