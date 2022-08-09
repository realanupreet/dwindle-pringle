haystack = "hellpo"
needle = "lp"
ans = -1
flag = 0
if len(needle) == 0:
    print("booie")
for i in range(len(haystack)):
    print("i is", i)
    if haystack[i] == needle[0]:
        # print(f"means {haystack[i]} == {needle[0]}")
        if len(haystack) >= (i+len(needle)):
            for j in range(len(needle)):
                # print(f"j is {j}")
                if haystack[i+j] == needle[j]:
                    # print("ok")
                    pass
                else:
                    # print("no wtf")
                    flag = -1
            if flag == 0:
                print("-------------> ans is ", i)
            flag = 0

print("boo")
