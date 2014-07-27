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

def is_circular( x ):
    X = str(x)
    
    for i in range( 0, len(X) ):
        X = X[1:len(X)] + X[0]
        if not isprime( int(X) ):
            return ( False )
    
    return ( True )
            
for i in range( 0, MAXN ):
    P.append( True )
    
for i in range( 2, sqrt_MAXN ):
    if P[i]:
        for j in range( i*i, MAXN, i ):
            P[j] = False

for i in range( 2, MAXN ):
    if P[i]:
        Primes.append( i )
       
ans = 0
        
for i in Primes:
    if is_circular( i ):
        ans += 1
        
print "%d" % (ans)