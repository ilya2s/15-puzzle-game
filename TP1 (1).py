setScreenMode(64,64)
import tuiles

def afficherImage (x, y, colormap, image):
    rangée = image
    for i in range(len(tuiles.images)):
        for j in range (len(rangée)):
            c=rangée[i][j]
            setPixel((x+j),(y+i), tuiles.colormap[c])


def afficherTuile(x, y, tuile):
    afficherImage(x*16, y*16, tuiles.colormap, tuiles.images[tuile])
    
    
for i in range(4):
    for j in range(4):
        afficherImage(i*16, j*16, tuiles.colormap, tuiles.images[10])
    
    
        
def attendreClick():
    
    while True:
        sleep(0.01)
        a = getMouse()
        if a.button==1:
            return ((a.x)//16, (a.y)//16 ) 
        continue

print(attendreClick())

    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    

    
    
    