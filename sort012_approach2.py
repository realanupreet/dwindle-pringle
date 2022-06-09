arr = [2, 0, 2, 1, 1, 0]
a = 0
b = 0
c = 0
for num in arr:
    if num == 0:
        a += 1
    elif num == 1:
        b += 1
    else:
        c += 1
for i in range(a):
    print("i for 0 is", i)
    arr[i] = 0
i = 0
for i in range(a, b+a):
    print("i for 1 is", i)
    arr[i] = 1
for i in range(a+b, a+b+c):
    print("i for 0 is", i)
    arr[i] = 2
