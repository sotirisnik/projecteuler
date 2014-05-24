memo = {}

def f( x ):

    if x == 1:
        return 0

    if x in memo:
        return ( memo[x] )
        
    if x % 2 == 0:
        memo[x] = ( 1 + f( x/2 ) )
        return ( memo[x] )
        
    memo[x] = ( 1 + f( 3*x + 1 ) )
    
    return ( memo[x] )
    
Maxim = 0
pos = 0

for i in range( 1, 1000000 ):
    tmp = f( i )
    if tmp > Maxim:
        Maxim = tmp
        pos = i
    
print "%d" % ( pos )