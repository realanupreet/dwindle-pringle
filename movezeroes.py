nums = [0, 0, 1]
# zc=0
for n in nums:
    if n == 0:
        nums.remove(n)
        nums.append(0)
