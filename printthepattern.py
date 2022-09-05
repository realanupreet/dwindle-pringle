# =====================

# GFG POTD

# =====================


# 1*2*3*10*11*12
# --4*5*8*9
# ----6*7
# 2 -> 6
# 3 -> 12
# 4 -> 18

# 1  2  3  4  - 17 18 19 20
#    5  6  7  - 14 15 16
#       8  9  - 12 13
#          10 - 11


# # 5

# 1  2  3  4  5  - 26 27 28 29 30
#    6  7  8  9  - 22 23 24 25
#       10 11 12 - 19 20 21
#          13 14 - 17 18
#             15 - 16

# # 6

# 1  2  3  4  5  6  -
#    7  8  9  10 11 -
#       12 13 14 15 -
#          16 17 18 -
#             19 20 -
#                21 - 22
n = 5
strs = []
pyheight = 0
for i in range(1, n+1):
    # print(i)
    pyheight += i*2
sindex = 1
eindex = pyheight
starting = eindex+1-n
for i in range(0, n):
    # print("i", i)
    strs.append("")
    strs[i] = "--"*i
    pyheight -= i*2

    for j in range(sindex, n-i+sindex):

        # print(" j", j)
        strs[i] += str(j)+"*"
        # if i == 1:
        #     strs.append()
    sindex += n-i
    for k in range(starting, starting+n-i):
        # print(" k", k)
        if k+1 < (starting+n-i):
            strs[i] += str(k)+"*"
        else:
            strs[i] += str(k)
    # print("starting is", starting)
    starting = starting - (n-i) + 1
    # print("starting is", starting)
