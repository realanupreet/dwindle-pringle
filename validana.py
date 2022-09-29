# sorting
# searching -> wont work because we need to get the occurences also right
# hashmap

s = "anagram"
t = "nagaram"
s = list(s)
t = list(t)
s.sort()
t.sort()
if s == t:
    print("Y")
else:
    print("N")
