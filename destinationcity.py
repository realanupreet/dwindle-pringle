paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

flatten_paths = []
pmap = {}
i = 0
for p in paths:
    # print(p)
    for i in p:
        flatten_paths.append(i)

flatten_paths = sorted(flatten_paths)

for f in flatten_paths:
    if f not in pmap:
        pmap[f] = 0
    else:
        pmap[f] += 1
snd = []
# print(pmap.keys())
for p in pmap.keys():
    # print(p)
    if pmap[p] == 0:
        snd.append(p)

for p in paths:
    for s in snd:
        if p[1] == s:
            print("woo", p[1])
