i = 1

text = ""

while len(text) < 1000000:
    text += str(i)
    i += 1
    
ans = 1

for i in range( 0, 7 ):
    ans *= int( text[10**i-1] )
    
print "%d" % (ans)