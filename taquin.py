import random
import math

def permutationAleatoire(n):
    return random.sample(range(n), n)


def inversions(tab, x):
    
    index = tab.index(x) + 1
    
    counter = 0
    
    for i in range(index, len(tab)):
        
        if tab[i] < x and tab[i] != 0:
            counter += 1
            
    return counter


def findR(tab):
    
    nbRows = int(math.sqrt(len(tab)))
    
    return math.ceil((tab.index(0) + 1) / nbRows)


def soluble(tab):
    
    total = findR(tab)
    
    for i in range(1, len(tab)):
        total += inversions(tab, i)
    
    return not total % 2


def initial(largeur):
    
    valid = False
    
    while not valid:
        c = permutationAleatoire(largeur*largeur)
        valid = soluble(c)
        
    return c


jeuBase = [3,5,6,7,10,14,11,9,4,13,2,0,8,1,12,15]
jeu = initial(4)

print(jeu)

print(soluble(jeu))   

