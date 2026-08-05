class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        n = len(nums)

        def dfs(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return 
            
            for i in range(start, n):
                if nums[i] > remaining:
                    break
                
                path.append(nums[i])

                dfs(i, remaining - nums[i])

                path.pop()
        dfs(0, target)
        return res
        