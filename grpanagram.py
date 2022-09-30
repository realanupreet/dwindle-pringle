strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = [""]

# if len(strs)>1:
#     print("yayyy")
# else:
# print([strs])


def validana(s, t):
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if s == t:
        return True
    else:
        return False


res = []

for i in range(len(strs)):
    # for a in res:
    #     for b in a:
    #         print("                    ",a,b,strs[i])
    #         if strs[i] == b:
    #             break
    print("==========", strs[i], "==")
    tmap = {}
    for j in range(i, len(strs)):
        if validana(strs[i], strs[j]):
            # print(strs[i], strs[j])
            if strs[i] in tmap:
                tmap[strs[i]].append(strs[j])
            else:
                tmap[strs[i]] = [strs[j]]

            print(tmap)

    # print("keys are ==>", list(tmap.keys()))
    res.append(tmap[list(tmap.keys())[0]])

print(res)

for r in res:
    for e in res:
        # print(r, e)
        if validana(r[0], e[0]):
            if len(r) > len(e):
                res.remove(e)
            # else:
                # res.remove(r)
            pass
# print("=====>", res)
print(res)
