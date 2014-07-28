import math

Primes = []
P = []

MAXN = 1000000
sqrt_MAXN = int(math.sqrt( MAXN )) + 1

def isprime( x ):
    lo = 0
    hi = len(Primes)-1
    
    while lo <= hi:
        mid = ( lo + hi ) / 2
        if Primes[ mid ] == x:
            return ( True )
        elif Primes[ mid ] > x:
            hi = mid-1
        else:
            lo = mid+1
            
    return ( False )
            
            
for i in range( 0, MAXN ):
    P.append( True )
    
for i in range( 2, sqrt_MAXN ):
    if P[i]:
        for j in range( i*i, MAXN, i ):
            P[j] = False

for i in range( 2, MAXN ):
    if P[i]:
        Primes.append( i )
        
Moves = []

for i in range( 0, 9 ):
    Moves.append( [] )
    
def f( idx, count, what, where ):
    
    if idx > 7 or count == 0:
        if len( what ) > 0 and count == 0:
            #print "what = %s" % (what)
            Moves[where].append( what )
        return
        
    f( idx+1, count-1, what + str(idx), where )
    f( idx+1, count, what, where )

for i in range( 1, 9 ):
    f( 0, i, "", i )
    
ans = 0

Solutions = []

for i in range( 0, 8 ):
    Solutions.append( "" )
    
D = []

for i in range( 0, 3 ):
    D.append( 0 );

Found = False
    
for i in Primes:
    
    if Found:
        break
        
    for j in range( 0, 3 ):
        D[j] = 0
    for j in str(i):
        if j == '0':
            D[0] += 1
        elif j == '1':
            D[1] += 1
        elif j == '2':
            D[2] += 1
    
    tmp = str(i)
    
    for j in range( 0, 2 ):
        
        if Found:
            break
            
        if D[j] != 0:
        
            for u in range( 0, len( str(i) ) ):
                
                if Found:
                    break
                    
                for k in Moves[ u ]:
                    
                    if int(k[0]) >= len( tmp ):
                        continue
                
                    val = tmp[ int(k[0]) ]
                    Found = True
                    
                    for z in k:
                        if int(z) >= len(tmp):
                            Found = False
                            break
                        if tmp[int(z)] != val:
                            Found = False
                            break
                    
                    if Found:
                        for t in range( 0, 8 ):
                            Solutions[t] = ""
                        
                        for a in range( 0, len( str(i) ) ):
                            
                            for t in range( 0, 8 ):
                                if str(a) in k:
                                    Solutions[t] += str(  int(tmp[a]) + t + 1 )
                                else:
                                    Solutions[t] += tmp[a]
                    
                        counter = 0
                        for t in range( 0, 8 ):
                            if isprime( int(Solutions[t]) ):
                                counter += 1
                        
                        if counter == 7:
                            Found = True
                            ans = i
                            break
                        else:
                            Found = False
                        
print "%d" % (ans)