ans = 0

L = []
A = []

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

for i in range( 0, 10 ):
    L.append( 0 )
    
for a in range( 1, 10000 ):
    for b in range( 1, 10000 ):
        tmp = a*b
        candidate = str(a) + str(b) + str(tmp)
        if len(candidate) > 9:
            break
        if len(candidate) != 9:
            continue
        if is_pan( int( candidate ) ):
            A.append( tmp )
            
A = ( set(A) )

for i in A:
    ans += i
    
print "%d" % (ans)