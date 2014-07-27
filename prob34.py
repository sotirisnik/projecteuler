memo = {}

def f( n ):

    if n == 0:
        return 1
        
    if n in memo:
        return memo[ (n) ]
        
    memo[n] = n * f(n-1)
    
    return ( memo[n] )

def sum_fact( x ):
    
    ret = 0
    
    while x > 0:
        ret += f( x%10 )
        x /= 10
        
    return ( ret )
    
ans = 0
    
for i in range( 3, 2540161 ):
    if i == sum_fact( i ):
        ans += i
        
print "%d" % (ans)