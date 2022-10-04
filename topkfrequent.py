nums = [1,1,1,2,1,1,1,1,1,2,3,3,3,3,3,3,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0]
k = 2

nmap={}

for n in nums:
    if n not in nmap:
        nmap[n]=1
    else:
        nmap[n]+=1

print(sorted(nmap,key=nmap.get,reverse=True)[:k])

# kmap={}
# for n in nmap:
#     kmap[nmap[n]]=n
# print(list(reversed(sorted(list(kmap.keys())))))
# listofoccurencedecreasing = (list(reversed(sorted(list(kmap.keys())))))

# listofoccurencedecreasing=listofoccurencedecreasing[:k]

# res=[]
# for l in listofoccurencedecreasing:
#     res.append(kmap[l])

# print(res)
