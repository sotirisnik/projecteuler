#10^(power-1) <= base^power < 10^power

ans = 0

for j in range( 1, 10 ):

    base = j
    power = 1
    
    while 10**(power-1) <= base**power:
        power += 1
        ans += 1
     
print "%d" % (ans)
