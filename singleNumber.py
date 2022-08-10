class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nmap = {}
        for i in range(len(nums)):
            # print(nums[i])
            if nums[i] in nmap:
                nmap[nums[i]] += 1
            else:
                nmap[nums[i]] = 1

        for n in nmap.keys():
            if nmap[n] == 1:
                return n
