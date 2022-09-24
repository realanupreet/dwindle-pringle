s = ["h", "e", "l", "l", "o", 'b', 'r', 'a', 'd']
i = 0
j = len(s)-1
while (i < j) and (i < len(s)):
    c = s[i]
    s[i] = s[j]
    s[j] = c
    print(i, j)
    i += 1
    j -= 1
