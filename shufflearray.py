class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array1 = nums[:len(nums)//2]
        array2 = nums[len(nums)//2:]
        lst = []
        for i in range(len(array1)):
            lst.append(array1[i])
            lst.append(array2[i])
        return lst
