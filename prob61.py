import math

def T( n ):
    return ( 0.5 * n * ( n + 1 ) )

def S( n ):
    return ( n * n )
    
def P( n ):
    return ( 0.5 * n * ( 3 * n - 1 ) )
    
def H( n ):
    return ( n * ( 2*n - 1 ) )

def Hept( n ):
    return ( 0.5 * n * ( 5*n - 3 ) )
    
def Oct( n ):
    return ( n * ( 3*n - 2 ) )
    
def inverseT( x ):
    """
    n * ( n + 1 ) - 2*x = 0
    n^2 + n - 2*x = 0
    D = b^2 - 4*a*g = 1 - 4*1*(-2*x) = 1 + 8*x
    x1,2 = ( -b +- sqrt( D ) ) / 2*a
    = ( -1 +- sqrt( 1 + 8*x ) ) / 2
    """
    return ( 0.5 * ( -1 + math.sqrt( 1 + 8*x ) ) )
    
def inverseS( x ):
    return ( (x**0.5) )
    
def inverseP( x ):
    """
    n * ( 3*n - 1 ) - 2*x = 0
    3*n^2 - n - 2*x = 0
    D = b^2 - 4*a*g = 1 - 4*3*(-2*x) = 1 + 24*x
    x1,2 = ( -b +- sqrt( D ) ) / 2*a
    = ( 1 +- sqrt( 1 + 24*x ) ) / 6
    """
    return ( ( 1 + math.sqrt( 1 + 24*x ) ) / 6 )
    
def inverseH( x ):
    """
    n * ( 2*n - 1 ) - x = 0
    2*n^2 - n - x = 0
    D = b^2 - 4*a*g = 1 - 4*2*(-x) = 1 + 8*x
    x1,2 = ( -b +- sqrt( D ) ) / 2*a
    = ( 1 +- sqrt( 1 + 8*x ) ) / 4
    """
    return ( 0.25 * ( 1 + math.sqrt( 1 + 8*x ) ) )

def inverseHept( x ):
    """
    n*(5*n - 3) = 2*x
    5*n^2 - 3*n - 2*x = 0
    D = b^2 - 4*a*g = 9 - 4*5*(-2*x) = 9 + 40*x
    x1,2 = ( -b +- sqrt( D ) ) / 2*a
    = ( 3 +- sqrt( 9 + 40*x ) ) / 10
    """
    return ( ( 3 + math.sqrt( 9 + 40*x ) ) / 10 )
    
def inverseOct( x ):
    """
    n * ( 3*n - 2 ) = x
    3*n^2 - 2*n - x = 0
    D = b^2 - 4*a*g = 4 - 4*3*(-x)
    = 4 + 12*x
    x1,2 = ( -b +- sqrt( D ) ) / 2*a
    = ( 2 +- sqrt( 4 + 12*x ) ) / 6
    """
    return ( ( 2 + math.sqrt( 4 + 12*x ) ) / 6 )
    
def isT( x ):
    tmp = inverseT( x )
    return ( tmp == int( tmp ) )

def isS( x ):
    tmp = inverseS( x )
    return ( tmp == int( tmp ) )
    
def isP( x ):
    tmp = inverseP( x )
    return ( tmp == int( tmp ) )
    
def isH( x ):
    tmp = inverseH( x )
    return ( tmp == int( tmp ) )

def isHept( x ):
    tmp = inverseHept( x )
    return ( tmp == int( tmp ) )
    
def isOct( x ):
    tmp = inverseOct( x )
    return ( tmp == int( tmp ) )
    
def join_num( i, j ):
    
    x = str(i)
    y = str(j)
    
    while len(x) < 2:
        x = "0" + x

    while len(y) < 2:
        y = "0" + y
        
    return ( ( x + y ) )
    
def go( L, Number, Sum, Numbers ):

    global Solution_Found

    if Solution_Found:
        return
    
    if len ( str(Number) ) != 4:
        return
    
    if len(L) == 0:
    
        if int(Numbers[0])/100 != int(Numbers[-1])%100:
            return
            
        if len( set(Numbers) ) == 6:
            #print Numbers
            print "%d" % (Sum)
            Solution_Found = True
        return
        
    for i in L:
        
        for j in range( 0, 100 ):
            
            tmp = join_num( Number%100, j )
            val = int(tmp)
            
            if len( str(val) ) != 4:
                continue
            
            Found = False
            
            if i == 'T':
                if isT( val ):
                    Found = True
            elif i == 'S':
                if isS( val ):
                    Found = True
            elif i == 'P':
                if isP( val ):
                    Found = True
            elif i == 'H':
                if isH( val ):
                    Found = True
            elif i == 'He':
                if isHept( val ):
                    Found = True
            elif i == 'O':
                if isOct( val ):
                    Found = True
            if Found:
                sl = L.copy()
                sl.remove( i )
                go( sl, val, Sum + val, Numbers + [tmp] )

start_list = set( ['T','S','P','H','He','O'] )
   
Solution_Found = False
   
for i in range( 1000, 10000 ):

    if Solution_Found:
        break

    if isT( i ):
        sl = start_list.copy()
        sl.remove( 'T' )
        go( sl, i, i, [i] )
        
    if isS( i ):
        sl = start_list.copy()
        sl.remove( 'S' )
        go( sl, i, i, [i] )
    
    if isP( i ):
        sl = start_list.copy()
        sl.remove( 'P' )
        go( sl, i, i, [i] )
    
    if isH( i ):
        sl = start_list.copy()
        sl.remove( 'H' )
        go( sl, i, i, [i] )
    
    if isHept( i ):
        sl = start_list.copy()
        sl.remove( 'He' )
        go( sl, i, i, [i] )
    
    if isOct( i ):
        sl = start_list.copy()
        sl.remove( 'O' )
        go( sl, i, i, [i] )