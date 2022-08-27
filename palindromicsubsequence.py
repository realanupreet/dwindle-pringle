st = "aaa"
# st = "bcb"
# l = 1
subseq = []


def chkpalin(start, end):
    while start < end:
        if st[start] == st[end]:
            # print(st[start], "==", st[end])
            start += 1
            end -= 1
        else:
            # print(st[start], "!=", st[end])
            return False
    return True


# print(chkpalin(0, 5))
# for m in range(0, len(st)):

for l in range(0, len(st)):

    for i in range(len(st)-l):
        # print("i ==>", st[i])
        if chkpalin(i, i+l):
            print("woohoo", st[i:i+l+1])
            subseq.append(st[i:i+l+1])
print(len(subseq))

# 134217727
