import math

Primes = []
P = []

MAXN = 1000000
sqrt_MAXN = int(math.sqrt( MAXN )) + 1

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
            
            
for i in range( 0, MAXN ):
    P.append( True )
    
for i in range( 2, sqrt_MAXN ):
    if P[i]:
        for j in range( i*i, MAXN, i ):
            P[j] = False

for i in range( 2, MAXN ):
    if P[i]:
        Primes.append( i )

def is_candidate( x, check_prime ):
    if check_prime:
        if not isprime( x ):
            return ( False )
    return ( len( str( x ) ) == 4 )
        
i = 236

Found = False
        
for i in range( i, len(Primes) ):
    if Found:
        break
    for j in range( i+1, len(Primes) ):
        if is_candidate( Primes[i], 0 ) and is_candidate( Primes[j], 0 ) and is_candidate( 2*Primes[ j ] - Primes[i], 1 ):
            if sorted( str(Primes[i]) ) == sorted( str( Primes[j] ) ) == sorted( str( 2*Primes[j] - Primes[i] ) ):
                print "%s" % ( str(Primes[i]) + str( Primes[j] ) + str( 2*Primes[j] - Primes[i] ) )
                Found = True
                break