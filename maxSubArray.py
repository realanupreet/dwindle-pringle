nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxsubarr(nums):
    current_sum = 0
    if len(nums) == 1:
        return nums[0]
    max_sum = max(nums)
    if max_sum < 0:
        return max_sum
    for num in nums:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        max_sum = max(current_sum, max_sum)
    return max_sum


print(maxsubarr(nums))
