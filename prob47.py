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

memo = {}

def distinct_fact( n ):
    
    counter = 0
    
    for i in Primes:
        
        if n % i == 0:
            counter += 1
        
        if counter > 4:
            return -1
        
        while n % i == 0:
            n /= i
        
        if n == 1:
            break
        
    return ( counter )
    
i = 2

Found = False

while not Found:
    
    i += 1
    
    Found = True
    
    for j in range( 0, 4 ):
        if distinct_fact( i+j ) != 4:
            Found = False
            break
    
    
print "%d" % (i)