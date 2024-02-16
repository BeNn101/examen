

def compter_mots(phrase):
    # phrase vide
    if not phrase:
        return 0
    
    
    mots = phrase.strip().split()
    
    #  nombre de mots
    return len(mots)
