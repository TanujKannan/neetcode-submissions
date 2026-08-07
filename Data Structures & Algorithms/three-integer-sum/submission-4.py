'''
Given nums, want to return all triplets whose sum is 0.
All indices must be distinct.

No duplicate triplets, order of triplets doesn't matter for output.

If sort the input, we can run two sum sorted, for every number.

Duplicate triplets?
    -> Once sorted, equal numbers will be adjacent. So can skip over them.

Optimization:
If our anchor number > 0, we can break since sorted.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #Optimize since won't find triplets after this point anyways.
            if nums[i] > 0:
                break
            
            #Two Sum Sorted Logic
            l = i + 1
            r = len(nums) - 1

            # nums[i] + nums[l] + nums[r] = 0 -> nums[l] + nums[r] = -nums[i]
            targetSum = -nums[i]

            while l < r:
                curSum = nums[l] + nums[r]
                if curSum == targetSum:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                
                elif curSum < targetSum:
                    l += 1
                
                else:
                    r -= 1
        
        return res

            

        