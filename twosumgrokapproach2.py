arr = [2,5,9,11]

# 2+9=11
# 11-2=9
tar=11
nmap={}
for a in range(0,len(arr)):
    print("a",a)
    if arr[a] not in nmap:
        nmap[arr[a]]=0
    print(nmap)

for a in arr[:len(arr)//2]:
    if tar-a in nmap:
        print("Success,",a,tar-a)