nums = [2, 2, 1, 1, 1, 2, 2]
maap = {}
for num in nums:
    if num in maap:
        maap[num] += 1
    else:
        maap[num] = 1
for ele in maap:
    if maap[ele] >= len(nums)/2:
        print(ele)


def majorityElement(nums):
    maap = {}
    for num in nums:
        if num in maap:
            maap[num] += 1
        else:
            maap[num] = 1
    for ele in maap:
        if maap[ele] >= len(nums)/2:
            return ele


print(majorityElement(nums))
