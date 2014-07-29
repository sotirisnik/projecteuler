import math

Primes = []
P = []

MAXN = 1000000
sqrt_MAXN = int(math.sqrt( MAXN )) + 1

def isprime( x ):

    if x < 2:
        return ( False )

    if x % 2 == 0:
        return ( False )
        
    sqrt_x = int(x**0.5)+1
    
    for i in range( 3, sqrt_x, 2 ):
        if x % i == 0:
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

amount = 1
step = 2
side_length = 1

tot_primes = 0

while True:

    for j in range( 0, 4 ):
        amount += step
        if isprime( amount ):
            tot_primes += 1
    
    side_length += 2
    step += 2
  
    if 10*(tot_primes) < 2*side_length-1:
        break
        
print "%d" % (side_length)
    
"""
1
3 5 7 9
13 17 21 25"""