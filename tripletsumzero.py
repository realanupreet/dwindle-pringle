arr = [-3, 0, 1, 2, -1, 1, -2]
nmap = {}
rmap = {}
ares = []
for a in arr:
    arr = [1, 2, 3, 4, 6]
    tar = 7
    start = 0
    end = len(arr)-1

    while start <= end:
        if arr[start]+arr[end] == tar:
            print([arr[start], arr[end]])
            break
        elif arr[start]+arr[end] > tar:
            end -= 1
        else:
            start += 1
    print("not found")
