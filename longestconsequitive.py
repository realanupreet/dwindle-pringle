nums = []
# nums = [0,3,7,2,5,8,4,6,0,1]
nums=set(nums)
ans=0
for n in nums:
    # print(n)
    tmpans=1
    if n-1 not in nums:
        # print("yes",n-1,"available")
    # else:
        while n+1 in nums:
            # print(n,n+1)
            n=n+1
            # print(" tans ->",tmpans)
            tmpans+=1
            # print(" tans ->",tmpans)
    if tmpans > ans:
        ans=tmpans

    # for u in nums:
    #     print("",n-u)

# # nmap={}
# mmap={}
# # for n in nums:
# #     nmap[n]=-1
# for n in nums:
#     if n+1 in nums:
#         # print("yes",n,"->",n+1)
#         mmap[n]=n+1
# # res=[]
# ans=0
# for m in mmap:
#     # print("m",m)
#     k=m
#     temp=[]
#     temp.append(m)
#     # temp.append(m+1)
#     while k in mmap:
#         # print(" k",k,k+1)
#         temp.append(k+1)
#         k=k+1
#     if len(temp)>ans:
#         ans=len(temp)
#     # res.append(temp)