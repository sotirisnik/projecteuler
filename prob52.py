i = 0

Found = False

while not Found:

    i += 1
    
    tmp = sorted( str(i) )
    
    Found = True
    
    for j in range( 2, 7 ):
        if tmp != sorted( str(i*j) ):
            Found = False
            break
            
print "%d" % (i)