arr = [9, 4, -2, -1, 5, 0, -5, -3, 2, 3]
neg = []
pos = []
res = []
for a in arr:
    if a < 0:
        neg.append(a)
    else:
        pos.append(a)
f = arr[0]
l = 0
n = len(arr)
arr = []
# if f < 0:
for i in range(n):
    if i < len(pos):
        arr.append(pos[i])
    if i < len(neg):
        arr.append(neg[i])

# elif f > 0:
#     for i in range(n):
#         if i < len(pos):
#             arr.append(pos[i])
#         if i < len(neg):
#             arr.append(neg[i])
