Count = []
Pos = []

for i in range( 0, 1000 ):
    Count.append( 0 )
    Pos.append( 0 )

MaxAns = 0
MaxPos = 0
    
for i in range( 2, 1000 ):
    
    num = 1
    denum = i
    
    for j in range( 0, 1000 ):
        Count[ j ] = 0
        Pos[ j ] = 0
    
    k = 0
    ans = 0
    
    while True:
    
        k = k + 1
    
        if num == 0:
            #print "%d %d" % ( i, k-1 )
            ans = k - 1
            break
    
        while num < denum:
            Count[ num  ] = Count[ num ] + 1
            Pos[ num ] = k
            num = num * 10
        num = num % denum
        Count[ num ] = Count[ num ] + 1
        
        if Count[ num ] >= 2:
            #print "%d %d" % ( i, k - Pos[ num ] + 1 )
            ans = k - Pos[ num ] + 1
            break
    
        Pos[ num ] = k
    
    if ans > MaxAns:
        MaxAns = ans
        MaxPos = i
    
print MaxPos