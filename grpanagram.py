strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ["a", "a", "a"]
# strs = [""]

# if len(strs)>1:
#     print("yayyy")
# else:
# # print([strs])
# if strs == ["", "", ""]:
#     print([strs])


def validana(s, t):
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    for a in t:
        if a not in dic:
            # print("boo")
            return False
        else:
            dic[a] -= 1
    for c in s:
        if dic[c] != 0:
            # print("boo")
            return False
    # print("Yayy")
    return True


res = []
# rmap = {}
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
            print(strs[i], strs[j])
            if strs[i] in tmap:
                tmap[strs[i]].append(strs[j])
                # rmap[strs[i]].append(strs[j])
            else:
                tmap[strs[i]] = [strs[j]]
                # rmap[strs[i]] = [strs[j]]

            print(tmap)
            # print("\n----->",rmap,"\n")

    print("keys are ==>", list(tmap.keys()))
    res.append(tmap[list(tmap.keys())[0]])

print("before removing unnecessary shit", res)
bres = {}
newres = []
for r in res:
    # print("r is ",r)
    if tuple(r) in bres:
        continue
    else:
        for e in res:
            if tuple(e) in bres:
                continue
            else:
                # if r == e:
                #     continue
                print("r =>", r, "e =>", e)
                if validana(r[0], e[0]):
                    # if len(r) > len(e):

                    if r != e and len(r) > len(e):
                        print("removed", e)
                        bres[tuple(e)] = 1
                    # else:
                        # res.remove(r)
                    pass

# for r in range(len(res)):
#     print("r is",r,res[r])
#     for e in range(r+1,len(res)-1):
#         print("   e is",e, res[e])
#         if validana(res[r][0], res[e][0]):
#             print("   removed",res[e])
#             res.remove(res[e])
#         print("   res is",res)

# print("=====>", res)
print("bres", bres)
newres = [r for r in res if tuple(r) not in bres]
print("after", newres)
