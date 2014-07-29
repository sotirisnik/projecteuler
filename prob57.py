num = 3
denom = 2

ans = 0

for i in range( 0, 1000 ):
    
    if len( str(num) ) > len( str(denom) ):
        ans += 1
    
    Sum = num + denom
    
    num += 2*denom
    denom = Sum
    
print "%d" % (ans)