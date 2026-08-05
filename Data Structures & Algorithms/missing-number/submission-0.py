class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Take sum of n numbers
        sumN = (n*(n+1))//2

        
        return sumN - sum(nums)
        