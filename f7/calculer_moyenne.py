def calculer_moyenne(liste):
    if not liste:
        raise ValueError("La liste ne peut pas être vide")
    return sum(liste) / len(liste)
