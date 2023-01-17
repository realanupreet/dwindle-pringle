arr=[-3, -1, 0, 1, 2]
newarr=[0]*len(arr) #makes [0,0,0,0,0] empty array

left = 0
right = len(arr) - 1
highindex = right

while left<=right:
    if arr[left]**2 > arr[right]**2:
        newarr[highindex] = arr[left]**2
        left+=1
    else:
        newarr[highindex] = arr[right]**2
        right-=1
    highindex-=1

print(newarr)