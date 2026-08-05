class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        nums.sort()
        def recurse(start, remaining):
            #Summed to target so note it down
            if remaining == 0:
                res.append(path[:])
                return
            
            #Now pick a door, explore it, come back and try a new one
            for i in range(start, n):
                if nums[i] > remaining:
                    break
                #Pick the door
                path.append(nums[i])

                #Explore again
                recurse(i, remaining - nums[i])

                #Come back, refresh notebook, for future doors
                path.pop()

        recurse(0, target)
        return res
        