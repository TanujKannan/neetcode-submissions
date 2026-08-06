'''
Need to return length of the longest consecutive sequence of numbers
that can be formed.

Sequence only starts if for any num, num - 1 is present.
While num + 1 is present, we update length.
Return max found.

Use a set for quick access.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 1

        if len(nums) == 0:
            return 0

        for num in numSet:
            if num - 1 not in numSet:
                cur = num
                length = 1
                while cur + 1 in numSet:
                    cur += 1
                    length += 1
                maxLen = max(maxLen, length)
        
        return maxLen

        