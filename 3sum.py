nums = [-1, 0, 1, 2, -1, -4]
ans = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i]+nums[j]+nums[k] == 0:
                print(f"i {nums[i]} j {nums[j]} k {nums[k]}")
                if sorted([nums[i], nums[j], nums[k]]) not in ans:
                    ans.append(sorted([nums[i], nums[j], nums[k]]))
            # print(i,j,k)
print(ans)
