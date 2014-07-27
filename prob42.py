x = raw_input().replace("\"","").split(',')

def t( n ):
    return ( 0.5 * n * ( n + 1 ) )

ans = 0
    
for i in x:
    tmp = 0
    for j in i:
        tmp += ord(j)-64
    idx = 1
    while t( idx ) < tmp:
        idx += 1
    if t( idx ) == tmp:
        ans += 1
        
print "%d" % (ans)