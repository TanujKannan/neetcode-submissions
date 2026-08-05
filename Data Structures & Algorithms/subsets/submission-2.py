class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)

        def recurse(start):
            if start == n:
                res.append(path[:])
                return 
        
            path.append(nums[start])

            recurse(start + 1)

            path.pop()

            recurse(start + 1)
            
        recurse(0)
        return res
        