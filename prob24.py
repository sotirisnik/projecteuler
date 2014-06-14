x = 0

Q = []
  
N = 10
cnt = 0
limit = 1000000

A = []
avail = []

def permute( i ):

    global cnt

    if cnt > limit:
        return
    
    if i == N:
        cnt += 1
        if cnt == limit:
            ans = ""
            for i in A:
                ans += str(i)
            print "%s" % (ans)
        return
        
    for j in range( 0, N ):
        if avail[j]:
            tmp = A[i]
            A[i] = j
            avail[j] = False
            permute( i + 1 )
            avail[j] = True
            A[i] = tmp

for i in range( 0, N ):
    A.append( i )
    avail.append( True )
    
permute( 0 )