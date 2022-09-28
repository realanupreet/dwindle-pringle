
nums = [2, 14, 18, 22, 22]

nums.sort()
for i in range(0, len(nums)-1):
    # print(i)
    print(i, i+1, "===>", nums[i], nums[i+1])
    if nums[i] == nums[i+1]:
        print("T")
        pass
