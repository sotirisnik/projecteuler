def is_prime( n ):

    if n < 2:
        return ( False )

    for i in range( 2, n ):
        if n % i == 0:
            return ( False )
    
    return ( True )

def is_candidate( x ):

    if x % 2 == 0:
        return ( False )
    
    for i in range( 1, x ):
        p = x - 2 * (i**2)
        if is_prime( p ):
            return ( True )
    
    return ( False )
    
i = 9

while True:
    if not is_prime(i) and not is_candidate( i ):
        print "%d" % (i)
        break
    i += 2