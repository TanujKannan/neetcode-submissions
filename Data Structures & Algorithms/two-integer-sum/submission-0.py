class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)

        for i, num in enumerate(nums):
            candidate = target - num
            if candidate in hashMap:
                return [hashMap[candidate], i]
            hashMap[num] = i
        
        return 
        