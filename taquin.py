# Auteurs : Ilyass El Ouazzani (20199147), Pierre-Emmanuel Seguin (20164112)
# Date : 14-03-2022


# Ce programme reproduit le Jeu de taquin : un un jeu graphique qui se joue en
# solitaire sur une grille carrée. Il se joue en déplaçant des carreaux
# numéroté. Il consiste à remettre dans l'ordre les carreaux du jeu à partir
# d'une configuration initiale quelconque.


import random
import math
import tuiles


# La procédure afficherImage() prend comme paramètres une position (x,y),
# un esemble de couleurs et une image et utilise la procédure setPixel()
# pour affiche à la coordonnée (x,y) de la grille de pixels de l'écran
# l'image indiquée en paramètre. 
# x (int) : la position horizontale du premier pixel à afficher
# y (int) : la position vericale du premier pixel à afficher
# colormap (list) : l'ensemble des couleurs a afficher
# image (list) : image définie par les indices des couleurs de colormap
def afficherImage (x, y, colormap, image):
    
    # La taille de l'image en pixels
    size = len(image)
    
    # Verifier que les positions entrées en paramètre sont positives
    x = -x if x < 0 else x      # si x négatif on utilise -x
    y = -y if y < 0 else y      # si y négatif on utilise -y
    
    # Boucle qui parcourt tous les couleurs que contient l'image
    # et les affiches un à un à partir du pixel à la coordonnée (x,y)
    for i in range(size):               # parcourir chaque ligne de l'image
        for j in range(size):           # parcourir chque élément de la ligne
            color = image[i][j]         # stocker la couleur
            
            # Afficher la couleur contenue dans colormap pour chaque pixel
            # de l'image à partir du pixel (x,y) spécifié en paramètre
            setPixel(x + j, y + i, colormap[color])


# La procédure afficherTuile() prend comme paramètres une position (x,y)
# et le numéro d'une tuile et utilise la procédure afficherImage() pour
# afficher à la postion (x,y) de la grille de tuiles l'image de la tuile.
# x (int) : la postion horizontale de la tuile dans la grille de tuiles
# y (int) : la position verticale de la tuile dans la grille de tuiles
# tuile (int) : numero de la tuile à afficher (entre 0 et 15)
def afficherTuile(x, y, tuile):
    
    # la taille de la tuile en pixels
    size = len(tuiles.images)
    
    # Appler la procédure afficherImage pour afficher l'image de la tuile
    # à la position (x,y) multipliée par la taille en pixel.
    afficherImage(x * size, y * size, tuiles.colormap,  tuiles.images[tuile])


