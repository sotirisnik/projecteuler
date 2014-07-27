import math

#for a in range( -1000, 1001 ):
#    for b in range( -1000, 1001 ):

a = -79
b = 1601

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

MaxAns = 0
Product = 0

for a in range( -999, 1000 ):
    for b in range( -999, 1000 ):
        n = 0
        while isprime( n*n + a*n + b):
            n = n + 1
        if n > MaxAns:
            MaxAns = n
            Product = a*b

print "%d" % (Product)