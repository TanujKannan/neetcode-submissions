class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        #Take XOR of all numbers from 0 to n
        xor = 0
        for i in range(n+1):
            xor = xor ^ i

        #And then take XOR of that through nums
        for num in nums:
            xor = xor ^ num

        #Number at the end will be the missing number
        return xor
        