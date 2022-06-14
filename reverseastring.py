st = "the sky is blue"
word = ""
ans = []
a = ""
for s in st:
    if s != " " and s != "\n":
        word = word + s
    else:
        ans.append(word)
        word = ""
ans.append(word)

for i in reversed(range(len(ans))):
    # print(ans[i])
    if ans[i] != "":
        a += " " + ans[i]
print(a[1:])
