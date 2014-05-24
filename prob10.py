L = []

N = 1999999

for i in range( 0, N+1 ):
    L.append( True )

sqrt_N = int( N**(0.5) )

for i in range( 2, sqrt_N+1 ):
    if L[i]:
        for j in range( i*i, N+1, i ):
            L[j] = False

ans = 0

for i in range( 2, N+1 ):
    if L[i]:
        ans += i
        
print "%d" % ( ans )