n = 100

L = []

for a in range( 2, n+1 ):
    for b in range( 2, n+1 ):
        L.append( a**b )
        
print "%d" % ( len( set(L) ) )