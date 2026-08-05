class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break

            j = i + 1
            k = n - 1

            while j < k:
                target = -1*nums[i]
                curSum = nums[j] + nums[k]
                if curSum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif curSum > target:
                    k -= 1
                else:
                    j += 1
        return res        