def is_abudant( n ):
    ret = 0
    for i in range( 1, n ):
        if n % i == 0:
            ret += i
    return ( ret > n )

def range_sum( x ):
    return ( ( 1 + x ) * ( x ) / 2 )
    
limit = 28123

P = {}

for i in range( 1, limit ):
    if is_abudant( i ):
        P[(i)] = 1
        
Q = {}

for i in P:
    for j in P:
        if i + j >= limit:
            break
        Q[(i+j)] = 1
        
print "%d" % (range_sum( limit-1 )-sum(Q))