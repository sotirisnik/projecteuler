L = []
adj = 4

def valid( x, y ):
    return ( x >= 0 and y >= 0 and x <= 19 and y <= 19 )
    
def up( x, y ):
    if not valid( x-adj+1, y ):
        return 0
    ret = L[x][y]
    for i in range( 1, adj ):
        ret *= L[x-i][y]
    return ( ret )
    
def down( x, y ):
    if not valid( x+adj-1, y ):
        return 0
    ret = L[x][y]
    for i in range( 1, adj ):
        ret *= L[x+i][y]
    return ( ret )

def left( x, y ):
    if not valid( x, y-adj+1 ):
        return 0
    ret = L[x][y]
    for i in range( 1, adj ):
        ret *= L[x][y-i]
    return ( ret )
    
def right( x, y ):
    if not valid( x, y+adj-1 ):
        return 0
    ret = L[x][y]
    for i in range( 1, adj ):
        ret *= L[x][y+i]
    return ( ret )

def diag( x, y ):
    if not valid( x+adj-1, y+adj-1 ):
        return 0
    ret = L[x][y]
    for i in range( 1, adj ):
        ret *= L[x+i][y+i]
    return ( ret )

def sec_diag( x, y ):
    if not valid( x+adj-1, y-adj+1 ):
        return 0
    ret = L[x][y]
    for i in range( 1, adj ):
        ret *= L[x+i][y-i]
    return ( ret )     

for i in range( 0, 20 ):
    x = raw_input().split( " " )
    T = []
    for j in x:
        T.append( int(j) )
    L.append( T )
    
Maxim = 0

for i in range( 0, 20 ):
    for j in range( 0, 20 ):
        Maxim = max( Maxim, up( i,j ), down( i,j ), left( i, j ), right( i,j ), diag( i, j ), sec_diag( i, j ) )

print "%d" % ( Maxim )