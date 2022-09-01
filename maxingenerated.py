# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

n = 10
nums = []
max = -1
for i in range(n+1):
    print(i)
    if i == 0:
        nums.append(0)
    elif i == 1:
        nums.append(1)
    elif i % 2 == 0:
        nums.append(nums[i//2])
    else:
        nums.append(nums[(i-1)//2]+nums[((i-1)//2)+1])

for i in nums:
    # print("i", i)
    if i > max:
        # print(i,">",max)
        max = i
