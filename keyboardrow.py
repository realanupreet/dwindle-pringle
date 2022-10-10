words = ["omk"]
row1="qwertyuiop"
row1=set(row1)
row2="asdfghjkl"
row2=set(row2)
row3="zxcvbnm"
row3=set(row3)
res=[]

def check(word, row):
    for w in word:
        if w.lower() not in row:
            return False
    return True

for word in words:
    if check(word,row1):
        res.append(word)
    elif check(word,row2):
        res.append(word)
    elif check(word,row3):
        res.append(word)