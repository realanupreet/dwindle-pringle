v1 = "1.1.29.9"
v2 = "1.0000000033.6.8.9"
num1 = ""
num2 = ""
num1arr = []
num2arr = []
for i in range(len(v1)):
    # print(v1[i])
    if v1[i] == ".":
        num1arr.append(int(num1))
        num1 = ""
    else:
        num1 += v1[i]
num1arr.append(int(num1))

for i in range(len(v2)):
    # print(v2[i])
    if v2[i] == ".":
        num2arr.append(int(num2))
        num2 = ""
    else:
        num2 += v2[i]
num2arr.append(int(num2))

i = 0
if len(num1arr) > len(num2arr):
    i = len(num1arr)-len(num2arr)
    for x in range(i):
        num2arr.append(0)
elif len(num2arr) > len(num1arr):
    i = len(num2arr)-len(num1arr)
    for x in range(i):
        num1arr.append(0)

for o in range(len(num1arr)):
    print(o)
    if num1arr[o] > num2arr[o]:
        print("v1 wins")
    elif num2arr[o] > num1arr[o]:
        print("v2 wins")


def compareversions(v1, v2):
    num1 = ""
    num2 = ""
    num1arr = []
    num2arr = []
    for i in range(len(v1)):
        # print(v1[i])
        if v1[i] == ".":
            num1arr.append(int(num1))
            num1 = ""
        else:
            num1 += v1[i]
    num1arr.append(int(num1))

    for i in range(len(v2)):
        # print(v2[i])
        if v2[i] == ".":
            num2arr.append(int(num2))
            num2 = ""
        else:
            num2 += v2[i]
    num2arr.append(int(num2))

    i = 0
    if len(num1arr) > len(num2arr):
        i = len(num1arr)-len(num2arr)
        for x in range(i):
            num2arr.append(0)
    elif len(num2arr) > len(num1arr):
        i = len(num2arr)-len(num1arr)
        for x in range(i):
            num1arr.append(0)

    for o in range(len(num1arr)):
        # print(o)
        if num1arr[o] > num2arr[o]:
            return 1
        elif num2arr[o] > num1arr[o]:
            return -1
    return 0


print("=======\n*** ***\n=======")

print(compareversions("0.1", "1.0.0"))
