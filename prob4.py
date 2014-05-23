def reverse( x ):
	ret = 0
	while x > 0:
		ret *= 10
		ret += x % 10
		x /= 10
	return ( ret )

def pal( x ):
	return ( x == reverse(x) )

ans = 0

for i in range(100,1000):
	for j in range(100,1000):
		tmp = i * j
		if pal(tmp):
			ans = max( ans, tmp )

print ans
