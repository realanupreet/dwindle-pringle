s = "anagram"
t = "nagaram"

dic = {}
for c in s:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
for a in t:
    if a not in dic:
        print("boo")
    else:
        dic[a] -= 1
for c in s:
    if dic[c] != 0:
        print("boo")
print("Yayy")


def isAnagram(s: str, t: str) -> bool:
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


print(isAnagram(s, t))
