s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
k=""
if words[0] != s[:len(words[0])]:
    print("False")
for w in words:
    k+=w
    if k==s:
        print("Yes")