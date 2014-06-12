def d( n ):
    ret = 0
    for i in range( 1, n ):
        if n % i == 0:
            ret += i
    return ( ret )

N = 10000

P = {}

for a in range( 1, N ):
    b = d(a)
    if a != b and d(b) == a:
        P[(a)] = 1
        P[(b)] = 1
        
ans = 0

for i in P:
    ans += i
    
print "%d" % ( ans )