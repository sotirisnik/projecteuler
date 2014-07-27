Moves = []

for i in range( 0, 18 ):
    Moves.append( [] )
       
for i in range( 1, 1000 ):
    for j in [ 2, 3, 5, 7, 11, 13, 17 ]:
        if i % j == 0:
            Moves[j].append( '0'*( 3-len( str(i) ) ) + str(i) )
            
def is_pan( x ):
    return ( len( set( x ) ) == 10 )

def make_moves( x, tmp, which ):
    for k in range( 0, 10 ):
            next = tmp[-2] + tmp[-1] + str(k)
            if next in Moves[which]:
                dfs( x+1, tmp + str(k) )
    
def dfs( x, tmp ):

    global ans

    if x == 7:
        if len(tmp) == 10 and is_pan( tmp ):
            ans += int(tmp)
        return

    if x == 0:
        for j in Moves[2]:
            dfs( x+1, tmp + j )
    elif x == 1:
        make_moves( x, tmp, 3 )
    elif x == 2:
        make_moves( x, tmp, 5 )
    elif x == 3:
        make_moves( x, tmp, 7 )
    elif x == 4:
        make_moves( x, tmp, 11 )
    elif x == 5:
        make_moves( x, tmp, 13 )
    elif x == 6:
        make_moves( x, tmp, 17 )

ans = 0
                
for i in range( 0, 10 ):
    dfs( 0, str(i) )
    
print "%d" % (ans)