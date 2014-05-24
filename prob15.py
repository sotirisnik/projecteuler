memo = {}

def f( n, m ):
    if m == 0 or n == m:
        return 1
    if m == 1:
        return n
    
    if (n,m) in memo:
        return ( memo[ (n,m) ] )
    
    memo[ (n,m) ] = f( n-1, m ) + f( n-1, m-1 )

    return ( memo[ (n,m) ] )
    
n = 20
    
print "%d" % ( f(2*n,n) )