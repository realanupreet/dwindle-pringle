nums = [-1,0,3,5,9,12]
target = 13

start = 0
end = len(nums)-1
print("size",len(nums))
# 0, 6
# 0<6; mid=3; nums[mid], nums[3]= 5 != 13
# 
# 
# s=4, , mid=5 = 12 < 13
while start<=end:
    print("S",start,"end",end)
    mid = start + (end-start)//2
    print("mid",mid)
    if nums[mid] == target:
        print(mid)
        break
    elif target < nums[mid]:
        end = mid-1
    else:
        start = mid+1

print(-1)


