s = "aaabbbacccbc"
smap = {}
for s in s:
    if s not in smap:
        smap[s] = 1
    else:
        smap[s] += 1
m = smap[s[0]]
for i in smap.keys():
    if smap[i] != m:
        print(False)
