# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 2
# XC
# MM
# Sample Output 2:
# 90
# 2000

s= "MM"
def roman(s):
    res=0
    cmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    c=0
    while c<len(s):
        if c+1<len(s) and cmap[s[c+1]] > cmap[s[c]]:
            res-=cmap[s[c]]
        else:
            res+=cmap[s[c]]
        c+=1
        # print("from loop",res)
    # print("after loop", res)
    return res

print(roman(s))



