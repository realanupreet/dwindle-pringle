st = "11122321"
aas = ""
i = 0
while i < len(st):
    j = 0
    f = 0
    while i+j < len(st) and st[i] == st[i+j]:
        f += 1
        j += 1
    print(f"f of {st[i]} is", f)
    aas += str(f)+st[i]
    i += j
print(aas)


def countandsay(n):
    if n == 1:
        return "1"
    aas = ""
    stm = countandsay(n-1)
    i = 0
    while i < len(stm):
        j = 0
        f = 0
        while i+j < len(stm) and stm[i] == stm[i+j]:
            f += 1
            j += 1
        # print(f"f of {stm[i]} is", f)
        aas += str(f)+stm[i]
        i += j
    return aas


print("\n*** *** *** *** ***\n")

print(countandsay(3))
