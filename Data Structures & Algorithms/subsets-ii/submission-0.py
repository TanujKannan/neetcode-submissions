class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        n = len(nums)
        nums.sort()

        def recurse(start):
            res.append(path[:]) 
        
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])

                recurse(i+1)

                path.pop()
        
        recurse(0)
        return res
        