class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)


        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                length = 1
                while cur + 1 in num_set:
                    cur += 1
                    length += 1

                max_len = max(max_len, length)

        return max_len              