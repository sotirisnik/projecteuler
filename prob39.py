"""
a + b + c = p => c = p - a - b => c^2 = ( p - a - b )^2
a^2 + b^2 = c^2

=> a^2 + b^2 = ( p - a - b )^2
=> (a^2) + (b^2) = (a^2) + 2*a*b - 2*a*p + (b^2) - 2*b*p + p^2
=> 0 = 2*a*b - 2*a*p - 2*b*p + p^2
=> b * 2 * ( a - p ) = 2*a*p - p*2
=> b = p*( 2*a - p ) / ( 2*(a-p) )
"""

def f( a, b, p ):
    return ( a*a + b*b - ( p - a - b ) ** 2 )

p = 120

ans = 0
Pans = -1

for p in range( 1, 1001 ):

    count = 0
    for a in range( 1, 1001 ):
        if a == p:
            continue
        
        mid = p*( 2*a - p ) / ( 2*(a-p) )
        
        if f(a,mid,p) == 0:
            count += 1

    if count > ans:
        ans = count
        Pans = p
        
print "%d" % (Pans)