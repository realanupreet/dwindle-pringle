nums = [1, 2, 3, 2]
nmap = {}
for n in nums:
    if n not in nmap:
        nmap[n] = 0
    else:
        nmap[n] += 1
sum = 0
for n in nmap:
    if nmap[n] == 0:
        # print(n)
        sum += n
