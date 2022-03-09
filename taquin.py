import random
import math
import tuiles


def afficherImage (x, y, colormap, image):
    rangee = image
    for i in range(len(tuiles.images)):
        for j in range (len(rangee)):
            c=rangee[i][j]
            setPixel((x+j),(y+i), tuiles.colormap[c])


def afficherTuile(x, y, tuile):
    taille = len(tuiles.images)
    afficherImage(x*taille, y*taille, tuiles.colormap, tuiles.images[tuile])


def makeTable(n):
    tab = []
    for i in range(n):
        tab.append(i)
    
    return tab


def permutationAleatoire(n):
    
    tab = makeTable(n)
        
    for i in range(n):
        
        temp = tab[i]
        
        randomIndex = -1
        
        while randomIndex < i:
            randomIndex = math.floor(random.random() * n)
        
        tab[i] = tab[randomIndex]
        tab[randomIndex] = temp
    
    return tab


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
