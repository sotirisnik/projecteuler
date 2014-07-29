n = 10000

ans = 0

for i in range( 1, n ):

    val = i
    
    Found = True
    
    for j in range( 0, 49 ):
        tmp = val + int( str(val)[::-1] )
        if str(tmp) == str(tmp)[::-1]:
            Found = False
            break
        val = tmp
    
    ans += Found
    
print "%d" % (ans)