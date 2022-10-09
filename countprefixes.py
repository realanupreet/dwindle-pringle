words = ["a","b","c","ab","bc","abc"]
s = "abc"
count =0
for w in words:
    if w == s[:len(w)]:
        count+=1
print(count)
