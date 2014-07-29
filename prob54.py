Weight = { '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }
    
def sort_hand( x ):

    for i in range( len(x)-1, 0, -1 ):
        for j in  range( 1, i+1 ):
            if Weight[ x[j-1][0] ] > Weight[ x[j][0] ]:
                tmp = x[j]
                x[j] = x[j-1]
                x[j-1] = tmp
            elif Weight[ x[j-1][0] ] == Weight[ x[j][0] ]:
                if x[j-1][1] > x[j][1]:
                    tmp = x[j]
                    x[j] = x[j-1]
                    x[j-1] = tmp
                
    return ( x )

def HighCardVal( x ):
    
    MaxVal = Weight[ x[0][0] ]
    
    for i in range( 1, len(x) ):
        MaxVal = max( MaxVal, Weight[ x[i][0] ] )
        
    return ( MaxVal )
    
def hasRoyalFlush( x ):
    
    D = {}
    
    D[ x[0][0] ] = 1
    
    for i in range( 1, len(x) ):
        if x[i][1] != x[0][1]:
            return ( False )
        D[ x[i][0] ] = 1
        
    for i in ['T','J','Q','K','A']:
        if i not in D:
            return ( False )
            
    return ( True )
    
def hasStraightFlush( x ):
    return ( hasStraight(x) and hasFlush(x) )
    
def StraightFlushVal( x ):
    return ( HighCardVal( x ) )

def hasFourOfAKind( x ):

    for i in range( 0, len(x)-3 ):
        if x[i][0] == x[i+1][0] == x[i+2][0] == x[i+3][0]:
            return ( True )
    
    return ( False )
    
def FourOfAKindVal( x ):

    for i in range( 0, len(x)-3 ):
        if x[i][0] == x[i+1][0] == x[i+2][0] == x[i+3][0]:
            return ( x[i][0] )
    
    return 0

def hasFlush( x ):
    
    for i in range( 1, len(x) ):
        if x[i][1] != x[0][1]:
            return ( False )
            
    return ( True )
    
def FlushVal( x ):
    return ( x[0][1] )
    
def hasThreeOfAKind( x ):

    for i in range( 0, len(x)-2 ):
        if x[i][0] == x[i+1][0] == x[i+2][0]:
            return ( True )

    return ( False )

def ThreeOfAKindVal( x ):

    for i in range( 0, len(x)-2 ):
        if x[i][0] == x[i+1][0] == x[i+2][0]:
            return ( x[i][0] )

    return 0
    
def hasStraight( x ):

    for i in range( 0, len(x)-1 ):
        if Weight[ x[i][0] ] != Weight[ x[i+1][0] ] - 1:
            return ( False )
            
    return ( True )
    
def StraightVal( x ):
    return ( HighCardVal( x ) )
    
def hasOnePair( x ):

    NumOfPairs = 0

    i = 0
    
    while i < len(x)-1:
        if x[i][0] == x[i+1][0]:
            NumOfPairs += 1
            i += 1
        i += 1
    
    return ( NumOfPairs == 1 )

def OnePairVal( x ):

    i = 0
    
    while i < len(x)-1:
        if x[i][0] == x[i+1][0]:
            return ( Weight[ x[i][0] ] )
        i += 1
            
    return 0    
            
def hasTwoPairs( x ):

    NumOfPairs = 0

    i = 0
    
    while i < len(x)-1:
        if x[i][0] == x[i+1][0]:
            NumOfPairs += 1
            i += 1
        i += 1
    
    return ( NumOfPairs == 2 )

def TwoPairVal( x ):

    MaxVal = 0

    i = 0
    
    while i < len(x)-1:
        if x[i][0] == x[i+1][0]:
            MaxVal = max( MaxVal, Weight[ x[i][0] ] )
            i += 1
        i += 1
        
    return ( MaxVal )
    
def hasFullHouse( x ):
    
    if x[0][0] == x[1][0] == x[2][0] and x[3][0] == x[4][0]:
        return ( True )
    if x[0][0] == x[1][0] and x[2][0] == x[3][0] == x[4][0]:
        return ( True )
    
    return ( False )
    
def FullHouseVal( x ):
    
    if x[0][0] == x[1][0] == x[2][0] and x[3][0] == x[4][0]:
        return ( ( Weight[ x[0][0] ], Weight[ x[3][0] ] ) )
    if x[0][0] == x[1][0] and x[2][0] == x[3][0] == x[4][0]:
        return ( ( Weight[ x[2][0] ], Weight[ x[0][0] ] ) )
    
    return ( (0,0) )
    
def find_category( x ):

    category = 1#highest value card
    
    if hasRoyalFlush( x ):
        category = 10
    elif hasStraightFlush( x ):
        category = 9
    elif hasFourOfAKind( x ):
        category = 8
    elif hasFullHouse( x ):
        category = 7
    elif hasFlush( x ):
        category = 6
    elif hasStraight( x ):
        category = 5
    elif hasThreeOfAKind( x ):
        category = 4
    elif hasTwoPairs( x ):
        category = 3
    elif hasOnePair( x ):
        category = 2
        
    return ( category )
    
def game( P1, P2 ):

    a = find_category( P1 )
    b = find_category( P2 )
    
    if a > b:
        return ( True )
    elif a < b:
        return ( False )
    
    if a == 10:
        return ( 0 )
    elif a == 9:
        if StraightFlushVal( P1 ) != StraightFlushVal( P2 ):
            return ( StraightFlushVal( P1 ) > StraightFlushVal( P2 ) )
    elif a == 8:
        if FourOfAKindVal( P1 ) != FourOfAKindVal( P2 ):
            return ( FourOfAKindVal( P1 ) > FourOfAKindVal( P2 ) )
    elif a == 7:
        if FullHouseVal( P1 ) != FullHouseVal( P2 ):
            return ( FullHouseVal( P1 ) > FullHouseVal( P2 ) )
    elif a == 6:
        if FlushVal( P1 ) != FlushVal( P2 ):
            return ( FlushVal( P1 ) > FlushVal( P2 ) )
    elif a == 5:
        if StraightVal( P1 ) != StraightVal( P2 ):
            return ( StraightVal( P1 ) > StraightVal( P2 ) )
    elif a == 4:
        if ThreeOfAKindVal( P1 ) == ThreeOfAKindVal( P2 ):
            return ( ThreeOfAKindVal( P1 ) > ThreeOfAKindVal( P2 ) )
    elif a == 3:
        if TwoPairsVal( P1 ) != TwoPairsVal( P2 ):
            return ( TwoPairsVal( P1 ) > TwoPairsVal( P2 ) )
    elif a == 2:
        if OnePairVal( P1 ) != OnePairVal( P2 ):
            return ( OnePairVal( P1 ) > OnePairVal( P2 ) )
    
    for i in range( len(P1)-1, -1, -1 ):
        if Weight[ P1[i][0] ] != Weight[ P2[i][0] ]:
            return ( Weight[ P1[i][0] ] > Weight[ P2[i][0] ]  )
    
    return ( False )
    
ans = 0

for i in range( 0, 1000 ):
    x = raw_input().split( " " )
    
    P1 = sort_hand( x[0:5] )
    P2 = sort_hand( x[5:] )
    
    ans += game( P1, P2 )
    
print "%d" % (ans)