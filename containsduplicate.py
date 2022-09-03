nums = [1, 2, 3, 1]
nmap = {}
for n in nums:
    if n in nmap:
        nmap[n] += 1
        if nmap[n] >= 2:
            print("Goo Goo Ga Ga")
    else:
        nmap[n] = 1
