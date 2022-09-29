mat = [
    [3],
    [2],
    [2],
    [2],
    [2],
    [2],
    [2],
]
r = len(mat)
c = len(mat[0])
res = [[0]*(c) for _ in range(r)]
print(r)
if r == 0:
    res = mat[0]

print("m=>", r)
print("m=>", c)


def printmat(mati, a, b):
    for i in range(a):
        for j in range(b):
            print(f"[{i}{j}]", end="")
            print(f" {mati[i][j]} ", end="")
        print("")
    print("========")


printmat(mat, r, c)
printmat(res, r, c)

for i in range(r-1):
    for j in range(c-1):
        p = i
        q = j
        temparr = []
        # temparr.append((f"{i}{j}"))
        temparr.append((p, q))

        while p < r-1 and q < c-1:
            p += 1
            q += 1
            # temparr.append(f"{p}{q}")
            temparr.append((p, q))
        if i != 0 and j != 0:
            break

        print("temparr ==>", temparr)

        resi = []
        for t in temparr:
            # print(t)
            x = int(t[0])
            y = int(t[1])
            resi.append(mat[x][y])
        resi.sort()
        for z, t in zip(resi, temparr):
            res[int(t[0])][int(t[1])] = z
        # printmat(res, len(res), len(res[0]))
    # print()

# print("r =>", r, "c =>", c)
r = r-1
c = c-1
# print("r =>", r, "c =>", c)

# r = 3
# c = 4
# 3,0
# print(0, c)
# print(r, 0)

res[0][c] = mat[0][c]
res[r][0] = mat[r][0]
print("res")
printmat(res, r+1, c+1)
# gibdiagonal(2,2)


# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33
# l = [0]*c
