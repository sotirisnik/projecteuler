import math

a = -79
b = 1601

Primes = []
P = []

MAXN = 7654321
sqrt_MAXN = int(math.sqrt( MAXN )) + 1

L = []

def is_pan( x, where ):

    for i in range( 0, where+1 ):
        L[i] = 0

    while x > 0:
        if x%10 > where:
            return ( False )
        L[ x%10 ] += 1
        if L[ x%10 ] >= 2:
            return ( False )
        x /= 10
    
    for i in range( 1, where+1 ):
        if L[i] != 1:
            return ( False )
    
    return ( True and L[0] == 0 )

def isprime( x ):
    lo = 0
    hi = len(Primes)-1
    
    while lo <= hi:
        mid = ( lo + hi ) / 2
        if Primes[ mid ] == x:
            return ( True )
        elif Primes[ mid ] > x:
            hi = mid-1
        else:
            lo = mid+1
            
    return ( False )


for i in range( 0, 10 ):
    L.append( 0 )    
            
for i in range( 0, MAXN ):
    P.append( True )
    
for i in range( 2, sqrt_MAXN ):
    if P[i]:
        for j in range( i*i, MAXN, i ):
            P[j] = False
            
for i in range( 2, MAXN ):
    if P[i]:
        Primes.append( i )
            
for i in Primes[::-1]:
    if is_pan( i, 7 ):
        print "%d" % (i)
        break