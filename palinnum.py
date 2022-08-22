num = 121
numstr = str(num)
revstr = ""
for n in numstr:
    revstr = n + revstr

if revstr == numstr:
    print(True)
else:
    print(False)
