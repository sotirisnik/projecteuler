memo = {}
cube = {}

i = 1

while True:

    tmp = ''.join( sorted( str(i*i*i) ) )
    
    if tmp not in memo:
        memo[ tmp ] = 1
        cube[ tmp ] = i
    else:
        memo[ tmp ] += 1
        if memo[ tmp ] == 5:
            print "%d" % ( cube[ tmp ]**3 )
            exit(0)
    
    i += 1
    