n = 1001

x = 1
amount = 2

ans = x

while x < n*n:
    a1 = amount
    an = amount*4
    ans = ans + 4*x + 2*( a1 + an )
    x = x + amount*4
    amount = amount + 2

print "%d" % (ans)