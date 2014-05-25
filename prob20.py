memo = {}

def f( x ):
    if x == 0:
        return 1
    
    if x in memo:
        return ( memo[x] )
    
    memo[x] = x*f(x-1)
    
    return ( memo[x] )

tmp = f(100)
ans = 0

while tmp > 0:
    ans += ( tmp % 10 )
    tmp /= 10
    
print "%d" % ( ans )