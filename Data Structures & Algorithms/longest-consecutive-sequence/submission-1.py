class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0

        for num in numSet:
            if num - 1 not in numSet:
                cur = num
                length = 1
                while cur + 1 in numSet:
                    length += 1
                    cur += 1
                
                max_len = max(max_len, length)
        
        return max_len
        