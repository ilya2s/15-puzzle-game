def inversions(tab, x):
    
    index = tab.index(x) + 1
    
    counter = 0
    
    for i, element in range(index, len(tab)):
        
        if tab[element] < x and tab[element] != 0:
            counter += 1

