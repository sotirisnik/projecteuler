import math

def T( n ):
    return ( 0.5 * n * ( n + 1 ) )

def P( n ):
    return ( 0.5 * n * ( 3 * n - 1 ) )
    
def H( n ):
    return ( n * ( 2*n - 1 ) )
    
def inverseT( x ):
    """
    n * ( n + 1 ) - 2*x = 0
    n^2 + n - 2*x = 0
    D = b^2 - 4*a*g = 1 - 4*1*(-2*x) = 1 + 8*x
    x1,2 = ( -b +- sqrt( D ) ) / 2*a
    = ( -1 +- sqrt( 1 + 8*x ) ) / 2
    """
    return ( 0.5 * ( -1 + math.sqrt( 1 + 8*x ) ) )
    
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
        
def isT( x ):
    tmp = inverseT( x )
    return ( tmp == int( tmp ) )

def isP( x ):
    tmp = inverseP( x )
    return ( tmp == int( tmp ) )
    
def isH( x ):
    tmp = inverseH( x )
    return ( tmp == int( tmp ) )

n = 286
    
while True:
    tmp = T( n )
    if isP( tmp ) and isH( tmp ):
        break
    n += 1
    
print "%d" % ( T(n) )