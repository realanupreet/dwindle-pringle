nums = [1, 3, 4, 2, 2]


# # def duplicateNum(nums):
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j]:
            # return nums[i]


# duplicateNum(nums)

nums.sort()
for i in range(len(nums)):
    if nums[i] == nums[i+1]:
        print(nums[i])