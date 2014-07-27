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
    
def is_truncatable_prime( x ):
    X = str(x)
    
    Len = len(X)
   
    for i in range(0, Len ):
        if not isprime( int(X) ):
            return ( False )
        X = X[1::]
        
    X = str(x)[0:len(X)-1]
    Len -= 1
    
    for i in range(0, Len ):
        if not isprime( int(X) ):
            return ( False )
        X = X[0:len(X)-1:]
    
    return ( True )
    
count = 0
how = 11
ans = 0

for i in Primes:
    if i < 10:
        continue
    if count < how and is_truncatable_prime( i ):
        ans += i
        count += 1
        
print "%d" % (ans)