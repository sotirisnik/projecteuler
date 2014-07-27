MAXN = 1000000

def is_pal( x ):
    for i in range( 0, len(x)/2 ):
        if x[i] != x[ len(x)-i-1 ]:
            return ( False )
    return ( True )

ans = 0

for i in range( 1, MAXN ):
    if is_pal( str(i) ) and is_pal( bin(i)[2::] ):
        ans += i
        
print "%d" % (ans)