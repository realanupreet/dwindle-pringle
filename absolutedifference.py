nums = [3, 2, 1, 5, 4]

k = 2

t = 0

for n in nums:
    for u in nums:
        print(n, u, n-u)
        if abs(n-u) == k:
            print("yess")
            t += 1
print("======\n\n======\nAnswer", int(t/2))
