s = "AABBBCCCEESFFAAA"
hmap = {}
wstart = 0
k = 10
myseq=""
for wend in range(0,len(s)):
    print("wend ->",wend,"wsum ->",myseq,)
    myseq+=s[wend]
    if len(myseq)>k-1:
        print(myseq)
        if myseq not in hmap:
            hmap[myseq] = 1
        else:
            hmap[myseq] +=1
        wstart+=1
        myseq=myseq[1:]

result =[]
for h in hmap:
    if hmap[h]>1:
        result+=[h]

