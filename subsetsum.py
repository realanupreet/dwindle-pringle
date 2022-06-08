nums = [2, 2, 1, 1]
if len(nums) == 2:
    if nums[0] == nums[1]:
        print("yes")
if len(nums) == 1:
    print("no")
sum = 0
for num in nums:
    sum += num
nums = sorted(nums)

lsum = sum-nums[-1]
rsum = nums[-1]
for i in range(2, len(nums)):
    if lsum == rsum:
        print("yes")
    elif lsum < rsum:
        print("no")
    else:
        print("oh god")
    lsum -= nums[-i]
    rsum += nums[-i]


def subsetsum(nums):
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return True
    if len(nums) == 1:
        return False
    sum = 0
    for num in nums:
        sum += num
    nums = sorted(nums)

    lsum = sum-nums[-1]
    rsum = nums[-1]
    for i in range(2, len(nums)):
        if lsum == rsum:
            return True
        elif lsum < rsum:
            return False
        lsum -= nums[-i]
        rsum += nums[-i]
    return False


print(subsetsum(nums))
