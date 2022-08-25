s = "abccbaacz"
nmap = {}
for i in s:
    if i in nmap:
        nmap[i] += 1
        if nmap[i] == 2:
            print("scream for ", i)
        print("haha")
    else:
        nmap[i] = 1
        print("hehe")
