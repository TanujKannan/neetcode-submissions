'''
Need to return two distinct indices such that their sum equals given target
Can assume there's only one solution
Need to return answer with smaller index first

Keep a dictionary that stores (num, index) pairs.
For every num, check if (target - num) exists in the dictionary.
If yes, return answer.
Otherwise, populate dictionary.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_dict = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_index_dict:
                return [num_index_dict[complement], index]
            num_index_dict[num] = index
        return []
        