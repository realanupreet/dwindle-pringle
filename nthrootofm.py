n = 2
m = 9

left = 0
right = m
while left <= right:
    mid = (left+right)/2
    if mid**n == m:
        print(mid)
        break
    elif mid**n > m:
        right = mid
    else:
        left = mid
print(-1)
