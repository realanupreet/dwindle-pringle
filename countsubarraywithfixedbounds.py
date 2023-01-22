nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5
count = 0
for k in range(1, len(nums)+1):
    print(k)
    wstart = 0
    for wend in range(1, len(nums)+1):
        print(wstart, wend)
        wsum = nums[wstart:wend]
        if min(wsum) == minK and max(wsum) == maxK and len(wsum) > k-1:
            print("", wsum, "\n  s>", wstart, "\n  e>", wend)
            count += 1
            wstart += 1
            print("wstart incremented", wstart)
