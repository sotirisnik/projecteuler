M = {}

M[1] = 'one'
M[2] = 'two'
M[3] = 'three'
M[4] = 'four'
M[5] = 'five'
M[6] = 'six'
M[7] = 'seven'
M[8] = 'eight'
M[9] = 'nine'
M[10] = 'ten'
M[11] = 'eleven'
M[12] = 'twelve'
M[13] = 'thirteen'
M[14] = 'fourteen'
M[15] = 'fifteen'
M[16] = 'sixteen'
M[17] = 'seventeen'
M[18] = 'eighteen'
M[19] = 'nineteen'
M[20] = 'twenty'
M[30] = 'thirty'
M[40] = 'forty'
M[50] = 'fifty'
M[60] = 'sixty'
M[70] = 'seventy'
M[80] = 'eighty'
M[90] = 'ninety'
M[1000] = 'onethousand'

def f( x ):
    
    if x in M:
        return ( M[x] )
        
    if x >= 100:
        ret = M[ (x/100) ] + 'hundred'
        if x % 100 != 0:
            ret += 'and' + f( x - (x/100)*100 )
        return ( ret )
    elif x > 10:
        return ( M[ (x/10)*10 ] + f( x - (x/10)*10 ) )
    
ans = 0
    
for i in range( 1, 1001):
    ans += len( f(i) )
print "%d" % ( ans )