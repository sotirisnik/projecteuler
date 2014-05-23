N = 100

A = {}
memo = {}

def best( x, y ):

	if x == N:
		return A[(x,y)]

	if (x,y) in memo:
		return memo[(x,y)]

	Best = 0

	if (x+1,y) in A:
		Best = max( Best, A[(x,y)] + best(x+1,y) )

	if (x+1,y+1) in A:
		Best = max( Best, A[(x,y)] + best(x+1,y+1) )

	memo[(x,y)] = Best;

	return Best

for i in range(1,N+1):
	x = raw_input().split(" ")
	j = 1
	for k in x:
		A[(i,j)] = int(k)
		j += 1

print best(1,1)
