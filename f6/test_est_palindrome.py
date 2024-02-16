import unittest
from est_palindrome import est_palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):
        print("Test palindrome simple :")
        print("Résultat attendu pour 'radar' : True")
        print("Résultat obtenu :", est_palindrome("radar"))
        self.assertTrue(est_palindrome("radar"))
        print("Résultat attendu pour 'level' : True")
        print("Résultat obtenu :", est_palindrome("level"))
        self.assertTrue(est_palindrome("level"))



    def test_palindrome_avec_espaces(self):
        print("Test palindrome avec espaces :")
        print("Résultat attendu pour 'a man a plan a canal panama' : True")
        print("Résultat obtenu :", est_palindrome("a man a plan a canal panama"))
        self.assertTrue(est_palindrome("a man a plan a canal panama"))
        print("Résultat attendu pour 'was it a car or a cat I saw' : True")
        print("Résultat obtenu :", est_palindrome("was it a car or a cat I saw"))
        self.assertTrue(est_palindrome("was it a car or a cat I saw"))


    def test_non_palindrome(self):
        print("Test non palindrome :")
        print("Résultat attendu pour 'hello' : False")
        print("Résultat obtenu :", est_palindrome("hello"))
        self.assertFalse(est_palindrome("hello"))
        print("Résultat attendu pour 'world' : False")
        print("Résultat obtenu :", est_palindrome("world"))
        self.assertFalse(est_palindrome("world"))




if __name__ == '__main__':
    unittest.main()
