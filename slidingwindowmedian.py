nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = []
wstart = 0
median = []
for wend in range(len(nums)+1):
    if wend >= k:
        if k % 2 == 0:
            print(nums[wstart:wend])
            temp = sorted(nums[wstart:wend])[k//2 - 1: k//2+1]
            median = (temp[0]+temp[1])/2
        else:
            print(nums[wstart:wend])
            median = sorted(nums[wstart:wend])[k//2:k//2+1][0]
        res.append('%.5f'%median)
        wstart += 1
