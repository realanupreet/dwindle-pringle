s = "is2 sentence4 This1 a3"
s = s.split()
smap = {}
for s in s:
    print(s)
    if s[-1] not in smap:
        smap[s[-1]] = s[:-1]
a = ""
for i in range(len(smap.keys())):
    i = i+1
    print(i)
    if i == len(smap.keys()):
        a+=smap[str(i)]
    else:
        a+=smap[str(i)]+" "
