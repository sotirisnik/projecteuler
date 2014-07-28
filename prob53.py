memo = {}

def fact( n ):

    if n == 0:
        return 1
    
    if n in memo:
        return ( memo[n] )
    
    memo[n] = n * fact( n - 1 )
    
    return ( memo[n] )

def c( n, r ):
    if r > n:
        return 0
    return ( fact(n) / ( fact(r) * fact( n-r ) ) )

limit = 1000000
    
n = 100

A = []
    
for i in range( 1, n+1 ):
    for j in range( 0, i+1 ):
        tmp = c( i, j )
        if tmp > limit:
            A.append( c(i,j) )
            
print "%d" % ( len(A) )