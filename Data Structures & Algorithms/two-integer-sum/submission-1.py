class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i , num in enumerate(nums):
            candidate = target - num
            if candidate in hashMap:
                return [hashMap[candidate], i]
            hashMap[num] = i
        