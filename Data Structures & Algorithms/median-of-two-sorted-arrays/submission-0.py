class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        
        m = len(A)
        n = len(B)

        even = ((m+n)%2 == 0)

        half = (m+n+1)//2

        left = max(0, half - n)
        right = min(m, half)

        while left <= right:
            i = (left+right)//2
            j = half - i

            left1 = A[i-1] if i > 0 else float('-inf')
            left2 = B[j-1] if j > 0 else float('-inf')
            right1 = A[i] if i < m else float('inf')
            right2 = B[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if even:
                    return (max(left1, left2) + min(right1, right2))/2.0
                else:
                    return max(left1, left2)
            elif left1 > right2:
                right = i - 1
            
            elif left2 > right1:
                left = i + 1
        
        return -1


        