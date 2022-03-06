setScreenMode(64,64)
import tuiles

def afficherImage (x, y, colormap, image):
    rangée = image
    for i in range(len(tuiles.images)):
        for j in range (len(rangée)):
            c=rangée[i][j]
            setPixel((x+j),(y+i), tuiles.colormap[c])
            print(c)


def afficherTuile(x, y, tuile):
    afficherImage(x*16, y*16, tuiles.colormap, tuiles.images[tuile])
    
afficherTuile(3,3,10)
    
    
    

    
    
    