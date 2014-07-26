n = 354294

ans = 0

def sum_fifth( x ):
    ret = 0
    while x > 0:
        ret = ret + (x%10)**5
        x = x / 10
    return ( ret )

for i in range( 10, n+1 ):
    if sum_fifth( i ) == i:
        ans = ans + i
        
print "%d" % (ans)