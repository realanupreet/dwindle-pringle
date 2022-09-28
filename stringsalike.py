vmap = {'a': 0,
        'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
s = "book"
ns1 = s[:(len(s)//2)]
ns2 = s[(len(s)//2):]
ao = 0
for a in ns1:
    if a in vmap:
        ao += 1
bo = 0
for b in ns2:
    if b in vmap:
        bo += 1
print(bo == ao)
