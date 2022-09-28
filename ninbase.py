n = 34
l = bin(n)
l = l[2:]
k = 6
num = 0

for i in range(len(l)):
    print(i)
    print(" ", l[len(l)-1-i], k**i)
    num += int(l[len(l)-1-i])*(k**i)


# not completed
