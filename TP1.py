import tuiles

setScreenMode(64,64)

def afficherImage (x, y, colormap, image):
    rangee = image
    for i in range(len(tuiles.images)):
        for j in range (len(rangee)):
            c=rangee[i][j]
            setPixel((x+j),(y+i), tuiles.colormap[c])


def afficherTuile(x, y, tuile):
    taille = len(tuiles.images)
    afficherImage(x*taille, y*taille, tuiles.colormap, tuiles.images[tuile])
    
afficherTuile(3,3,10)
    
    
    

    
    
    