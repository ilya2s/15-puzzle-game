import random
import math
import tuiles


def afficherImage (x, y, colormap, image):
    size = len(image)
    
    x = -x if x < 0 else x
    y = -y if y < 0 else y
    
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
    
    if not len(tab) % 2 and len(tab) != 0:
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
