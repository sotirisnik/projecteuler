x = raw_input().split(',')

for i in range( 0, len(x) ):
    x[i] = int( x[i] )

#print x


L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
SP = [ ord( ' ' ),  ord('!'), ord( '\''), ord('('), ord(')'), ord(','), ord('.'), ord(';') ]

def isSP( x ):

    lo = 0
    hi = len( SP )-1
    
    while lo <= hi:
        mid = ( lo + hi ) / 2
        if SP[ mid ] == x:
            return ( True )
        elif SP[ mid ] > x:
            hi = mid-1
        else:
            lo = mid+1
            
    return ( False )
    

Found = False
    
for a in L:
    if Found:
        break
    for b in L:
        if Found:
            break
        for c in L:
            if Found:
                break
            
            matches = 0
            
            counter = 0
            
            for i in range( 0, len(x) ):
                
                val = x[i]^ord(a)
                
                if counter == 1:
                    val = x[i]^ord(b)
                elif counter == 2:
                    val = x[i]^ord(c)
                
                counter += 1
                
                if counter == 3:
                    counter = 0
                
                if ( ord('a') <= val <= ord('z') ) or ( ord('0') <= val <= ord('9') ) or ( ord('A') <= val <= ord('Z') ) or isSP( val ):
                    matches += 1
            
            if matches == len(x):
                
                print "Encryption key consists of: %c%c%c" % ( a, b, c )
           
                print "Original text is:"
           
                ans = 0
           
                msg = ""
                for i in range( 0, len(x) ):
                    t = a
                    if i % 3 == 1:
                        t = b
                    elif i % 3 == 2:
                        t = c
                    ans += x[i]^ord(t)
                    msg += str( chr( x[i]^ord(t) ) )
                    
                print msg
                
                print "Solution is: %d" % (ans)
                
                Found = True