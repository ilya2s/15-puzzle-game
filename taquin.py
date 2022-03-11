import random
import math
import tuiles



def afficherImage (x, y, colormap, image):
    size = len(tuiles.images)
    
    for i in range(size):
        for j in range(size):
            color = image[i][j]
            setPixel(x + j, y + i, colormap[color])


def afficherTuile(x, y, tuile):
    size = len(tuiles.images)
    afficherImage(x * size, y * size, tuiles.colormap,  tuiles.images[tuile])


def attendreClick():
    
    size = len(tuiles.images)
        
    while True:
        
        sleep(0.01)
        a = getMouse()
        
        if a.button == 1:
            
            while a.button != 0:
                a = getMouse()
                
            return(a.x // size, a.y // size)


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
    
    if not len(tab) % 2:
        total = findR(tab)
    else:
        total = 0  
    
    for i in range(1, len(tab)):
        total += inversions(tab, i)
    
    return not total % 2


def initial(largeur):
    
    valid = False
    
    while not valid:
        c = permutationAleatoire(largeur*largeur)
        valid = soluble(c)
        
    return c
