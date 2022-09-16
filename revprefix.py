word = "abcdefd"
ch = "d"
#  "dcbaefd"
n = ""
l = ""

for i in range(len(word)):
    if word[i] == ch:
        n = word[:i+1]
        l = n[::-1]
        l += word[i+1:]
        break
