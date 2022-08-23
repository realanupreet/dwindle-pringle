str = " "
newstr = ""
for s in str:
    if s.isalnum():
        newstr += s.lower()
for i in range(0, len(newstr)):
    print("i -->", newstr[i], "|| -i -->", newstr[-i-1])
    if newstr[i] != newstr[-i-1]:
        print("not palin")
