def find_missing_number(nums):
    i, n = 0, len(nums)
    res=[]
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            print("i is", i)
            res.append(i)
        print("end n is", n)
    print(res)


def main():
    print(find_missing_number([4, 0, 3, 1, 6, 8]))


main()
