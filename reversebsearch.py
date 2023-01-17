num = [20,17,15,14,13,12,10,9,8,4]
target = 4

left = 0
right = len(num)-1

while left <= right:
    mid = left+ (right-left)//2
    if num[mid]==target:
        print(mid)
    
    if num[mid]>target:
        left=mid+1
    else:
        right=mid-1

print(-1)