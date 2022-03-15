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


# La fonction initial() prend une largeur en paramètre et utilise
# les fonctions permutationAleatoire() et soluble() pour retourner un tableau
# de longueur largeur*largeur contenant les entiers de 0 à largeur*largeur - 1
# qui correspond à une configuration de tuile qui est soluble.
# largeur (int) : nombre de rangées et de colonnes du jeu de Taquin.
def initial(largeur):
    
    # variable pour valider si la configuration du tableau est soluble
    valid = False
    
    # boucle qui attends une configuration soluble
    while not valid:
        
        # créer un tableau d'entiers dans un ordre aléatoire
        c = permutationAleatoire(largeur*largeur)
        
        # valider si la configuration du tableau est soluble pour le jeu
        valid = soluble(c)
        
    return c        # retourner le tableau ayant une configuration soluble


# La procédure renderGrid() prend une largeur et tableau d'entiers comme
# paramètres et utilise la procédure afficherTuile() pour afficher chaque
# à l'écran la tuile correspendante à chaque entier du tableau.
# largeur (int) : nombre de rangées et de colonnes du jeu
# grid (list) : liste d'entiers représentant les tuiles du jeu
def renderGrid(largeur, grid):
    
    # boucle qui va afficher chaque tuile du tableau à la bonne postion dans la
    # grille de tuiles de l'écran
    for i in range(len(grid)):
        
        # (i % largeur) nous donne la position x de la tuile selon l'index de 
        # l'entier dans le tableau et (i // largeur) nous donne la position y 
        # de la tuile selon l'index de l'entier dans le tableau 
        afficherTuile(i % largeur, i // largeur, grid[i])


# La fonction tileIndex() prend la position d'une tuile et la largeur du jeu
# comme paramètres et retourne l'index de cette tuile dans le tableau d'entiers
# contenant la configuration du jeu.
# tile (Tuple) : contient position (x, y) de la tuile dans la gille de tuiles
# largeur (int) : nombre de rangées et de colonnes du jeu   
def tileIndex(tile, largeur):
    
    # nombre de rangées * position en y + position en x nous donne l'indice de
    # la tuile dans le tableau contenant la configuration du jeu.
    return largeur*tile[1] + tile[0]        # retourner l'indice de la tuile


# La fonction tileBorders() prend la position d'une tuile et la largeur du jeu
# comme paramètres et retourne une structure qui indique si cette tuile est en
# bordure du jeu par la gauche, la droite, le haut ou le bas.
# tile (Tuple) : contient position (x, y) de la tuile dans la gille de tuiles
# largeur (int) : nombre de rangées et de colonnes du jeu   
def tileBorders(tile, largeur):
    
    # la tuile sera en bordure du jeu si sa position en x == 0
    # ou si sa position en y == largeur - 1
    border = struct(left = tile[0] == 0,            # verifier bordure à gauche
                    right = tile[0] == largeur -1,  # verifier bordure à droite
                    up = tile[1] == 0,              # verifier borduire en haut
                    down = tile[1] == largeur - 1)  # verifier bordure en bas
    
    # retourner la structure indiquant les bordures de la tuile
    return border


# La fonction tileOffsets() prend en paramètre les bordures d'une tuile dans
# le jeu et retourne une structure qui indique si on doit on explorer le
# voisinage de cette tuile vers la gauche, la droite, le haut et le bas.
# borders (struct) : structure indiquant les bordures de la tuile dans le jeu
def tileOffsets(borders):
    
    # on explore 1 tuile voisine si la tuile actuelle n'est pas en bordure
    # du jeu sinon on n'explore pas dans cette direction.
    offsets = struct(left = 0 if borders.left else 1,       # vers la gauche
                     right = 0 if borders.right else 1,     # vers la droite
                     up = 0 if borders.up else 1,           # vers le haut
                     down = 0 if borders.down else 1)       # vers le bas
    
    # retourner la  structure indiquant les directions à explorer et de combien
    # de tuiles va t'on explorer dans chaque direction
    return offsets


# La fonction canMOve() prends la position d'une tuile, la largeur du jeu et
# le tableau contenant la configuration du jeu et utilise les fonctions
# tileBoders(), tileOffsets() et tileIndex() pour retourner l'index de la 
# tuile vide si celle si est dans le voisinage de la tuile. sinon la fonction
# retourne -1 (la tuile ne peu pas bouger)
# tile (Tuple) : contient position (x, y) de la tuile dans la gille de tuiles
# largeur (int) : nombre de rangées et de colonnes du jeu
# grid (list) : liste d'entiers représentant les tuiles du jeu
def canMove(tile, largeur, grid):
    
    # structure indiquant si la tuile se trouve en bordure du jeu et où
    borders = tileBorders(tile, largeur)
    
    # structure indiquant les directions à expolrer pour la tuile
    offsets = tileOffsets(borders)
    
    # le range duquel on va explorer le voisinage de la tuile horizontalement
    xStart = tile[0] - offsets.left
    xStop = tile[0] + offsets.right + 1
    
    # le range duquel on va explorer le voisinage de la tuile verticalement
    yStart = tile[1] - offsets.up
    yStop = tile[1] + offsets.down + 1
    
    # boucle qui explore a gauche et a droite de la tuile
    for x in range(xStart, xStop):
        
        # l'index de la tuile voisine 
        neighbourIndex = tileIndex((x, tile[1]), largeur)
        
        # si la tuile voisine est la tuile vide (r) on retourne son index
        if grid[neighbourIndex] == 0:
            return neighbourIndex
    
    # boucle qui explore en haut et en bas de la tuile    
    for y in range(yStart, yStop):
        
        # l'index de la tuile voisine
        neighbourIndex = tileIndex((tile[0], y), largeur)
        
        # si la tuile voisine est la tuile vide (r) on retourne son index
        if grid[neighbourIndex] == 0:
            return neighbourIndex
    
    # si aucune des tuiles voisines n'est la tuile vide
    return -1       # on retourne -1 (la tuile ne peu pas bouger)


# La fonction makeSolution() prends la largeur du jeu en paramètre et utilise
# la fonction makeTable() pour retourner un tableau d'entier represetant
# la solution finale du jeu de Taquin selon sa largeur.
# largeur (int) : nombre de rangées et de colonnes du jeu
def makeSolution(largeur):
    
    # Créer un tableau d'entiers de 0 à largeur * largeur - 1
    solution = makeTable(largeur*largeur)
    solution.remove(0)      # enlever 0 du début du tableau
    solution.append(0)      # rajouter 0 à la fin du tableau
    
    # retourner la solution du jeu
    return solution


# La procédure moveTile() prends l'index de la tuile vide, l'index de la tuile
# cliquée par le joeur, le tableau contennant la configuration du jeu et la
# largeur du jeu en paramètre. La procédure met à jour la configuration du jeu
# et utilise la procédure renderGrid() pour afficher la nouvelle configuration.
# indexR (int) : index de la tuile vide (r) dans la configuration du jeu
# clickedIndex (int) : index de la tuile cliquée par le joueur
# grid (list) : liste d'entiers représentant les tuiles du jeu 
# largeur (int) : nombre de rangées et de colonnes du jeu
def moveTile(indexR, clickedIndex, grid, largeur):
    
    # stocker temorairement la tuile vide (r)
    temp = grid[indexR]
    
    # remplacer la tuile vide par la tuile cliquée par le joeur
    grid[indexR] = grid[clickedIndex]
    
    # remplacer la tuile cliquée par la tuile vide
    grid[clickedIndex] = temp
    
    # afficher la nouvelle configuration sur l'écran
    renderGrid(largeur, grid)

        
# La fonction taquin() prends la largeur du jeu en paramètre et utilise toutes les
# procedures et fonctions définies afin d'éxecuter le déroulement du jeu de Taquin.
# largeur (int) : nombre de rangées et de colonnes du jeu
def taquin(largeur):
    
    # taille de l'écran en pixels
    # (16 px par tuile) * nombre de rangées et de colonnes du jeu
    screenSize = 16 * largeur
    
    # créer un écran d'une taille adaptée à la largeur du jeu
    setScreenMode(screenSize, screenSize)
    
    # boucle principale du jeu
    # recommence une nouvelle partie après chaque résolution du jeu
    while True:
        
        # créer la configuration initiale soluble du jeu
        grid = initial(largeur)
        
        # afficher la configuration initiale à l'écran
        renderGrid(largeur, grid)
        
        # créer la solution de cette configuration
        solution = makeSolution(largeur)
        
        # variable pour déterminé si le jeu est résolu ou non
        solved = False
        
        # boucle qui attends que le jeu soit résolu
        while not solved:
            
            # attendre que le joeur clique sur une tuile
            clickedTile = attendreClick()
            
            # stocker l'index de la tuile cliquée par le joueur
            indexClicked = tileIndex(clickedTile, largeur)
            
            # verifier si la tuile cliquée peu se déplacer
            # stocker l'index de la tuile vide voisine 
            # (-1 si la tuile cliquée ne peu pas se déplacer)
            indexR = canMove(clickedTile, largeur, grid)
            
            # si la tuile cliquée peu se déplacer
            if indexR >= 0:
                
                # mettre à jour la configuration du jeu
                # et mettre à jour l'affichage à l'écran
                moveTile(indexR, indexClicked, grid, largeur)
            
            # verifier si le jeu est résolu
            solved = grid == solution
        
        # quand le jeu est résolu afficher un message de félicitation au joueur
        else:
            alert('FÉLICITATION!')


# La fonction testTaquin a pour but de tester le bon fonctionnement des
# procédures et fonctions du programme afin de déceler touts bugs ou erreurs.
def testTaquin():
    
    # Tests unitaires de la fonction permutationAleatoire()
    assert permutationAleatoire(0) == []
    assert permutationAleatoire(-1)== []
    assert permutationAleatoire(1) == [0]
    assert permutationAleatoire(2) == [0, 1] or [1, 0]
    
    # Tests unitaires de la fonction inversions()
    assert inversions([0,2,9,1,4,3],2)== 1
    assert inversions([0,9,8,2,4,3],8)== 3
    assert inversions([0,0,0,0,0],0)== 0 
    assert inversions([1,2,3,4,5],1)== 0 
    assert inversions([1,8,5,4,2,6],6)== 0 
    
    # Tests unitaires de la fonction soluble()
    assert soluble([3,5,6,7,10,14,11,9,4,13,2,0,8,1,12,15])== True
    assert soluble([3,5,6,7,10,14,15,9,4,13,2,0,8,1,12,11])== False
    assert soluble([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])== False
    assert soluble([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0])== False
    assert soluble([14,15,9,12,11,10,13,2,7,6,5,4,3,8,1,0])== True
    
    # Tests unitaires de la fonction initial()
    # La fonction initiale nous retournant des tableaux aléatoire nous avons 
    # donc decider de tester quelques cas "spéciaux" et complétons nos tests
    # avec la vérification de la longueur du tableaux retourné. 
    assert initial(1)== [0]
    assert initial(0)== [] 
    assert len(initial(2))== 4
    assert len(initial(3))== 9 
    assert len(initial(4))== 16
    
    
    ###### Tests unitaires de la procédure afficherImage() ######
        
    # L'appel répéter de la procédure setScreenMode() lors des tests nous
    # permet de renitialisé les pixels de l'écran
    setScreenMode(16, 16)    
    
    
    afficherImage(0, 0, tuiles.colormap, tuiles.images[10])
    
    # r représente le texte qui doit être retourné par l'appel de la fonction
    # exportScreen() si la procéduure afficherImage() est valide 
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
    
    # La méthode .strip() nous permet d'enlever les espaces aux debut et à
    # la fin du texte facilitant ainsi la structure des tests.
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
    
    # Valeurs plus grande que l'image pour tester le positionnement des
    # pixels a l'endroit souhaité.
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
    
    
    ###### Tests unitaires de la procédure afficherTuile() ######
    
    #Ces valeurs furent choisies pour faciliter la mise en forme des tests
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
    
    # L'appel répéter de la procédure setScreenMode() lors des tests nous
    # permet de renitialisé les pixels de l'écran
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
