jewels = "aA"
stones = "aAAbbbb"
c = 0
for s in stones:
    for j in jewels:
        if s == j:
            c += 1
