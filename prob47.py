memo = {}

def distinct_fact( n ):

    if n in memo:
        return ( memo[n] )
    
    S = set()
    
    tmp = n
    
    idx = 2
    
    while tmp > 1:
        
        if  tmp % idx == 0:
            S.add( idx )
            if len(S) > 4:
                tmp = 0
                break
        
        while tmp % idx == 0:
            tmp /= idx
        
        idx += 1
    
    memo[n] = len(S)
    
    return ( memo[n] )
    
i = 1

while True:
    i += 1
    counter = 0
    for j in range( 0, 4 ):
        if distinct_fact( i+j ) != 4:
            continue
        else:
            counter += 1
    if counter == 4:
        break
    
print "%d" % (i)