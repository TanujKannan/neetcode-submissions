class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        used = [False]*n

        def recurse():
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True


                recurse()

                path.pop()
                used[i] = False
        
        recurse()
        return res
        