nums = [3, 2, 3]
# def majorityElement(nums):
n = len(nums)
n = n/3
m = []
nmap = {}
for j in nums:
    if j not in nmap:
        nmap[j] = 1
    else:
        nmap[j] += 1
for k in nmap.keys():
    if nmap[k] > n:
        m.append(k)
