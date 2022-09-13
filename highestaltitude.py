gain = [-5, 1, 5, 0, -7]
# ngain = []
maxg = 0
rg = 0
for g in gain:
    rg += g
    if rg > maxg:
        maxg = rg
