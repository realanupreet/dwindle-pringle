nums = [1, 1, 2]
print(len(nums)//2)
for i in range(0, len(nums), 2):
    print("i is", i)
    if i+1 < len(nums):
        if nums[i] != nums[i+1]:
            print(nums[i])
    if nums[-1] != nums[-2]:
        print(nums[-1])


def uniqueElement(arr, n):
    # Write your code here
    if len(nums) == 1:
        return nums[0]
    for i in range(0, len(nums), 2):
        # print("i is", i)
        if i+1 < len(nums):
            if nums[i] != nums[i+1]:
                return nums[i]
    if nums[-1] != nums[-2]:
        return nums[-1]
    pass


print(uniqueElement(nums, 3))
