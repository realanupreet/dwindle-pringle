x = 2.00000
n = 10
res = 1


def powhelper(n, x):
    res = 1
    for i in range(n):
        res = res*x
    return res


if n < 0:
    n = n*-1
    return (1/powhelper(n, x))
elif n == 0:
    return 1
else:
    return powhelper(n, x)
