F = {}

F[0] = 1
F[1] = 1

ans = 0
i = 2

while 1:
	F[i] = F[i-1] + F[i-2]

	if F[i] > 4000000:
		break

	if F[i] % 2 == 0:
		ans += F[i]

	i += 1

print "%d" % (ans)