# La fonction attendreClick() utilise la fonction getMouse () pour attendre
# que le bouton de souris soit relaché. La fonction retourne un enregistrement
# contenant les champs x et y qui indiquent la coordonnée de la tuile
# sur laquelle le joueur a cliqué.
def attendreClick():
    
    # la taille de la tuile en pixels
    size = len(tuiles.images)
    
    # Boucle qui attend le click du joeusuppérieur à l'index de l'élément actuelk trop souvent
        sleep(0.01)
        
        # lire la position de la souris  
        a = getMouse()
        
        # Si le joueur click sur le bouton de la souris
        if a.button == 1:
            
            # Attendre que le joueur relâche le bouton de la souris
            while a.button != 0:
                a = getMouse()      # lire la position de la souris
            
            # return la position où le joueur a relaché le boutton de la souris
            # la position a est divisé par la taille en pixel des tuiles pour 
            # avoir la position de la tuile et non pas la postition du pixel    
            return(a.x // size, a.y // size)


# La fonction makeTable() prend la longueur d'un tableau en paramètre
# et retourne un tableau de n entiers entre 0 et n-1.
# n (int) : longueur du tableau voulu.
def makeTable(n):
    tab = []                # Créer un tableau vide
    
    # boucle qui ajoute les entiers entre 0 et n-1 au tableau 
    for i in range(n):
        tab.append(i)
    
    # retourner un tableau de n entiers entre 0 et n-1
    return tab


# La fonction permutationAleatoire() prend en paramètre la longueur
# d'un tableau et utilise la fonction makeTable() pour retourner un tableau
# de n entiers en 0 et n-1 dans un ordre aléatoire.
# n (int) : longueur du tableau voulu.
def permutationAleatoire(n):
    
    tab = makeTable(n)  # créer un tableau n entiers entre 0 et n-1
        
    # boucle qui parcourt chaque élément du tableau
    for i in range(n):
        
        temp = tab[i]       # stocker l'élément actuel
        
        # la position aléatoire d'un autre élément du tableau initialisée à -1
        # afin de ne pas choisir le premier élément du tableau
        randomIndex = -1
        
        # Boucle qui attend un index suppérieur à celui de l'élément actuel
        while randomIndex < i:
            
            # trouver index aléatoire entre 0 et n-1
            randomIndex = math.floor(random.random() * n)
        
        # remplacer l'élément actuel par l'élément à l'index aléatoire
        tab[i] = tab[randomIndex]
        
        # remplacer l'élément à l'index aléatoire par l'élément actuel       
        tab[randomIndex] = temp
    
    # retourner le tableau mélangé
    return tab


# La fonction inversions() prend comme paramètres un tableau d'entiers
# et une valeur x et retourne le nombre d'éléments dans le tableau qui sont
# après x et inférieurs à x. Cela indique indique à quel point la valeur x 
# n'est pas bien ordonnée dans le tableau tab.
# tab (list) : tableau d'entiers
# x (int) : valeur a évaluer
def inversions(tab, x):
    
    # index auquel on commence a évaluer l'ordre
    index = tab.index(x) + 1    # index de la valeur suivant x dans tab
    
    # compteur d'éléments inférieurs à x
    counter = 0
    
    # parcourir chaque élément qui suit la valeur x
    for i in range(index, len(tab)):
        
        # verifier si l'élément est inférieur à x et qu'il n'est pas l'élément 0
        if tab[i] < x and tab[i] != 0:
            counter += 1    # si c'est le cas incrementer le compteur de 1
    
    # retourner le nombre d'éléments après x inférieurs à x   
    return counter


# La fonction findR() prend un tableau d'entiers en paramètre et retourne
# la rangée de l'élément 0 (la case vide) dans le jeu
# tab (list) : tableau d'entiers
def findR(tab):
    
    # nombre de rangées dans le jeu
    nbRows = int(math.sqrt(len(tab)))
    
    # retourner la rangée de la case vide
    return math.ceil((tab.index(0) + 1) / nbRows)


# La fonction soluble() prend un tableau d'entiers en paramètre vérifie si la
# combinaison d'entiers est soluble pour le jeu de Taquin
# tab (list) : tableau d'entiers
def soluble(tab):
    
    # si le tableau de longueur pair et n'est pas vide
    if not len(tab) % 2 and len(tab) != 0:
        total = findR(tab)      # initialise compteur à la rangée de r
        
    # si le tableau de longueur impair 
    else:
        total = 0               # initialise compteur à 0
    
    # parcourir toutes les valeurs entre 1 et len(tableau) - 1
    for i in range(1, len(tab)):
        
        # incrémenter total par le nombre d'éléments suivants la valeur
        # et inférieurs à la valeur de l'itération actuelle
        total += inversions(tab, i)
    
    # Si total pair, la combinaison est soluble pour le jeu, retourne True
    # Si total impair, combinaison non soluble pour le jeu, retourne False
    return not total % 2


def initial(largeur):
    
    valid = False
    
    while not valid:
        c = permutationAleatoire(largeur*largeur)
        valid = soluble(c)
        
    return c


def renderGrid(largeur, grid):
    for i in range(len(grid)):
        afficherTuile(i % largeur, i // largeur, grid[i])

        
def tileIndex(tile, largeur):
    return largeur*tile[1] + tile[0]


def tileBorders(tile, largeur):
    border = struct(left = tile[0] == 0, right = tile[0] == largeur -1, 
                       up = tile[1] == 0, down = tile[1] == largeur - 1)
    
    return border


def tileOffsets(borders):
    offsets = struct(left = 0 if borders.left else 1,
                     right = 0 if borders.right else 1,
                     up = 0 if borders.up else 1,
                     down = 0 if borders.down else 1)
    
    return offsets


def canMove(tile, largeur, grid):
    
    borders = tileBorders(tile, largeur)
    offsets = tileOffsets(borders)
    
    xStart = tile[0] - offsets.left
    xStop = tile[0] + offsets.right + 1
    
    yStart = tile[1] - offsets.up
    yStop = tile[1] + offsets.down + 1
    
    for x in range(xStart, xStop):
        neighbourIndex = tileIndex((x, tile[1]), largeur)
        if grid[neighbourIndex] == 0:
            return neighbourIndex
        
    for y in range(yStart, yStop):
        neighbourIndex = tileIndex((tile[0], y), largeur)
        if grid[neighbourIndex] == 0:
            return neighbourIndex
    
    return -1


def makeSolution(largeur):
    
    solution = makeTable(largeur*largeur)
    solution.remove(0)
    solution.append(0)
    
    return solution


def moveTile(indexR, clickedIndex, grid, largeur):
    
    temp = grid[indexR]
    grid[indexR] = grid[clickedIndex]
    grid[clickedIndex] = temp
    
    renderGrid(largeur, grid)

        
def taquin(largeur):
    
    screenSize = 16 * largeur
    
    setScreenMode(screenSize, screenSize)
    
    while True:
                
        grid = initial(largeur)
        
        renderGrid(largeur, grid)
        
        solution = makeSolution(largeur)

        solved = False

        while not solved:

            clickedTile = attendreClick()

            indexClicked = tileIndex(clickedTile, largeur)

            indexR = canMove(clickedTile, largeur, grid)
            
            if indexR >= 0:
                moveTile(indexR, indexClicked, grid, largeur)
            
            solved = grid == solution
        
        else:
            alert('FÉLICITATION!')


def testTaquin():
    
    
    assert permutationAleatoire(0) == []
    assert permutationAleatoire(-1)== []
    assert permutationAleatoire(1) == [0]
    assert permutationAleatoire(2) == [0, 1] or [1, 0]
    
    assert inversions([0,2,9,1,4,3],2)== 1
    assert inversions([0,9,8,2,4,3],8)== 3
    assert inversions([0,0,0,0,0],0)== 0 
    assert inversions([1,2,3,4,5],1)== 0 
    assert inversions([1,8,5,4,2,6],6)== 0 
    
    assert soluble([3,5,6,7,10,14,11,9,4,13,2,0,8,1,12,15])== True
    assert soluble([3,5,6,7,10,14,15,9,4,13,2,0,8,1,12,11])== False
    assert soluble([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])== False
    assert soluble([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0])== False
    assert soluble([14,15,9,12,11,10,13,2,7,6,5,4,3,8,1,0])== True
    
    assert initial(1)== [0]
    assert initial(0)== [] 
    assert len(initial(2))== 4
    assert len(initial(3))== 9 
    assert len(initial(4))== 16
    
    
    setScreenMode(16, 16)    

    afficherImage(0, 0, tuiles.colormap, tuiles.images[10])
    
    r = """
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888
"""
    
    assert exportScreen() == r.strip()
    
    
    afficherImage(0, 0, tuiles.colormap, tuiles.images[0])
    
    r = """
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
"""
    
    assert exportScreen() == r.strip()
    
    
    afficherImage(0, 0, tuiles.colormap, tuiles.images[-1])
    
    r = """
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888
"""
    
    assert exportScreen() == r.strip()
    
    
    setScreenMode(18, 18)
    
    
    afficherImage(-1, -1, tuiles.colormap, tuiles.images[-1])
    
    r = """
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#000
#000#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888#000
#000#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888#000
#000#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888#000
#000#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888#000
#000#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#000
#000#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
"""
    
    assert exportScreen() == r.strip()
    
    
    setScreenMode(18, 18)
    
    
    afficherImage(2, 2, tuiles.colormap, tuiles.images[4])
    
    r = """
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc
#000#000#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888
#000#000#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#000#000#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#000#000#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888
#000#000#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888
"""
    
    assert exportScreen() == r.strip()
    
    
    setScreenMode(16, 32)
    
    afficherTuile(0, 0, 0)
    
    r = """
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
"""
    
    assert exportScreen() == r.strip()
    
    
    afficherTuile(0, 0, 10)
    
    r = """
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
"""
    
    assert exportScreen() == r.strip()
    
    
    afficherTuile(0, 0, -1)
    
    r = """
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
"""
    
    assert exportScreen() == r.strip()
    
    
    setScreenMode(16, 32)
    
    
    afficherTuile(0, -1, -1)
    
    r = """
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888
"""
    
    assert exportScreen() == r.strip()
    
    
    afficherTuile(0, -1, 4)
    
    r = """
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888
"""
    
    assert exportScreen() == r.strip()
