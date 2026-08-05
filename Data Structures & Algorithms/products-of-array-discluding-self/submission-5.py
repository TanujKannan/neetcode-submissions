'''
Need to return output where output[i] = prod of all nums except nums[i]

First idea to have a prefix and suffix array
prefix[i] = prod of all before i
suffix[i] = prod of all after i

then output[i] = prefix[i]*suffix[i]
O(N) space and time.

Might be able to do single array and do passes.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)

        for i in range(1, len(nums)):
            output[i] = nums[i-1] * output[i-1]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
