names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
pmap = {
}
for n, h in zip(names, heights):
    print(n, h)
    pmap[h] = n
tmp = list(reversed(sorted(list(pmap.keys()))))
names = []
for t in tmp:
    names.append(pmap[t])
