words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
nmap = {}
# k = 1
# for i in range(len(pattern)):
#     if pattern[i] not in nmap:
#         nmap[pattern[i]] = k
#     else:
#         k = nmap[pattern[i]]
#     print(k)
#     if i+1 < len(pattern) and pattern[i] != pattern[i+1]:
#         k = k+1


# ======pattern helper=======
i = 1
for p in pattern:
    if p not in nmap:
        nmap[p] = i
        i += 1

# =====pattern identifier====
s = []
for p in pattern:
    # print(nmap[p])
    s.append(nmap[p])


def patternIndentifier(pattern, nmap):
    s = []
    for p in pattern:
        # print(nmap[p])
        s.append(nmap[p])
    return s


def indexer(pattern):
    nmap = {}
    i = 1
    for p in pattern:
        if p not in nmap:
            nmap[p] = i
            i += 1
    return nmap


def patternCompare(pattern1, pattern2):
    if patternIndentifier(pattern1, indexer(pattern1)) == patternIndentifier(pattern2, indexer(pattern2)):
        print("wooo hooo")
        return True
    else:
        print(":*(")
        return False


ans = []
for w in words:
    if patternCompare(pattern, w):
        ans.append(w)
