import math

Primes = []
P = []

MAXN = 10000
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
    
    if x > Primes[-1]:
        sqrt_x = int(x**0.5)+1
        for i in range( 3, sqrt_x, 2 ):
            if x % i == 0:
                return ( False )
        return ( True )
        
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

Sets = []

for i in range( 0, Primes[-1]+1 ):
    Sets.append( set() )

for i in range( 0, len(Primes) ):
    for j in range( i+1, len( Primes ) ):
        if isprime( int( str( Primes[i] ) + str( Primes[j] ) ) ) and isprime( int( str( Primes[j] ) + str( Primes[i] ) ) ):
            Sets[ Primes[i] ].add( Primes[j] )

Found = False
ans = 0
BestSol = []

def go( L, S, depth ):

    global Found, ans, BestSol
    
    if depth == 0:
        if not Found:
            ans = sum(L)
            BestSol = L
            Found = True
        else:
            if ans > sum(L):
                ans = sum(L)
                BestSol = L
        return
        
    for i in S:
        go( L + [i], S & Sets[i], depth-1 )
            
for i in range( 0, len(Sets) ):
    go( [i], Sets[i], 4 )
        
print "%d" % (ans)