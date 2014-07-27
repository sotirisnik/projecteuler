import math

def P( n ):
    return ( 0.5*n*(3*n-1) )
    

def inverseP( x ):
    """
    3*n^2 -n = 2*x
    3*n^2 - n -2*x = 0
    D = b^2 - 4*a*g = 1 + 24*x
    x1,2 = (1 +- ( sqrt( 1 + 24*x) ) ) / 2*3
    """
    return ( ( (1.0 + math.sqrt( 1 + 24*x ) ) / 6.0  ) )

def isP( x ):
    tmp = inverseP(x)
    return ( tmp == int( tmp ) )
    
i = 2

Found = False

while not Found:
    for j in range( 1, i ):
        S = P(i) + P(j)
        D = P(i) - P(j)
        if isP(S) and isP(D):
            print "%d" % ( abs( D ) )
            Found = True
            break
    i += 1
