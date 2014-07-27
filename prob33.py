def gcd( a, b ):
    if b == 0:
        return ( a )
    return ( gcd( b, a%b ) )
   
def is_curious( a, b ):

    if b % 10 == 0:
        return ( False )

    A = str(a)
    B = str(b)
    
    for i in range( 0, len(str(A)) ):
        for j in range( 0, len(str(B)) ):
            if A[i] == B[j]:
                c = int( A[0:i] + A[i+1:len(A)] )
                d = int( B[0:j] + B[j+1:len(B)] )
                if d == 0:
                    continue
                if a * d == c * b:
                    #print "%s %s" % (A, B)
                    return ( True )
    
    return ( False )
    
L = []

ans = 1

for num in range( 10, 100 ):
    for denom in range( num+1, 100 ):
        if is_curious( num, denom ):
            L.append( (num,denom) )
            
num = 1
denom = 1

for i in L:
    num *= i[0]
    denom *= i[1]

GCD = gcd( num, denom )

print "%d" % (denom / GCD)