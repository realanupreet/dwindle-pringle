s = "What is the solution to this problem"
k = 9
s = s.split()
s = s[0:k]
n = ""
j = 0
for i in s:
    if j == 0:
        n += str(i)
    else:
        n += " "+str(i)
    j += 1
print(n)
