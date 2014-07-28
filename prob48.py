n = 1000

ans = 0

for i in range( 1, n+1 ):
    ans += (i**i)
    
print "%d" % (ans%(10**10))