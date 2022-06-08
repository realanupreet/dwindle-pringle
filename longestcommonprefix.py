strs = ["a"]
# tillwhen = 1000000000
# for str in strs:
#     print(len(str))
#     tillwhen = min(tillwhen, len(str))

# a = []
# for j in range(tillwhen):
#     for i in range(len(strs)-1):
#         if strs[i][j] == strs[i+1][j]:
#             print(f"yes {strs[i]}[{j}] == {strs[i+1]}[{j}]")
#         else:
#             print("no")
#             break
#     a.append(strs[i][j])


def fun(strs):
    if len(strs) == 1:
        return strs[0]
    tillwhen = 1000000000
    for str in strs:
        print(len(str))
        tillwhen = min(tillwhen, len(str))

    a = [""]
    for j in range(tillwhen):
        for i in range(len(strs)-1):
            if strs[i][j] == strs[i+1][j]:
                print(f"yes {strs[i]}[{j}] == {strs[i+1]}[{j}]")
            else:
                print("no")
                return "".join(a)
        a.append(strs[i][j])
        if len(a) == tillwhen+1:
            return "".join(a)
    return


print(fun(strs))
