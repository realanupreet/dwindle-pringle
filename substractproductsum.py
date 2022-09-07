n = 234
t = []
nn = str(n)
for n in nn:
    t.append(int(n))

s = 0
p = 1
for i in t:
    p *= i
    s += i

print(p-s)
