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

F = []

F.append( Primes[0] )

for i in range( 1, len(Primes) ):
    F.append( F[i-1] + Primes[i] )
    
def rangeSum( i, j ):
    if i-1 < 0:
        return ( F[j] )
    return ( F[j] - F[i-1] )
    
ans = 0    

Found = False
    
for k in range( len(Primes)-1, -1, -1 ):        
    if Found:
        break
    for j in range( 0, len(Primes)-k ):
        if rangeSum(j,j+k) > MAXN:
            break
        if isprime( rangeSum(j,j+k) ):
            Found = True
            ans = rangeSum(j,j+k)
            
print "%d" % (ans)