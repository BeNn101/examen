def est_palindrome(chaine):
    
    chaine = chaine.replace(" ", "").lower()
    chaine_inverse = chaine[::-1]
    return chaine == chaine_inverse
