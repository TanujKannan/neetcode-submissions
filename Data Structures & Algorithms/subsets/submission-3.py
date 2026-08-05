class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        n = len(nums)
        def dfs(i):
            if i == n:
                res.append(path[:])
                return

            path.append(nums[i])

            dfs(i + 1)

            path.pop()

            dfs(i + 1)
        
        dfs(0)
        return res
        