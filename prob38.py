L = []

def is_pan( x ):

    for i in range( 0, 10 ):
        L[i] = 0

    while x > 0:
        L[ x%10 ] += 1
        if L[ x%10 ] >= 2:
            return ( False )
        x /= 10
    
    for i in range( 1, 10 ):
        if L[i] != 1:
            return ( False )
    
    return ( True and L[0] == 0 )
    
ans = 0

for i in range( 0, 10 ):
    L.append( 0 )

for i in range( 1, 10000 ):
    tmp = ""
    for j in range( 1, 10 ):
        tmp += str(j*i)
        if len(tmp) > 9:
            break
        if len(tmp) == 9 and is_pan( int(tmp) ):
            ans = max( ans, int(tmp) )
        
print "%d" % (ans)