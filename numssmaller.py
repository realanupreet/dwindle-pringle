nums = [8, 1, 2, 2, 3]
newnum = []
for n in nums:
    count = 0
    for i in nums:
        if i < n:
            count += 1
    newnum.append(count)
