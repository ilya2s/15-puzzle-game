import random
import math
import tuiles


def afficherImage (x, y, colormap, image):
    size = len(image)
    
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
