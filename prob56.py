def digit_sum( x ):
    
    ret = 0
    
    while x > 0:
        ret += x%10
        x /= 10
    
    return ( ret )

MaxVal = 0
n = 100

for a in range( 1, n ):
    for b in range( 0, n ):
        MaxVal = max( MaxVal, digit_sum( a**b ) )
        
print "%d" % (MaxVal)