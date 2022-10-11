s = "foobar"
letter = "k"

count =0
for i in s:
    print(i)
    if i == letter:
        count+=1


print(float.__floor__(count/len(s) * 100))