Coins = [ 1, 2, 5, 10, 20, 50, 100, 200 ]

memo = {}

def dp( amount, which  ):

    if amount < 0 or which < 0:
        return 0
        
    if amount == 0:
        return 1

    if (amount, which) in memo:
        return ( memo[ (amount, which) ] )
        
    Best = dp( amount - Coins[ which ], which ) + dp( amount, which - 1 )
    
    memo[ (amount, which) ] = Best
    
    return ( Best )
    
print "%d" % ( dp(200, 7) )