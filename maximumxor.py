nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
sol = 0
for i in reversed(range(32)):
    prefixs = set([x >> i for x in nums])
    sol <<= 1
    candidate = sol + 1
    for p in prefixs:
        if candidate ^ p in prefixs:
            sol = candidate
            break
print(sol)
