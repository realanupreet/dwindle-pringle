x = 2.000
n = 10
if x == 0:
    return 0
if n == 0:
    return 1
if n == 1:
    return x


def powhelper(x, n):
    if x == 0:
        return 0
    if n == 1:
        return x
    print(f"for {x} {n}")
    res = powhelper(x, n // 2)
    res = res * res
    return x * res if n % 2 else res


res = powhelper(x, abs(n))

return res if n >= 0 else 1 / res
