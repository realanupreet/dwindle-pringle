class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for a in accounts:
            sum = 0
            for b in a:
                sum += b
            if sum > max:
                max = sum
        return max
