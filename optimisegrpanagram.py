strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ["","",""]
smap = {}
for s in strs:
    # print(s)
    print(sorted(s))
    ss=sorted(s)
    if tuple(ss) in smap:
        smap[tuple(ss)]+=[s]
    else:
        smap[tuple(ss)]=[s]
res=[]
for s in smap.keys():
    print("---------------->",s)
    res.append(smap[s])
print(smap)
print(res)