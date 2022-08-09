import math
x = 1
s = 0
e = 2**31
# m = 0
ans = 0
while(s <= e):
    m = s+(e-s)/2
    if m*m <= x:
        ans = m
        s = m+1
    else:
        e = m-1
print(math.trunc(ans))
